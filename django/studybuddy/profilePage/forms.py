from django import forms
from models import StudyBuddyUser

class UserProfileForm(forms.ModelForm):
	phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Enter your phone number'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder' : 'Enter your email address'}))
	school_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Enter your school name'}))
	year = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'Enter your school year'}))
	about_me = forms.CharField(widget=forms.Textarea(attrs={'class' : 'about_me' , 'placeholder' : 'Enter something about yourself'}))
    	class Meta:
        	model = StudyBuddyUser
        	fields = ['phone', 'email', 'school_name', 'year', 'about_me']

