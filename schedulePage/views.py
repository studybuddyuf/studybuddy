from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from profilePage.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.core.context_processors import csrf
from django.conf import settings
from django.contrib.auth.decorators import login_required
import datetime
import time

@login_required
def main(request):
    return render_to_response('schedulePage.html', {'full_name': request.user.username, 'scheduleItems': courseInfoUser(request.user.username)})

@login_required
def edit(request):
	args = {}
	args['full_name'] = request.user.username
	args['scheduleItems'] = courseListUser(request.user.id)
	args['sectionNumbers'] = sectionObjects(request.user.id)
	test = []
	args['personalItems'] = getPersonal(request.user.id, test)
	args['test'] = test
	args.update(csrf(request))
	return render_to_response('editSchedulePage.html', args)

@login_required
def addClass(request):
	# We have a user ID (via request.user.id), the current semester (via CURRENT_SEMESTER), a course name,
	# and a section number
	# First, get the course ID based on the course name we received
	# Next, get the regular/discussion schedule IDs for the given course ID, semester, and section number
	# Finally, insert the regular/discussion schedule IDs

	# Dictionary to hold various items
	args = {}

	# Extract course name and section number from posted item
	courseName = request.POST['sectionItem'].split(" (section ")[0]
	sectionNumber = request.POST['sectionItem'].split(" (section ")[1].split(")")[0]

	# Get the course ID
	course = CourseName.objects.filter(courseName = courseName)
	courseID = course[0].courseID

	# Get the regular/discussion schedule IDs
	courseSection = CourseSection.objects.filter(courseID = courseID, semester = settings.CURRENT_SEMESTER, sectionNumber = sectionNumber)[0]

	# Need an instance of a StudyBuddyUser
	studyBuddyUser = StudyBuddyUser.objects.filter(user_id = request.user.id)[0]

	# Insert the regular schedule ID
	UserSchedule.objects.create(userID = studyBuddyUser, scheduleID = courseSection.regularScheduleID)

	# Insert the discussion schedule ID, if any
	if courseSection.discussionScheduleID is not None:
		UserSchedule.objects.create(userID = studyBuddyUser, scheduleID = courseSection.discussionScheduleID)

	# Return
	return edit(request)

@login_required
def addPersonal(request):
	scheduleItem = Schedule()	
	beginhour = int(request.POST['beginhour'])
	beginminute = int(request.POST['beginminute'])
	if(request.POST['beginampm']=='PM'):
		beginhour = beginhour+12
	endhour = int(request.POST['endhour'])
	endminute = int(request.POST['endminute'])
	if(request.POST['endampm']=='PM'):
		endhour = endhour+12
	
	begin = datetime.time(beginhour, beginminute)
	end = datetime.time(endhour, endminute)
	
	if request.POST.get('monday') =='True':
		scheduleItem.mondayStart = begin
		scheduleItem.mondayEnd = end
	if request.POST.get('tuesday') =='True':
		scheduleItem.tuesdayStart = begin
		scheduleItem.tuesdayEnd = end
	if request.POST.get('wednesday') =='True':
		scheduleItem.wednesdayStart = begin
		scheduleItem.wednesdayEnd = end
	if request.POST.get('thursday') =='True':
		scheduleItem.thursdayStart = begin
		scheduleItem.thursdayEnd = end
	if request.POST.get('friday') =='True':
		scheduleItem.fridayStart = begin
		scheduleItem.fridayEnd = end
	if request.POST.get('saturday') =='True':
		scheduleItem.saturdayStart = begin
		scheduleItem.saturdayEnd = end
	if request.POST.get('sunday') =='True':
		scheduleItem.sundayStart = begin
		scheduleItem.sundayEnd = end

	scheduleItem.save()

	userScheduleItem = UserSchedule()
	userScheduleItem.userID = StudyBuddyUser.objects.filter(user=request.user.id)[0]
	userScheduleItem.scheduleID = Schedule.objects.filter(scheduleID=scheduleItem.scheduleID)[0]

	userScheduleItem.save()

	return edit(request)

