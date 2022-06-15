from django import forms
from candidate.models import CandidateProfile
# from employers.models import User


class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model = CandidateProfile
        exclude = ('user',)

        widgets={
            'qualification':forms.Select(attrs={'class':'form-control form-select','placeholder':'Qualification'}),
            'skills': forms.TextInput(attrs={'class': 'form-control','placeholder':'MySkills'}),
            'dateofbirth': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Dateofbirth','type':'date'}),
            'experience':forms.NumberInput(attrs={'class': 'form-control ','placeholder':'Experience'}),
            'place':forms.TextInput(attrs={'class': 'form-control ','placeholder':'Place'}),
            'profile_pic':forms.FileInput(attrs={'class':'form-control ','placeholder':'ProfileImage'}),
            'resume': forms.FileInput(attrs={'class': 'form-control ','placeholder':'Resume'})

        }

class CandidateProfileEditForm(forms.ModelForm):

    first_name=forms.CharField()
    last_name=forms.CharField()
    phone=forms.CharField()
    email=forms.EmailField()
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'FirstName'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'LastName'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

    class Meta:
        model=CandidateProfile
        fields=['first_name',
                'last_name',
                'email',
                'phone',
                'qualification',
                'skills',
                'dateofbirth',
                'experience',
                'place',
                'profile_pic',
                'resume']
        widgets = {
            'qualification': forms.Select(attrs={'class': 'form-control form-select', 'placeholder': 'Qualification'}),
            'skills': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'MySkills'}),
            'dateofbirth': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Dateofbirth', 'type': 'date'}),
            'experience': forms.NumberInput(attrs={'class': 'form-control ', 'placeholder': 'Experience'}),
            'place': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Place'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control ', 'placeholder': 'ProfileImage'}),
            'resume': forms.FileInput(attrs={'class': 'form-control ', 'placeholder': 'Resume'})

        }