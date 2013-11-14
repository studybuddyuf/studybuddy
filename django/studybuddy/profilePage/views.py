from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from forms import UserProfileForm
from forms import UserEmailForm
from profilePage.models import *
from django.contrib.auth.decorators import login_required

@login_required
def update_profile(request):
    if request.method == 'POST':
        form1 = UserEmailForm(request.POST, instance=request.user)
        form2 = UserProfileForm(request.POST, instance=request.user.profile)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return HttpResponseRedirect('/profile')
    else:
        user = request.user
        profile = user.profile
        form1 = UserEmailForm(instance=user)
        form2 = UserProfileForm(instance=profile)

    args = {}
    args.update(csrf(request))

    args['form1'] = form1
    args['form2'] = form2


    return render_to_response('editProfilePage.html', args)
	
def profile(request):
    return render_to_response('profilePage.html', {'full_name': request.user.username, 'phone': getPhone(request.user), 'schoolname': getSchoolName(request.user), 'year': getYear(request.user), 'aboutme': aboutMe(request.user), 'email': getEmail(request.user)})	

def getPhone(un):
	return StudyBuddyUser.objects.filter(user = un)[0].phone
	
def getSchoolName(un):
	return StudyBuddyUser.objects.filter(user = un)[0].school_name

def getYear(un):
	return StudyBuddyUser.objects.filter(user = un)[0].year

def aboutMe(un):
		return StudyBuddyUser.objects.filter(user = un)[0].about_me
		
def getEmail(un):
		return un.email