from django import forms
from models import StudyBuddyUser

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = StudyBuddyUser
        fields = {"phone", "school_name", "year"}
