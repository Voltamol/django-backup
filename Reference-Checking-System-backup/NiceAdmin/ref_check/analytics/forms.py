from django import forms
from .models import(Candidate, 
                    Referee, 
                    Candidate_Documents, 
                    Referee_Questionnaire
                    )

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'

class RefereeForm(forms.ModelForm):
    class Meta:
        model = Referee
        fields = '__all__'

class CandidateDocumentsForm(forms.ModelForm):
    class Meta:
        model = Candidate_Documents
        fields = '__all__'

class RefereeQuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Referee_Questionnaire
        fields = '__all__'