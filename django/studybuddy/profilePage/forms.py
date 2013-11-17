from django import forms
from django.contrib.auth.models import User
from models import StudyBuddyUser
from django.core.validators import RegexValidator

class UserProfileForm(forms.ModelForm):
	phone = forms.CharField(error_messages={'invalid': "Enter a valid phone number (xxx-xxx-xxxx)"}, required=True, validators=[RegexValidator(regex=r'^\d\d\d-\d\d\d-\d\d\d\d$', code=None)])
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
"""
class PhoneField(MultiValueField):
    def __init__(self, *args, **kwargs):
        error_messages = {
            'incomplete': 'Enter a valid phone number (xxx-xxx-xxxx)',
        }
        fields = (
            CharField(error_messages={'incomplete': 'Enter a valid phone number (xxx-xxx-xxxx)'},
                      validators=[RegexValidator(r'^\d\d\d-\d\d\d-\d\d\d\d$', 'Enter a valid phone number (xxx-xxx-xxxx)')]),
        )
        super(PhoneField, self).__init__(
            self, error_messages=error_messages, fields=fields,
            require_all_fields=True, *args, **kwargs)
"""
