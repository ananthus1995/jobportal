from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    options=(
            ('employer', 'employer'),
            ('candidate', 'candidate')
    )
    role=models.CharField(max_length=120,choices=options,default='candidate')
    phone=models.CharField(max_length=20,null=True)




class Jobs(models.Model):
    title=models.CharField(max_length=55)
    company=models.ForeignKey(User,on_delete=models.CASCADE,related_name='company')
    location=models.CharField(max_length=55)
    experience=models.PositiveIntegerField(default=0)
    salary=models.PositiveIntegerField(null=True)
    description=models.CharField(null=True,max_length=200)
    responsibility=models.CharField(max_length=200)
    qualification=models.CharField(max_length=200)
    created_date=models.DateField(auto_now_add=True)
    last_date=models.DateField(null=True)
    active_status=models.BooleanField(default=True)



class CompanyProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, related_name='employer')
    company_name=models.CharField(max_length=100)
    logo=models.ImageField(upload_to='companyprofile', null=True)
    services=models.CharField(max_length=150)
    location=models.CharField(max_length=100)
    description=models.CharField(max_length=200)


class Applications(models.Model):
    applicant=models.ForeignKey(User,on_delete=models.CASCADE,related_name='applicant')
    job=models.ForeignKey(Jobs,on_delete=models.CASCADE)
    options=(
        ('applied','applied'),
        ('accepted','accepted'),
        ('rejected','rejected'),
        ('pending','pending'),
        ('cancelled','cancelled')
    )
    status=models.CharField(max_length=20,choices=options,default='applied')
    date=models.DateField(auto_now_add=True)
    class Meta:
        unique_together=('applicant','job')

# Create your models here.
