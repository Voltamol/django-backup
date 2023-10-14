from django.db import models

class Candidate(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=255)

class Referee(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    comp_name = models.CharField(max_length=255)
    referee_name = models.CharField(max_length=255)
    company_email = models.EmailField()
    company_telephone = models.CharField(max_length=20)

class Candidate_Documents(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    cv = models.FileField(upload_to='cv/')
    photo = models.ImageField(upload_to='photos/')

class Referee_Questionnaire(models.Model):
    referee = models.ForeignKey(Referee, on_delete=models.CASCADE)
    problem_solving = models.IntegerField()
    communication_skills = models.IntegerField()
    time_management = models.IntegerField()
    creativity = models.IntegerField()
    willingness_to_learn = models.IntegerField()
    team_work = models.IntegerField()
    reliability = models.IntegerField()
    opinion = models.CharField(max_length=200)

class Progress_Tracker(models.Model):
    candidate = models.ForeignKey(Candidate_Documents, on_delete=models.CASCADE)
    referee = models.ForeignKey(Referee, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)