@login_required
def removeClass(request):
	# We have a user ID (via request.user.id), the current semester (via CURRENT_SEMESTER), and a course name
	# First, get the course ID based on the course name we received
	# Next, get all of the schedule IDs for the given course ID and semester
	# Finally, remove all rows from user schedule which have our current user ID plus the semester IDs we just got

	# Get the course ID
	course = CourseName.objects.filter(courseName = request.POST['scheduleItem'])
	courseID = course[0].courseID

	# Get the sections for this course
	courseSectionList = CourseSection.objects.filter(courseID = courseID, semester = settings.CURRENT_SEMESTER)

	# Get the schedule IDs for these courses
	scheduleIDList = []
	for courseSection in courseSectionList:
		# Add the regular schedule ID
		scheduleIDList.append(courseSection.regularScheduleID.scheduleID)

		# Add the discussion schedule ID, if it exists
		if courseSection.discussionScheduleID is not None:
			scheduleIDList.append(courseSection.discussionScheduleID.scheduleID)

	# Remove the user schedule rows
	for scheduleID in scheduleIDList:
		UserSchedule.objects.filter(userID = request.user.id, scheduleID = scheduleID).delete()

	# Return
	return edit(request)

@login_required
def removePersonal(request):
	personalSchedule = Schedule.objects.filter(scheduleID=request.POST['personalItem'])[0]
	personalUserSchedule = UserSchedule.objects.filter(scheduleID=personalSchedule)[0]	
	personalSchedule.delete()
	personalUserSchedule.delete()
	return edit(request)

def sectionObjects(userid):
	sectionList = CourseSection.objects.all()
	courseList = CourseName.objects.all()
	enrolledCourseList = courseListUser(userid)
	newList = []
	for e in sectionList :
		for i in courseList:
			if e.courseID.courseID == i.courseID and i.courseName not in enrolledCourseList:
				newList.append(i.courseName + " (section " + str(e.sectionNumber) + ")")
	return newList

def courseInfoUser(un):
  list = []
  for e in scheduleListUser(un):
    list.append(scheduleTime(e.scheduleID.scheduleID))
  return list

def scheduleListUser(un):
  return UserSchedule.objects.filter(userID__user__username=un)
  
def courseListUser(userID):
  userScheduleList = UserSchedule.objects.filter(userID=userID)
  courseSectionList = []
  for schedule in userScheduleList:
    schedule = CourseSection.objects.filter(regularScheduleID=schedule.scheduleID)
    if schedule:
      courseSectionList.append(schedule)
  courseNameList = []
  for course in courseSectionList:
    for e in course:
      courseNameList.append(CourseName.objects.filter(courseID=e.courseID))
  justNameList = []
  for course in courseNameList:
    for att in course:
      justNameList.append(att.courseName)
  return justNameList

#returns a String list if times on a given day exist.
#for example if a course was Monday 9 to 10
#this method would reutrn a list containing the following
#Monday , 9:00:00 , 10:00:00
#im not sure how to trim the seconds off of the dateTime yet. working on it.
def allTimesItem(scheduleID):
  list = []
  schedule = Schedule.objects.get(scheduleID=scheduleID)
  if schedule:
	list.append('Monday')
 	list.append('Tuesday')
	list.append('Wednesday')
	list.append('Thursday')
	list.append('Friday')
	list.append('Saturday')
	list.append('Sunday')
	list.append(str(schedule.mondayStart))
	list.append(str(schedule.tuesdayStart))
	list.append(str(schedule.wednesdayStart))
	list.append(str(schedule.thursdayStart))
	list.append(str(schedule.fridayStart))
	list.append(str(schedule.saturdayStart))
	list.append(str(schedule.sundayStart))

    	list.append(str(schedule.mondayEnd))
   	list.append(str(schedule.tuesdayEnd))    
    	list.append(str(schedule.wednesdayEnd))   
    	list.append(str(schedule.thursdayEnd))   
    	list.append(str(schedule.fridayEnd))
	list.append(str(schedule.saturdayEnd))
 	list.append(str(schedule.sundayEnd))
  return list



