from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import redirect

def main(request):
    return render_to_response('schedulePage.html', {'full_name': request.user.username, 'scheduleItems': courseInfoUser(request.user.username)})

def edit(request):
    return render_to_response('editSchedulePage.html', {'full_name': request.user.username, 'scheduleItems': courseInfoUser(request.user.username),  'sectionNumbers': sectionObjects() })
    
def PageObjects(request):
    return UserSchedule.objects.filter(userID__user__username=un)
	
def sectionObjects():
	sectionList = CourseSection.objects.all()
	courseList = CourseName.objects.all()
	newList = []
	for e in sectionList :
		for i in courseList:
			if e.courseID.courseID == i.courseID:
				newList.append(i.courseName + ":" + str(e.sectionNumber))
	return newList

def courseInfoUser(un):
  list = []
  for e in scheduleListUser(un):
    list.append(scheduleTime(e.scheduleID.scheduleID))
  return list

from profilePage.models import *
from django.core.exceptions import ObjectDoesNotExist

def scheduleListUser(un):
  return UserSchedule.objects.filter(userID__user__username=un)
  

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
    reg = False
    course = CourseSection.objects.get(discussionScheduleID=scheduleID)
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
