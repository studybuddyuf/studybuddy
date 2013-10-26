from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from profilePage.models import *
from django.core.context_processors import csrf
from django.core.mail import send_mail

def main(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('searchPage.html', c)

def search(request):
	listC = []
	for e in CourseName.objects.all():
		listC.append(e)
	return render_to_response('searchPage.html', {'list': listC})
	
def emailtest(request):
	args = {}
	args.update(csrf(request))
	return render_to_response('emailtest.html', args)

def emailResults(request):
	#currently, only one name value pair is posted. Later this needs
	#to be inside another for loop
	result = StudyBuddyUser.objects.filter(user__id=request.POST['ID'])
	toUser = result[0]
	result = CourseName.objects.filter(courseID=request.POST['Class'])
	clas = result[0]
	fromUser = request.user
	message = 'This is an email from StudyBuddy. '+fromUser.username+' would like to study with you,'
	message = message + ' in the class '+clas.courseID
	message = message + '\n  wow            cool'
	message = message + '\n      such request'
	message = message + '\n so professional        wow'
	message = message + '\n                 wow'
	send_mail(('StudyBuddy Request From '+fromUser.username), message, fromUser.email, ['jacobrabb@gmail.com'], fail_silently = False)
	args = {}
	args.update(csrf(request))
	args['text'] = 'IT WORKED'
	return render_to_response('emailtest.html', args)

		
		