#returns a String list of times given scheduleID and day
#example. scheduleID=1 mondayStart=9:00:00 mondayEnd=10:00:00
#timesItemDay(1,'Monday') returns the following list:
#['9:00:00','10:00:00']
def timesItemDay(scheduleID, day):
  list = []
  schedule = Schedule.objects.get(scheduleID=scheduleID)
  if day == 'Monday':
    if schedule.mondayStart:
      list.append(str(schedule.mondayStart))
      list.append(str(schedule.mondayEnd))
  if day == 'Tuesday':
    if schedule.tuesdayStart:
      list.append(str(schedule.tuesdayStart))
      list.append(str(schedule.tuesdayEnd))
  if day == 'Wednesday':
    if schedule.wednesdayStart:
      list.append(str(schedule.wednesdayStart))
      list.append(str(schedule.wednesdayEnd))
  if day == 'Thursday':
    if schedule.thursdayStart:
      list.append(str(schedule.thursdayStart))
      list.append(str(schedule.thursdayEnd))
  if day == 'Friday':
    if schedule.fridayStart:
      list.append(str(schedule.fridayStart))
      list.append(str(schedule.fridayEnd))
  if day == 'Saturday':    
    if schedule.saturdayStart:
      list.append(str(schedule.saturdayStart))
      list.append(str(schedule.saturdayEnd))
  if day == 'Sunday':
    if schedule.sundayStart:
      list.append(str(schedule.sundayStart))
      list.append(str(schedule.sundayEnd))
  return list

def scheduleTime(scheduleID):
  list = []
  #print 'This is debug output: '+ str(scheduleID)
  try: #check if Id is a regular
    course = CourseSection.objects.get(regularScheduleID=scheduleID)
    reg = True
  except CourseSection.DoesNotExist:
    try:
      reg = False
      course = CourseSection.objects.get(discussionScheduleID=scheduleID)
    except CourseSection.DoesNotExist:
	  return list 
  if reg:
    list.append('Lecture')
  else:
    list.append('Discussion')
  list.append('Course Name: '+ str(course.courseID))
  list.append('Semester: '+ str(course.semester))
  list.append('Section: '+ str(course.sectionNumber))
  listAll = allTimesItem(scheduleID)
  for e in listAll:
    list.append(e)
  return list
 
#kind of like the method above
def getPersonal(un, test):
	scheduleItems = UserSchedule.objects.filter(userID=un)
	personal = []
	for item in scheduleItems:
		try:
			CourseSection.objects.get(regularScheduleID=item.scheduleID)
		except CourseSection.DoesNotExist:
			try:
				CourseSection.objects.get(discussionScheduleID=item.scheduleID)
			except CourseSection.DoesNotExist:
				tup = []
				tup.append(str(item.scheduleID.scheduleID))
				tup.append(lookGood(item.scheduleID))	
				personal.append(tup)	
	return personal

def lookGood(item):
	return_string = ""
	if(item.mondayStart):
		return_string += "M: "
		return_string += str(item.mondayStart)
		return_string += " to "
		return_string += str(item.mondayEnd)
		return_string += " "
	if(item.tuesdayStart):
		return_string += "T: "
		return_string += str(item.tuesdayStart)
		return_string += " to "
		return_string += str(item.tuesdayEnd)
		return_string += " "
	if(item.wednesdayStart):
		return_string += "W: "
		return_string += str(item.wednesdayStart)
		return_string += " to "
		return_string += str(item.wednesdayEnd)
		return_string += " "
	if(item.thursdayStart):
		return_string += "TH: "
		return_string += str(item.thursdayStart)
		return_string += " to "
		return_string += str(item.thursdayEnd)
		return_string += " "
	if(item.fridayStart):
		return_string += "F: "
		return_string += str(item.fridayStart)
		return_string += " to "
		return_string += str(item.fridayEnd)
		return_string += " "
	if(item.saturdayStart):
		return_string += "SA: "
		return_string += str(item.saturdayStart)
		return_string += " to "
		return_string += str(item.saturdayEnd)
		return_string += " "
	if(item.sundayStart):
		return_string += "SU: "
		return_string += str(item.sundayStart)
		return_string += " to "
		return_string += str(item.sundayEnd)
		return_string += " "
	return return_string
