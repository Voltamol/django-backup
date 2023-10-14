from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from .models import Candidate
from .forms import CandidateForm
from .forms import RefereeForm
from .forms import CandidateDocumentsForm
# Create your views here.

def index(request):
    return render(request,'analytics/index.html')

def candidate_profile_view(request):
    return render(request,'analytics/candidate profile view.html')

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
                return HttpResponseRedirect(reverse("analytics:candidate_profile_view"))
            else:
                raise Http404("referee form invalid")
        elif "submit_documents" in request.POST.get('form'):
            documents_form=CandidateDocumentsForm(request.POST)
            if documents_form.is_valid():
                documents_form.save()
                return HttpResponseRedirect(reverse("analytics:candidate_idx"))
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
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('analytics:candidate_idx'))
        else:
            raise Http404("check for mismatching name attributes")
    else:
        return render(request,"analytics/Candidate_signup.html")

def login(request):
    return render(request,"analytics/login.html")

def questionnaire(request):
    return render(request,'analytics/questionaire.html')

def referee_candidates_list(request):
    return render(request,'analytics/referee_candidates_list.html')

def thank_you(request):
    return render(request,'analytics/thank_you.html')