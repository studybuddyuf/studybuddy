from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from profilePage.models import *
from django.core.context_processors import csrf
from django.core.mail import send_mail
from django.conf import settings

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

#Debugging and Testing code
def searchResultTest(request):
	args = {}
	#classes = request.POST.getlist('class[]')
	args['classes'] = request.POST.getlist('class[]')
	#if len(classes) > 0:
	#	args['first'] = classes[0]
	#if len(classes) > 1:
	#	args['second'] = classes[1]
	return render_to_response('searchResultTest.html', args)
	
def emailtest(request):
	args = {}
	args.update(csrf(request))
	return render_to_response('emailtest.html', args)

def emailResults(request):
	results = request.POST.getlist('class[]')
	messages = []
	test = []
	for i in results:
		#split the string we get
		longword = i.split()

		#make some db 'quarries'
		clas = "lol"
		toUser = "lol"
		result = StudyBuddyUser.objects.filter(user__username=longword[1])
		if result:
			toUser = result[0]
		else:
			test.append(i)
			test.append(i.split())
		result = CourseName.objects.filter(courseID=longword[0])
		if result:
			clas = result[0]

		fromUser = request.user

		if(clas!="lol" and toUser!="lol"):
			#now that we know what we are doing, we need to
			#generate the message and also alert studybuddy of our intentions
			message = 'This is an email from StudyBuddy. '+fromUser.username+' would like to study with you,'
			message = message + ' in the class '+clas.courseID
			message = message + '\n  wow            cool'
			message = message + '\n      such request'
			message = message + '\n so professional        wow'
			message = message + '\n                 wow'

			#this line currently not working, perhaps next sprint
			#send_mail(('StudyBuddy Request From '+fromUser.username), message, fromUser.email, ['jacobrabb@gmail.com'], fail_silently = False)

			messages.append(message)

			#make studybuddy aware of the request
			newrequest = StudyBuddyRequest()
			newrequest.status = 2
			#hardcoded
			newrequest.semester = Semester.objects.filter(semester=settings.CURRENT_SEMESTER)[0]
			newrequest.courseID = CourseName.objects.filter(courseID=clas.courseID)[0]
			newrequest.requesterUserID = StudyBuddyUser.objects.filter(user=fromUser)[0]
			newrequest.requesteeUserID = StudyBuddyUser.objects.filter(user=toUser.user)[0]

			#please ignore the next line of code.
			if str(StudyBuddyRequest.objects.filter(requesterUserID=newrequest.requesterUserID, requesteeUserID=newrequest.requesteeUserID, courseID=newrequest.courseID, semester=newrequest.semester).count) == '<bound method QuerySet.count of []>':	
			#thanks
				newrequest.save()
			else:
				guy = StudyBuddyRequest.objects.filter(requesterUserID=newrequest.requesterUserID, requesteeUserID=newrequest.requesteeUserID, courseID=newrequest.courseID, semester=newrequest.semester)[0]
				guy.status = 2
				guy.save()



	args = {}
	args.update(csrf(request))
	args['messages'] = messages
	args['test'] = test
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
		semester = settings.CURRENT_SEMESTER

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
			string = tup[0]+' '+str(tup[1])
			tup.append(string)
			#and append that tuple to the results
			resultsList.append(tup)

		#filter our results if the box is checked
		if request.POST.get('hourMatch') == 'true':
			resultsList = filter(request, resultsList) #later add a second paremeter based on hours needed
				

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
				string = str(tup[0])+' '+str(tup[1])
				tup.append(string)
				resultsList.append(tup)

		
	
	#you shouldn't be able to get here without picking a radio, but if you do, it will 
	#just return two blank lists, no big deal. Same as if it found no results
	args = {}
	args['resultsList'] = resultsList
	args['test'] = testing
	args.update(csrf(request))
	return render_to_response('searchResult.html', args)


def filter (request, resultsList):
	vanwirer = timeArray(request.user)
	returnList = []	
	for result in resultsList:	
		if match(result[1], vanwirer):
			returnList.append(result)
	return returnList


def match (candidate, currentFree):
	counter = 0
	candidateFree = timeArray(candidate)	
	for day in my_range(0, 6, 1):
		for fiveMinute in my_range(0, (settings.SLEEP_HOUR*12-settings.AWAKE_HOUR*12-1), 1):
			if(candidateFree[day][fiveMinute] and currentFree[day][fiveMinute]):
				counter += 1
				if counter == 1*12: #The 1 is the number of hours the user wants to match.
					return True
			else:
				counter = 0
		counter = 0
	return False 

#takes a user and makes a free list of their free time
def timeArray(user):
	daySlots = []	
	#constants will be defined in settings file later
	startTime = settings.AWAKE_HOUR*60
	endTime = settings.SLEEP_HOUR*60
	stepSize = settings.GRANULARITY 
	#make the empty list (all free)
	for j in my_range(0, 6, 1):
		timeSlots = []
		for i in my_range(startTime,endTime, stepSize):
			timeSlots.append(True)
		daySlots.append(timeSlots)

	#get a list of the user's time blocks	
	#get the studybuddyuser from the auth_user
	studybuddyuser = StudyBuddyUser.objects.filter(user=user)[0]

	#get the userschedules from the studybuddyuser
	userSchedules = UserSchedule.objects.filter(userID=studybuddyuser)

	#get a list of the schedule objects
	scheduleObjects = []
	for userschedule in userSchedules:
		scheduleObjects.append(userschedule.scheduleID)

	#now, iterate through this list	
	for scheduleobj in scheduleObjects:
		if(scheduleobj.mondayStart):
			fillOut(scheduleobj.mondayStart, scheduleobj.mondayEnd, 0, daySlots)
		if(scheduleobj.tuesdayStart):
			fillOut(scheduleobj.tuesdayStart, scheduleobj.tuesdayEnd, 1, daySlots)
		if(scheduleobj.wednesdayStart):
			fillOut(scheduleobj.wednesdayStart, scheduleobj.wednesdayEnd, 2, daySlots)
		if(scheduleobj.thursdayStart):
			fillOut(scheduleobj.thursdayStart, scheduleobj.thursdayEnd, 3, daySlots)
		if(scheduleobj.fridayStart):
			fillOut(scheduleobj.fridayStart, scheduleobj.fridayEnd, 4, daySlots)
		if(scheduleobj.saturdayStart):
			fillOut(scheduleobj.saturdayStart, scheduleobj.saturdayEnd, 5, daySlots)
		if(scheduleobj.sundayStart):
			fillOut(scheduleobj.sundayStart, scheduleobj.sundayEnd, 6, daySlots)

	return daySlots

#void method that fills out an array based on a certain day
def fillOut(startTime, endTime, day, daySlots):
	start = startTime.hour*12
	start = start + startTime.minute/5
	end = endTime.hour*12 + endTime.minute/5
	if start < settings.AWAKE_HOUR*12:
		start = settings.AWAKE_HOUR*12
	if end >= settings.SLEEP_HOUR*12:
		end = settings.SLEEP_HOUR*12-1
	for i in my_range(0, end-start, 1):
		daySlots[day][i] = False

#helper method for python's for loops
def my_range(start, end, step):
	while start <= end:
		yield start
		start+=step
