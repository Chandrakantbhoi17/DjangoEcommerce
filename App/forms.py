
from dataclasses import fields
from xml.parsers.expat import model
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.contrib.auth.models import User

from App import models

""" class UserRegisterForm(UserCreationForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={}))
	username = forms.CharField(label=("Mobile Number/Email"),widget=forms.TextInput(attrs={'oninput':'validate()'}))
	password1 = forms.CharField(label=("Password"), strip=False, widget=forms.PasswordInput(attrs={'oninput':'checkpass1()'}),)
	password2  = forms.CharField(label=("Confirm"), strip=False, widget=forms.PasswordInput(attrs={'oninput':'checkpass2()'}),)
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'password1', 'password2'] """
class ResistraionForm(UserCreationForm):
	username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'oninput':'validate()','class':'form-control'}),error_messages={'required':'Please enter (email or phone number)'},label='Email or phone number')
	password1=forms.CharField(max_length=8,widget=forms.PasswordInput(attrs={'class':'form-control'}),error_messages={'required':'Please enter password'},label='password')
	password2=forms.CharField(max_length=8,widget=forms.PasswordInput(attrs={'class':'form-control'}),error_messages={'required':'Please enter password'},label='Password(confirm)')
	
	class Meta:
		model=User
		fields=['username','password1','password2']
	def __ini__(self,*args,**kwargs):
		self.fields['username'].label=False

		self.fields['password1'].label=False
		self.fields['password2'].label=False
    

class CustomAuthenticationForm(AuthenticationForm):
	username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control mb-2'}),error_messages={'required':'Please enter (email or phone number)'})
	password=forms.CharField(max_length=8,widget=forms.PasswordInput(attrs={'class':'form-control  mb-2'}),error_messages={'required':'Please enter password'},label='Password')
	class Meta:
		model=User
		fields=['username','password']
	def __ini__(self,*args,**kwargs):
		self.fields['username'].label=False
		self.fields['password'].label=False
 

class UserDetailForm(forms.ModelForm):
	class Meta:
		model=models.UserDetail
		fields='__all__'
		exclude=['user']
		
     
