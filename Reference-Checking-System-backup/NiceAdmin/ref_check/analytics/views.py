from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.http import JsonResponse
from .models import Candidate
from . models import Referee
from . models import SystemAdmin
from . models import Candidate_Documents
from . models import Verification
from .forms import CandidateForm
from .forms import RefereeForm
#from .forms import RefereeBasicForm
from .forms import CandidateDocumentsForm
from .forms import LoginForm
from .forms import RefereeQuestionnaireForm
from .forms import RefereeHierarchicalForm
# Create your views here.

def index(request):
    if request.session.get('user','') == 'Admin':
        return render(request,'analytics/index.html')
    else:
        return HttpResponseRedirect(reverse('analytics:login'))

def candidate_profile_view(request):
    referee_form=RefereeHierarchicalForm()
    status=request.session.get('not_found',0)
    if request.session.has_key('not_found'):
        request.session.pop('not_found')
    email=request.session.get('email')
    candidate=Candidate.objects.get(email=email)
    documents=candidate.candidate_documents_set.first()
    context={'referee_form':referee_form,'status':status,'documents':documents}
    return render(request,'analytics/candidate profile view.html',context=context)

def handle_update(model,post_data,label):
    
    email=post_data.get('email')
    email=email[0] if isinstance(email,list) else email
    
    candidate=Candidate.objects.get(email=email)
    model_fields=[
        field.get_attname() 
        for field in model._meta.get_fields()
        if hasattr(field,'get_attname')
    ]
    shared_attributes={
        key:value 
        for key,value in post_data.items()
        if key in model_fields
    }
    
    
    if label=='Update_Referee':
        comp_name=shared_attributes.get('comp_name')
        comp_name=comp_name[0] if isinstance(comp_name,list) else comp_name
        verifications=Verification.objects.filter(
            candidate=candidate, referee__comp_name=comp_name
        )
        
        for verification in verifications:
            
            for key,value in shared_attributes.items():
                setattr(verification.referee,key,value[0])
            verification.referee.save()
            return True
    elif label=='Update_Candidate':
        for key,value in shared_attributes.items():
            setattr(candidate,key,value[0])
        documents=candidate.candidate_documents_set.first()
        updates=dict(
            job_title=post_data.get('job_title')[0],
            cv=post_data.get('cv')[0],
            photo=post_data.get('photo')[0]
        )
        cv=updates.get('cv')
        if not cv:
            updates.pop('cv')
        
        photo=updates.get('photo')
        if not photo:
            updates.pop('photo')
        for key,value in updates.items():
            setattr(documents,key,value)
        candidate.email=email
        candidate.save()
        documents.save()
        return True
    elif label=='Change Password':
        current=post_data.get('current_password')
        current=current[0] if isinstance(current,list) else current
        new=post_data.get('new_password')
        confirmation=post_data.get('confirmation')
        if new==confirmation and candidate.password==current:
            new=new[0] if isinstance(new,list) else new
            candidate.password=new
            candidate.save()
            return True
        else:
            return False
        

def update(request):
    if request.method == 'POST':
        post_data=dict(request.POST)
        if request.session.has_key('email'):
            post_data['email']=request.session['email']
        if 'Update_Referee' in request.POST.get('form'):
            boolean=handle_update(Referee,post_data,'Update_Referee')
            if boolean:
                return JsonResponse({'message':'Referee updated successfully'})
            else:
                return JsonResponse({'message':'operation failed'})
        elif 'Update_Candidate' in request.POST.get('form'):
            post_data={**post_data,**dict(request.FILES)}
            boolean=handle_update(Candidate,post_data,'Update_Candidate')
            if boolean:
                return JsonResponse({'message':'Candidate updated successfully'})
            else:
                return JsonResponse({'message':'operation failed'})
        elif 'Change Password' in request.POST.get('form'):
            
            boolean=handle_update(Candidate,post_data,'Change Password')
            if boolean:
                return JsonResponse({'message':'password updated successfully'})
            else:
                return JsonResponse({'message':'operation failed, may be due to incorrect value of current password or the confirmation password does not match the new password'})
            
def candidate_reports(request):
    return render(request,"analytics/Candidate Reports.html")

def candidates(request):
    return render(request,"analytics/candidates.html")

def candidate_idx(request):
    if request.method=='POST':
        if "add_referee" in request.POST.get('form'):
            referee_form=RefereeForm(request.POST)
            if referee_form.is_valid():
                referee=referee_form.save()
                candidate_id=request.session.get('saved_candidate')
                candidate=Candidate.objects.get(id=candidate_id)
                verification=Verification(candidate=candidate,referee=referee,is_verified=False)
                verification.save()
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
            Candidate.objects.get(email=email)
        except (KeyError,Candidate.DoesNotExist):
            if form.is_valid():
                candidate=form.save()
                request.session['saved_candidate']=candidate.id
                request.session['email']=email
                request.session['user']='Candidate'
                return HttpResponseRedirect(reverse('analytics:candidate_idx'))
            else:
                raise Http404("check for mismatching email attributes")
        else:
            return render(request,"analytics/Candidate_signup.html",{'user_exists':1})
    else:
        form=CandidateForm()
        return render(request,"analytics/Candidate_signup.html",{'user_exists':0,'form':form})
    
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
    referee_email=request.session.get('referee_email')
    if request.method=='POST':
        form=RefereeQuestionnaireForm(request.POST)
        if form.is_valid():
            feedback=form.save()
            try:
                verification=Verification.objects.get(candidate_id=feedback.candidate.id,referee=feedback.referee.id)
            except Verification.DoesNotExist:
                verification=Verification(candidate=feedback.candidate, referee=feedback.referee,is_verified=True)
                verification.save()
                return HttpResponseRedirect(reverse('analytics:referee_candidates_list',args=(referee_email,)))
            else:
                verification.is_verified=True
                verification.save()
                return HttpResponseRedirect(reverse('analytics:referee_candidates_list',args=(referee_email,)))
        else:
            raise Http404("disabling might be causing problems")
    else:
        candidate_id=request.COOKIES.get('selected_candidate')
        referee=Referee.objects.get(company_email=referee_email)
        form=RefereeQuestionnaireForm(initial_candidate_id=candidate_id,initial_referee_id=referee.id)
        
        return render(request,'analytics/questionaire.html',{'form':form,'referee_email':referee_email})

def referee_candidates_list(request,referee_email):
    referee=Referee.objects.get(company_email=referee_email)
    documents = Candidate_Documents.objects.filter(
        candidate__verification__is_verified=False,
        candidate__verification__referee_id=referee.id
    )
    documents=set(list(documents))
    if len(documents) == 0:
        return HttpResponseRedirect(reverse('analytics:thank_you'))
    else:
        request.session['referee_email']=referee_email
        return render(request,'analytics/referee_candidates_list.html',{'documents':documents,'referee_email':referee_email})

def thank_you(request):
    return render(request,'analytics/thank_you.html')