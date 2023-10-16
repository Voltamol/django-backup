from django.db import models
import os
class Candidate(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.firstname
    
class SystemAdmin(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=255)

class Referee(models.Model):
    comp_name = models.CharField(max_length=255)
    referee_name = models.CharField(max_length=255)
    company_email = models.EmailField()
    company_telephone = models.CharField(max_length=20)

    def __str__(self):
        return self.referee_name

def cv_upload_path(instance, filename):
    # Upload the CV file to the 'cv' subfolder
    return os.path.join('cv', filename)

def photo_upload_path(instance, filename):
    # Upload the photo file to the 'photos' subfolder
    return os.path.join('photos', filename)


class Candidate_Documents(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    cv = models.FileField(upload_to=cv_upload_path)
    photo = models.ImageField(upload_to=photo_upload_path)

    def truncate_filename(self, filename):
        try:
            filename=os.path.basename(filename)
            filename,extension=filename.split('.')
        except Exception:
            filename=os.path.basename(filename)
            extension="."
        else:
            extension_length=len(extension)
            filename=filename[:10-extension_length]
        finally:
            filename="".join([filename,'..',extension])
            return filename
        
    @property
    def cv_basename(self):
        return os.path.basename(self.cv.url)
    
    @property
    def cv_truncated_basename(self):
        return self.truncate_filename(self.cv.url)
    
    @property
    def photo_basename(self):
        return os.path.basename(self.photo.url)
    
    @property
    def photo_truncated_basename(self):
        return self.truncate_filename(self.photo.url)

class Referee_Questionnaire(models.Model):
    candidate=models.ForeignKey(Candidate, on_delete=models.CASCADE,default='')
    referee = models.ForeignKey(Referee, on_delete=models.CASCADE)
    problem_solving = models.IntegerField()
    communication_skills = models.IntegerField()
    time_management = models.IntegerField()
    creativity = models.IntegerField()
    willingness_to_learn = models.IntegerField()
    team_work = models.IntegerField()
    reliability = models.IntegerField()
    opinion = models.CharField(max_length=200)

class Verification(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    referee = models.ForeignKey(Referee, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)

class Progress_Tracker(models.Model):
    candidate = models.ForeignKey(Candidate_Documents, on_delete=models.CASCADE)
    referee = models.ForeignKey(Referee, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)