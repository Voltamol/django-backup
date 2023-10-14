from django.urls import path
from . import views

app_name='analytics'
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('candidate_profile_view', views.candidate_profile_view, name='candidate_profile_view'),
    path('Candidate_Reports', views.candidate_reports, name='candidate_reports'),
    path('candidates', views.candidates, name='candidates'),
    path('candidate_idx', views.candidate_idx, name='candidate_idx'),
    path('candidate_signup', views.candidate_signup, name='candidate_signup'),
    path('login', views.login, name='login'),
    path('questionnaire', views.questionnaire, name='questionnaire'),
    path('referee_candidates_list', views.referee_candidates_list, name='referee_candidates_list'),
    path('thank_you', views.thank_you, name='thank_you'),
]