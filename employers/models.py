from django.db import models
from django.contrib.auth.models import User

class Jobs(models.Model):
    title=models.CharField(max_length=100)
    companyname=models.CharField(max_length=100)
    location=models.CharField(max_length=55)
    experience=models.PositiveIntegerField(default=0)
    salary=models.PositiveIntegerField(null=True)



class CompanyProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True, related_name='employer')
    company_name=models.CharField(max_length=100)
    logo=models.ImageField(upload_to='companyprofile', null=True)
    services=models.CharField(max_length=150)
    location=models.CharField(max_length=100)
    description=models.CharField(max_length=200)




# Create your models here.
