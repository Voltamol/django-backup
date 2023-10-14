from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import (
    Candidate,
    Referee,
    Candidate_Documents,
    Referee_Questionnaire,
    Progress_Tracker
)
from .forms import CandidateForm
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
    return render(request,"analytics/Candidate_idx.html")

def candidate_signup(request):
    if request.method == 'POST':
        form=CandidateForm(request.POST)
        if form.is_valid():
            #form.save()
            firstname=form.cleaned_data['firstname']
            lastname=form.cleaned_data['lastname']
            phone=form.cleaned_data['phone']
            email=form.cleaned_data['email']
            candidate=Candidate.objects.create(firstname=firstname,lastname=lastname,phone=phone,email=email)
            candidate.save()
            HttpResponseRedirect(reverse('analytics:candidate_idx'))
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