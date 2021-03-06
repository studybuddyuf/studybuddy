#Why is CourseNumber.sectionNumber an AutoField?

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
  if schedule.mondayStart:
    list.append('Monday')
    list.append(str(schedule.mondayStart))
    list.append(str(schedule.mondayEnd))
  if schedule.tuesdayStart:
    list.append('Tuesday')
    list.append(str(schedule.tuesdayStart))
    list.append(str(schedule.tuesdayEnd))
  if schedule.wednesdayStart:
    list.append('Wednesday')
    list.append(str(schedule.wednesdayStart))
    list.append(str(schedule.wednesdayEnd))
  if schedule.thursdayStart:
    list.append('Thursday')
    list.append(str(schedule.thursdayStart))
    list.append(str(schedule.thursdayEnd))
  if schedule.fridayStart:
    list.append('Friday')
    list.append(str(schedule.fridayStart))
    list.append(str(schedule.fridayEnd))
  if schedule.saturdayStart:
    list.append('Saturday')
    list.append(str(schedule.saturdayStart))
    list.append(str(schedule.saturdayEnd))
  if schedule.sundayStart:
    list.append('Sunday')
    list.append(str(schedule.sundayStart))
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
  



def courseInfoUser(un):
  list = []
  for e in scheduleListUser(un):
    list.append(scheduleTime(e.scheduleID.scheduleID))
  return list
    




