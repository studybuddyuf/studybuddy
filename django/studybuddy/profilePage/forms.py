from django import forms
from django.contrib.auth.models import User
from models import StudyBuddyUser

class UserProfileForm(forms.ModelForm):
	phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Enter your phone number'}))
	school_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Enter your school name'}))
	year = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Enter your school year'}))
	about_me = forms.CharField(widget=forms.Textarea(attrs={'class' : 'about_me' , 'placeholder' : 'Enter something about yourself'}))
    	class Meta:
			model = StudyBuddyUser
			fields = ['phone', 'school_name', 'year', 'about_me']

class UserEmailForm(forms.ModelForm):
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder' : 'Enter your email address'}))
    	class Meta:
			model = User
			fields = ['email']
