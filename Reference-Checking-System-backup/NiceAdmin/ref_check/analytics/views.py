from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'analytics/index.html')

def candidate_profile_view(request):
    return HttpResponse("Candidate Profile View")

def candidate_reports(request):
    return HttpResponse("Candidate Reports")

def candidates(request):
    return HttpResponse("Candidates")

def candidate_idx(request):
    return HttpResponse("Candidate Index")

def candidate_signup(request):
    return HttpResponse("Candidate Signup")

def login(request):
    return HttpResponse("Login")

def questionnaire(request):
    return HttpResponse("Questionnaire")

def referee_candidates_list(request):
    return HttpResponse("Referee Candidates List")

def thank_you(request):
    return HttpResponse("Thank You")