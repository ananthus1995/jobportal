from django import forms
from employers.models import Jobs,CompanyProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class Jobforms(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = '__all__'
        widgets={
            'title':forms.TextInput(attrs={'class':' form-control form-control-user','placeholder':'JobTitle'}),
            'companyname':forms.TextInput(attrs={'class':'   form-control form-control-user','placeholder':'CompanyName'}),
            'location':forms.TextInput(attrs={'class':' col-sm-6 form-control form-control-user','placeholder':'Location'}),
            'experience':forms.NumberInput(attrs={'class':'col-sm-6  form-control form-control-user','placeholder':'Experience'}),
            'salary':forms.NumberInput(attrs={'class':'col-sm-6  form-control form-control-user','placeholder':'Salary'})
        }

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']
        widgets={'first_name':forms.TextInput(attrs={'class':'col-sm-6 form-control form-control-user'}),
            'last_name':forms.TextInput(attrs={'class':'col-sm-6   form-control form-control-user',}),
            'username':forms.TextInput(attrs={'class':' col-sm-6 form-control form-control-user'}),
            'email':forms.EmailInput(attrs={'class':' form-control form-control-user'}),
            'password1':forms.PasswordInput(attrs={'class':'col-sm-6  form-control form-control-user'}),
            'password2': forms.PasswordInput(attrs={'class': 'col-sm-6  form-control form-control-user'})

        }

class SigninForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput())
    widgets = {'username': forms.TextInput(attrs={'class': 'col-sm-6 form-control form-control-user'}),
               'password': forms.TextInput(attrs={'class': 'col-sm-6   form-control form-control-user' })

               }

class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model= CompanyProfile
        exclude = ['user']
