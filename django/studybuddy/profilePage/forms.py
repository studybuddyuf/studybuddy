from django import forms
from models import StudyBuddyUser

class UserProfileForm(forms.ModelForm):
	email = forms.EmailField()
	about_me = forms.CharField(widget=forms.Textarea(attrs={'class' : 'about_me'}))
    	class Meta:
        	model = StudyBuddyUser
        	fields = ['phone', 'email', 'school_name', 'year', 'about_me']

