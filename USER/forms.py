from dataclasses import fields

from USER.models import Profile
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class createform(UserCreationForm):
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        
        
class editform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name' ,'email']
class updateProfile(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image','bio','about']
class dflt(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image','bio','about']
    