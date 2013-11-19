from django import forms
from profilePage.models import *
from django.core.exceptions import ObjectDoesNotExist

class scheduleForm(forms.Form):
    items = forms.ModelChoiceField(queryset=StudyBuddyUser.objects.all())
