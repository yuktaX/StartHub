from django.forms import ModelForm,ClearableFileInput
#from .models import Take
from .models import Startup,Teammember
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import modelformset_factory

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
class StartupForm(ModelForm):
    class Meta:
        model=Startup
        fields='__all__'

class SignUpForm(UserCreationForm):
    name=forms.CharField(max_length=100, required=False, help_text='Optional.')
    mob=forms.IntegerField(required=False)
    typee= forms.CharField(max_length=100, required=False, help_text='Optional.')
    dp = forms.FileField(required=False)
   
    class Meta:
        model = User
        fields = ['username', 'name', 'password1', 'password2', 'mob','typee','dp']
        labels = {'mob': 'Mobile Number','username': 'e-Mail ID','typee': 'Account Type','dp':'dp'}
       
"""
TeammemberFormSet = modelformset_factory(
    Teammember, fields=("position", "bio","link","company","image",), extra=1
)

name=models.CharField(max_length=100)
    position=models.CharField(max_length=100, null=True, blank=True)
    bio=models.TextField(null=True, blank=True)
    link=models.URLField(null=True, blank=True)
    company = models.ForeignKey(to=Startup, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', blank=True)

"""
