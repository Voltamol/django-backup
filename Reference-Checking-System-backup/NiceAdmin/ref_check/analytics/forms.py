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
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class RefereeForm(forms.ModelForm):
    class Meta:
        model = Referee
        fields = '__all__'
        widgets={
            'comp_name': forms.TextInput(attrs={'class': 'form-control'}), 
            'referee_name': forms.TextInput(attrs={'class': 'form-control'}),
            'company_email': forms.EmailInput(attrs={'class': 'form-control'}), 
            'company_telephone':forms.TextInput(attrs={'class': 'form-control'})
        }


class CandidateDocumentsForm(forms.ModelForm):
    class Meta:
        model = Candidate_Documents
        fields = '__all__'
        widgets={
            'candidate': forms.Select(attrs={'class': 'form-control'}),
            'job_title': forms.TextInput(attrs={'class': 'form-control'}),
            'cv': forms.FileInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }

class RefereeQuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Referee_Questionnaire
        fields = '__all__'
        widgets = {
            'candidate': forms.Select(attrs={'class': 'form-control disabled'}),
            'referee': forms.Select(attrs={'class': 'form-control disabled'}),
            'problem_solving': forms.NumberInput(attrs={'class': 'form-control', 'type': 'range', 'min': '0', 'max': '100', 'value': '50'}),
            'communication_skills': forms.NumberInput(attrs={'class': 'form-control', 'type': 'range', 'min': '0', 'max': '100', 'value': '50'}),
            'time_management': forms.NumberInput(attrs={'class': 'form-control', 'type': 'range', 'min': '0', 'max': '100', 'value': '50'}),
            'creativity': forms.NumberInput(attrs={'class': 'form-control', 'type': 'range', 'min': '0', 'max': '100', 'value': '50'}),
            'willingness_to_learn': forms.NumberInput(attrs={'class': 'form-control', 'type': 'range', 'min': '0', 'max': '100', 'value': '50'}),
            'team_work': forms.NumberInput(attrs={'class': 'form-control', 'type': 'range', 'min': '0', 'max': '100', 'value': '50'}),
            'reliability': forms.NumberInput(attrs={'class': 'form-control', 'type': 'range', 'min': '0', 'max': '100', 'value': '50'}),
            'opinion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        initial_candidate_id = kwargs.pop('initial_candidate_id', None)
        initial_referee_id = kwargs.pop('initial_referee_id', None)
        super().__init__(*args, **kwargs)
        if initial_candidate_id:
            self.initial['candidate'] = initial_candidate_id
        if initial_referee_id:
            self.initial['referee'] = initial_referee_id

class LoginForm(forms.Form):
    email= forms.EmailField()
    password= forms.CharField(max_length=255)
