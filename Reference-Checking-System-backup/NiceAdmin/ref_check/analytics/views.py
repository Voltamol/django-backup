from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.http import JsonResponse
from .models import Candidate
from . models import Referee
from . models import SystemAdmin
from .forms import CandidateForm
from .forms import RefereeForm
#from .forms import RefereeBasicForm
from .forms import CandidateDocumentsForm
from .forms import LoginForm
# Create your views here.

def index(request):
    if request.session.get('user','') == 'Admin':
        return render(request,'analytics/index.html')
    else:
        return HttpResponseRedirect(reverse('analytics:login'))

def candidate_profile_view(request):
    referee_form=RefereeForm()
    status=request.session.get('not_found',0)
    if request.session.has_key('not_found'):
        request.session.pop('not_found')
    email=request.session.get('email')
    candidate=Candidate.objects.get(email=email)
    documents=candidate.candidate_documents_set.first()
    context={'referee_form':referee_form,'status':status,'documents':documents}
    return render(request,'analytics/candidate profile view.html',context=context)

def handle_update(model,Form,model_name,request):
    try:
        query_dict={model_name:request.POST.get(model_name)}
        model_instance=model.objects.get(**query_dict)
    except (KeyError,model.DoesNotExist):
        request.session['not_found'] = 1
        return False
    else:
        form=Form(request.POST,instance=model_instance)
        if form.is_valid():
            form.save()
        else:
            raise Http404("form invalid")
        return True
    
def update(request):
    if request.method == 'POST':
        if 'Update_Referee' in request.POST.get('form'):
            handle_update(Referee,RefereeForm,'referee_name',request)
        elif 'Update_Candidate' in request.POST.get('form'):
            handle_update(Candidate,CandidateForm,'email',request)
            
def candidate_reports(request):
    return render(request,"analytics/Candidate Reports.html")

def candidates(request):
    return render(request,"analytics/candidates.html")

def candidate_idx(request):
    if request.method=='POST':
        if "add_referee" in request.POST.get('form'):
            referee_form=RefereeForm(request.POST)
            if referee_form.is_valid():
                referee_form.save()
                return JsonResponse({'message': 'success'})
            else:
                raise Http404("referee form invalid")
        elif "submit_documents" in request.POST.get('form'):
            documents_form=CandidateDocumentsForm(request.POST,request.FILES)
            if documents_form.is_valid():
                documents_form.save()
                return HttpResponseRedirect(reverse("analytics:candidate_profile_view"))
            else:
                raise Http404("documents form invalid")
        else:
            print(request.POST)
            raise Http404("you posted an invalid form")
    else:
        referee_form=RefereeForm()
        documents_form=CandidateDocumentsForm()
        return render(request,"analytics/Candidate_idx.html",{'referee_form':referee_form, 'documents_form':documents_form})

def candidate_signup(request):
    if request.method == 'POST':
        form=CandidateForm(request.POST)
        email=request.POST.get('email')
        try:
            user=Candidate.objects.get(email=email)
        except (KeyError,Candidate.DoesNotExist):
            if form.is_valid():
                form.save()
                request.session['email']=email
                request.session['user']='Candidate'
                return HttpResponseRedirect(reverse('analytics:candidate_idx'))
            else:
                raise Http404("check for mismatching email attributes")
        else:
            return render(request,"analytics/Candidate_signup.html",{'user_exists':1})
    else:
        return render(request,"analytics/Candidate_signup.html",{'user_exists':0})
    
def authenticate(model,email,password):
    try:
        model.objects.get(email=email,password=password)
    except (KeyError,model.DoesNotExist):
        return False
    else:
        return True
    
def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            if authenticate(Candidate,email,password):
                if request.session.has_key('login_attempts'):
                    request.session.pop('login_attempts')
                request.session['email']=email
                request.session['user']='Candidate'
                return HttpResponseRedirect(reverse('analytics:candidate_profile_view'))
            elif authenticate(SystemAdmin,email,password):
                if request.session.has_key('login_attempts'):
                    request.session.pop('login_attempts')
                request.session['email']=email
                request.session['user']='Admin'
                return HttpResponseRedirect(reverse('analytics:index'))
            else:
                if not request.session.has_key('login_attempts'):
                    request.session['login_attempts'] = 1
                    return render(request, 'analytics/login.html')
                else:
                    if request.session.get('login_attempts') == 3:
                        request.session.pop('login_attempts')
                        raise Http404("maximum login attempts reached try again later...")
                    else:
                        request.session['login_attempts'] += 1
                        login_attempts=request.session.get('login_attempts',0)
                        return render(request, 'analytics/login.html',{'login_attempts':login_attempts})
        else:
            raise Http404("check for mismatching name attributes")
    else:
        login_attempts=request.session.get('login_attempts',0)
        return render(request,"analytics/login.html",{'login_attempts':login_attempts})

def questionnaire(request):
    return render(request,'analytics/questionaire.html')

def referee_candidates_list(request):
    return render(request,'analytics/referee_candidates_list.html')

def thank_you(request):
    return render(request,'analytics/thank_you.html')