from django.db import models
from employers.models import User

class CandidateProfile(models.Model):
    options = (
        ('plustwo', '12th'),
        ('BSc', 'BSc'),
        ('BCA', 'BCA'),
        ('BCom', 'BCom'),
        ('MCA', 'MCA'),
        ('BTech','Btech'),
        ('Mtech','Mtect')

    )
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='candidate')
    qualification=models.CharField(max_length=120,choices=options)
    skills=models.CharField(max_length=150)
    dateofbirth=models.DateField(null=True)
    place=models.CharField(max_length=65)
    profile_pic = models.ImageField(upload_to='cand-profile')
    experience=models.PositiveIntegerField(default=0)
    resume = models.FileField(upload_to='cand-resume', null=True)
