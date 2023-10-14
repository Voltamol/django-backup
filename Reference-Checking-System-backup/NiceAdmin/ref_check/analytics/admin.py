from django.contrib import admin
from .models import(Candidate, 
                    Referee, 
                    Candidate_Documents, 
                    Referee_Questionnaire, 
                    Progress_Tracker)

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'phone', 'email')
    # Add any other desired configuration options or fieldsets

@admin.register(Referee)
class RefereeAdmin(admin.ModelAdmin):
    list_display = ('id', 'comp_name', 'referee_name', 'company_email', 'company_telephone')
    # Add any other desired configuration options or fieldsets

@admin.register(Candidate_Documents)
class CandidateDocumentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'candidate', 'job_title')
    # Add any other desired configuration options or fieldsets

@admin.register(Referee_Questionnaire)
class RefereeQuestionnaireAdmin(admin.ModelAdmin):
    list_display = ('id', 'referee', 'problem_solving', 'communication_skills', 'time_management', 'creativity')
    # Add any other desired configuration options or fieldsets

@admin.register(Progress_Tracker)
class ProgressTrackerAdmin(admin.ModelAdmin):
    list_display = ('id', 'candidate', 'referee', 'status')
    # Add any other desired configuration options or fieldsets