from django import forms
# from employers.models import Jobs,CompanyProfile
# from django.contrib.auth.models import User
from employers.models import User,Jobs,CompanyProfile
from django.contrib.auth.forms import UserCreationForm



class Jobforms(forms.ModelForm):
    class Meta:
        model = Jobs
        exclude=('company','created_date','active_status')
        widgets={
            'title':forms.TextInput(attrs={'class':' form-control form-control-user','placeholder':'JobTitle'}),
            # 'company':forms.TextInput(attrs={'class':'   form-control form-control-user','placeholder':'CompanyName'}),
            'location':forms.TextInput(attrs={'class':' col-sm-6 form-control form-control-user','placeholder':'Location'}),
            'experience':forms.NumberInput(attrs={'class':'col-sm-6  form-control form-control-user','placeholder':'Experience'}),
            'salary':forms.NumberInput(attrs={'class':'col-sm-6  form-control form-control-user','placeholder':'Salary'}),
            'description':forms.TextInput(attrs={'class':'  form-control form-control-user','placeholder':'Description'}),
            'responsibility': forms.TextInput(attrs={'class': '  form-control form-control-user', 'placeholder': 'Responsibilities'}),
            'qualification': forms.TextInput(attrs={'class': 'col-sm-6   form-control form-control-user', 'placeholder': 'Qualification'}),
            'last_date': forms.DateInput(attrs={'class': 'col-sm-6  form-control form-control-user','type':'date'})
        }


class SignupForm(UserCreationForm):
    # 'password1': forms.PasswordInput(attrs={'class': 'col-sm-6  form-control form-control-user'}),
    # 'password2': forms.PasswordInput(attrs={'class': 'col-sm-6  form-control form-control-user'})
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class': '  form-control form-control-user'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class': '  form-control form-control-user'}))
    class Meta:
        model=User
        fields=['role','first_name','last_name','username','email','phone','password1','password2']
        # exclude=('last_name',)
        widgets={'role':forms.Select(attrs={'class':' form-control '}),
            'first_name':forms.TextInput(attrs={'class':' form-control form-control-user'}),
            'last_name':forms.TextInput(attrs={'class':'  form-control form-control-user',}),
            'username':forms.TextInput(attrs={'class':' form-control form-control-user'}),
            'phone':forms.TextInput(attrs={'class':'  form-control form-control-user'}),
            'email':forms.EmailInput(attrs={'class':' form-control form-control-user'}),


        }

class SigninForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class': ' form-control form-control-user'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user'}))


class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model= CompanyProfile
        exclude = ('user',)
