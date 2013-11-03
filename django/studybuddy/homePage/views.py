from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.conf import settings
from django.core.context_processors import csrf
from profilePage.models import *

def main(request):
	#List of Study Buddy requests that a user has received
	list = StudyBuddyRequest.objects.filter(requesteeUserID=request.user, status='2')
	
	args = {}
	args['full_name'] = request.user.username
	args['requestList'] = list
	args.update(csrf(request))

	return render_to_response('homePage.html', args)

def acceptRequest(request):
	requester = StudyBuddyUser.objects.filter(user__username=request.POST['requesterUserID'])
	requestee = StudyBuddyUser.objects.filter(user__username=request.user.username)
	sbRequest = StudyBuddyRequest.objects.filter(requesterUserID=requester[0].user_id, requesteeUserID=requestee[0].user_id, courseID=request.POST['courseID'], semester=settings.CURRENT_SEMESTER)[0]
	sbRequest.status = '4'
	sbRequest.save()

	return main(request)

def rejectRequest(request):
	requester = StudyBuddyUser.objects.filter(user__username=request.POST['requesterUserID'])
	requestee = StudyBuddyUser.objects.filter(user__username=request.user.username)
	sbRequest = StudyBuddyRequest.objects.filter(requesterUserID=requester[0].user_id, requesteeUserID=requestee[0].user_id, courseID=request.POST['courseID'], semester=settings.CURRENT_SEMESTER)[0]
	sbRequest.status = '3'
	sbRequest.save()

	return main(request)
