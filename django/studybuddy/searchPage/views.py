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
	args = {}
	args.update(csrf(request))
	args['list'] = listC
	return render_to_response('searchPage.html', args)
	
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

def doSearch(request):
	#initialize lists
	testing = []
	resultsList = []
	
	#multiplex based on the radio button
	if(request.POST['searchtype']=='course'):
		#the user is searching by course, get the relevant proprties from the post
		courseName = request.POST['Class']
		#semester is hardcoded, replace later with a function which generates the current semester
		semester = "Fall 2013"

		#get the relevant course sections
		courseSectionList = CourseSection.objects.filter(courseID = courseName).filter(semester = semester)

		#get the users who are in those courses
		userScheduleList = []
		for coursen in courseSectionList:
			item = UserSchedule.objects.filter(scheduleID = coursen.regularScheduleID)
			for us in item:
				#and ARENT the user who is making the request (vanwirer)
				if(request.user.id != us.userID.id):
					userScheduleList.append(us)

		#now, populate the return list
		for user in userScheduleList:
			tup = []
			#first, we statically append the course name, as we are searching for only one course
			tup.append(courseName)

			#next, we append the user we are interested in
			tup.append(user.userID)

			#finally, we append their status. If there is no status, make it 1, the default
			item = StudyBuddyRequest.objects.filter(semester = semester).filter(courseID = courseName).filter(requesterUserID = request.user.id).filter(requesteeUserID = user.userID.id)
			if(item):
				tup.append(item[0].status)
			else:
				tup.append("1")

			#and append that tuple to the results
			resultsList.append(tup)

	#this code is if the user is searching based on name
	elif(request.POST['searchtype']=='name'):

		#first get the relevant information from the post
		firstName = request.POST['FirstName']
		lastName = request.POST['LastName']

		semester = "Fall 2013"

		#go ahead and get a list of the current user (vanwirer) courses.
		#this will come in handy later

		thisUserCourseList = []
		list1 = UserSchedule.objects.filter(userID=request.user) 
		for item in list1:
			list2 = CourseSection.objects.filter(regularScheduleID=item.scheduleID)
			for item2 in list2:
				thisUserCourseList.append(item2)



		#next, get all of the studybuddy users which have that name
		#this can be more than one user!
		sbusersList1 = StudyBuddyUser.objects.filter(user__last_name=lastName).filter(user__first_name=firstName)

		#filter out the current user (vanwirer). This is probably not required but it makes some later parts behavior more predictable
		sbusersList = []
		for e in sbusersList1:
			if(e.user!=request.user):
				sbusersList.append(e)

		#now, begin populating the results list
		for e in sbusersList:
			#first, get the schedule objects with that match one particular user
			userScheduleList = UserSchedule.objects.filter(userID=e)
			courseSectionList = []
			#now, filter those so that you only get ones which are courses
			for item in userScheduleList:
				courses = CourseSection.objects.filter(regularScheduleID=item.scheduleID)
				for item2 in courses:
					#further filter so that we only get courses which the requester is is in
					if(item2 in thisUserCourseList):
						courseSectionList.append(item2)
			#now, for each course, we need to build a tuple.
			for item in courseSectionList:
				tup = []
				#course id goes in the tuple first, that's easy.
				tup.append(item.courseID)
				#next comes the user object, that's also easy.
				tup.append(e)
				#next comes the tricky part, we need to get the status of their outstanding request
				item2 = StudyBuddyRequest.objects.filter(semester = semester).filter(courseID = item.courseID).filter(requesterUserID= request.user.id).filter(requesteeUserID= e.user.id)
				if(item2):
					tup.append(item2[0].status)
				else:
					tup.append("1")
				resultsList.append(tup)

		
	
	#you shouldn't be able to get here without picking a radio, but if you do, it will 
	#just return two blank lists, no big deal. Same as if it found no results
	args = {}
	args['resultsList'] = resultsList
	args['test'] = testing
	return render_to_response('resultsTest.html', args)
	