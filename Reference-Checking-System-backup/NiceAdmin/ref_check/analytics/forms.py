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
            'cv': forms.FileInput(attrs={'class': 'form-control','accept':".pdf, .doc, .docx, .pptx"}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control','accept':".jpg, .jpeg, .png"})
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


class RefereeSubfieldsForm(forms.Form):
    comp_name = forms.CharField(max_length=255)
    referee_name = forms.CharField(max_length=255)
    company_email = forms.EmailField()
    company_telephone = forms.CharField(max_length=20)

class RefereeHierarchicalForm(forms.ModelForm):
    subfields=RefereeSubfieldsForm()
    class Meta:
        model=Candidate
        fields=['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def __init__(self,*args,**kwargs):
        self.fields['subfields'].widget = forms.MultiWidget(widgets=[
            forms.TextInput(attrs={'class': 'form-control'}),
            forms.TextInput(attrs={'class': 'form-control'}),
            forms.EmailInput(attrs={'class':'form-control'}), 
            forms.TextInput(attrs={'class': 'form-control'}),
        ])

        self.fields['subfields'].fields[0] = self.fields['subfields'].fields['comp_name']
        self.fields['subfields'].fields[1] = self.fields['subfields'].fields['referee_name']
        self.fields['subfields'].fields[2] = self.fields['subfields'].fields['company_email']
        self.fields['subfields'].fields[3] = self.fields['subfields'].fields['company_telephone']

    def decompress(self, value):
        if value:
            return [
                value['subfields']['comp_name'],
                value['subfields']['referee_name'], 
                value['subfields']['company_email'], 
                value['subfields']['company_telephone']
            ]
        
        return [None, None, None, None]

    def compress(self, data_list):
        return {
            'subfields': {
                'comp_name': data_list[0],
                'referee_name': data_list[1],
                'company_email': data_list[2],
                'company_telephone': data_list[3]
            }
        }
