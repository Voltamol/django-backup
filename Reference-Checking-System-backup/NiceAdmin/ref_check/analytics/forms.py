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
        widgets={
            'candidate': forms.Select(attrs={'class': 'form-control'}),
            'comp_name': forms.TextInput(attrs={'class': 'form-control'}), 
            'referee_name': forms.TextInput(attrs={'class': 'form-control'}),
            'company_email': forms.EmailInput(attrs={'class': 'form-control'}), 
            'company_telephone':forms.TextInput(attrs={'class': 'form-control'})
        }

# class RefereeBasicForm(forms.Form):
#     candidate = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=[])  # Replace choices with actual choices
#     comp_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     referee_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     company_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
#     company_telephone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

#     def __init__(self, *args, **kwargs):
#         super(RefereeForm, self).__init__(*args, **kwargs)
#         self.fields['candidate'].choices = [(candidate.id, candidate.name) for candidate in Referee.objects.all()]

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

class LoginForm(forms.Form):
    email= forms.EmailField()
    password= forms.CharField(max_length=255)
