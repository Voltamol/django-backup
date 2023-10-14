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
        referee_form=RefereeForm(request.POST)
        documents_form=CandidateDocumentsForm(request.POST)
        print(referee_form)
        # print(documents_form)
        if documents_form.is_valid():
            email=documents_form.cleaned_data['candidate-email']
            try:
                candidate=Candidate.objects.get(email=email)
            except (KeyError,Candidate.DoesNotExist):
                raise Http404('Candidate does not exist')
            else:
                #saving documents...
                documents=candidate.documents_set.create(
                    job_title=documents_form.cleaned_data['job_title'],
                    cv=documents_form.cleaned_data['cv'],
                    photo=documents_form.cleaned_data['photo']
                )
                #documents.save()
                #saving references...
                if referee_form.is_valid():
                    #references=candidate.referee_set.create()
                    print(dict(referee_form))
                    return HttpResponseRedirect(reverse("analytics:candidate_profile_view"))
                else:
                    raise Http404("referee validation check for mismatching name attributes")
        else:
            raise Http404("documents validation check for mismatching name attributes")
    else:
        return render(request,"analytics/Candidate_idx.html")

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