from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.conf import settings
from django.core.context_processors import csrf
from profilePage.models import *
from schedulePage.views import *
from django.contrib.auth.decorators import login_required

argl = []

@login_required
def main(request):
	#List of Study Buddy requests that a user has received
	list = StudyBuddyRequest.objects.filter(requesteeUserID=request.user, status='2')
	friendsList = StudyBuddyRequest.objects.filter(requesterUserID=request.user, status='4')
	args = {}
	args['full_name'] = request.user.username
	args['requestList'] = list
	args.update(csrf(request))
	args['friends'] = friendsList

	return render_to_response('homePage.html', args)

@login_required
def acceptRequest(request):
	#make the object
	requester = StudyBuddyUser.objects.filter(user__username=request.POST['requesterUserID'])
	requestee = StudyBuddyUser.objects.filter(user__username=request.user.username)
	sbRequest = StudyBuddyRequest.objects.filter(requesterUserID=requester[0].user_id, requesteeUserID=requestee[0].user_id, courseID=request.POST['courseID'], semester=settings.CURRENT_SEMESTER)[0]
	sbRequest.status = '4'
	sbRequest.save()

	#make the reverse object

	newRequest = StudyBuddyRequest()
	newRequest.semester = Semester.objects.filter(semester=settings.CURRENT_SEMESTER)[0]
	newRequest.courseID = CourseName.objects.filter(courseID=request.POST['courseID'])[0]
	newRequest.requesterUserID = requestee[0]
	newRequest.requesteeUserID = requester[0]
	newRequest.status = '4'

	#please ignore the next line of code.
	if str(StudyBuddyRequest.objects.filter(requesterUserID=newRequest.requesterUserID, requesteeUserID=newRequest.requesteeUserID, courseID=newRequest.courseID, semester=newRequest.semester).count) == '<bound method QuerySet.count of []>':	
	#thanks
		newRequest.save()
	else:
		guy = StudyBuddyRequest.objects.filter(requesterUserID=newRequest.requesterUserID, requesteeUserID=newRequest.requesteeUserID, courseID=newRequest.courseID, semester=newRequest.semester)[0]
		guy.status = '4'
		guy.save()

	return main(request)

@login_required
def rejectRequest(request):
	requester = StudyBuddyUser.objects.filter(user__username=request.POST['requesterUserID'])
	requestee = StudyBuddyUser.objects.filter(user__username=request.user.username)
	sbRequest = StudyBuddyRequest.objects.filter(requesterUserID=requester[0].user_id, requesteeUserID=requestee[0].user_id, courseID=request.POST['courseID'], semester=settings.CURRENT_SEMESTER)[0]
	sbRequest.status = '3'
	sbRequest.save()

	return main(request)

@login_required
def viewProfile(request):
	user = StudyBuddyUser.objects.filter(user__username=request.GET['userID'])[0]
	args = {}
	args['user'] = user
	args['full_name'] = user.user.username
	args['scheduleItems'] = courseInfoUser(user.user.username)

	return render_to_response('viewProfile.html', args)
