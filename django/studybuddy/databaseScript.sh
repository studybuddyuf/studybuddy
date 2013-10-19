#!/bin/sh

# Only run the script if it is being run from the same directory as the studyBuddy.db file
if ! test -s ./studyBuddy.db
then
    echo "ERROR: This script must be run from the directory where studyBuddy.db resides"
    echo "Please change your directory to the directory which contains studyBuddy.db"
    exit
fi

# 1. rm studyBuddy.db
rm -f ./studyBuddy.db

# Tell the user to answer "no" when prompted about creating a superuser
echo
echo "******************************************************************************"
echo "***** Type \"no\" (without the quotes) when prompted to create a superuser *****"
echo "******************************************************************************"
echo

# 2. python manage.py syncdb
python manage.py syncdb

# 3. Run commands in python shell
python manage.py shell << HERE

from django.contrib.auth.models import User
from profilePage.models import *


#Semester(semester,startDate,endDate)
fall13 = Semester(semester='Fall 2013', startDate='2012-01-01', endDate='2012-05-31')
fall13.save()

#adding Artificial Intelligence and Heuristics
sch1 = Schedule(scheduleID=1, mondayStart='09:35',mondayEnd='10:25',wednesdayStart='09:35', wednesdayEnd='10:25', fridayStart='09:35', fridayEnd='10:25')
sch1.save()
cn = CourseName(courseID='CAP4621',courseName='Artificial Intelligence and Heuristics')
cn.save()
cs = CourseSection(courseID=cn,semester=fall13, sectionNumber=9001 ,regularScheduleID=sch1)
cs.save()

#adding software engineering
cn = CourseName(courseID='CEN3031',courseName='Introduction to Software Engineering')
cn.save()
sch2 = Schedule(scheduleID=2, mondayStart='12:50',mondayEnd='1:40',wednesdayStart='12:50', wednesdayEnd='1:40', fridayStart='12:50', fridayEnd='1:40')
sch2.save()
sch3 = Schedule(scheduleID=3, wednesdayStart='10:40', wednesdayEnd='11:30')
sch3.save()
cs1 = CourseSection(courseID=cn,semester=fall13,regularScheduleID=sch2, discussionScheduleID=sch3)
cs1.save()


#addig operating systems
cn = CourseName(courseID='COP4600',courseName='Operating Systems')
cn.save()
sch4 = Schedule(scheduleID=4, mondayStart='09:35',mondayEnd='10:25',wednesdayStart='09:35', wednesdayEnd='10:25', fridayStart='09:35', fridayEnd='10:25')
sch4.save()
sch5 = Schedule(scheduleID=5, tuesdayStart='09:35',tuesdayEnd='10:25')
sch5.save()
cs = CourseSection(courseID=cn,semester=fall13,regularScheduleID=sch4, discussionScheduleID=sch5)
cs.save()

#makeing 5 AUTH_USERS (not a studyBuddy User)
user1 = User(id=1, username='vanwirer', first_name='Vanwirer', last_name='Griffin', email='hackYou@gmail.com',last_login='2013-12-12 08:15:16+00:00', is_superuser=1, is_staff=1, is_active=1, date_joined='2013-10-10 00:00:00+00:00')
user1.set_password('pass')
user1.save()
sbu1 = StudyBuddyUser(user_id=1,phone = 1234567891,school_name = 'University of Florida', year = 5)
sbu1.save()
#adding schedule items.
usi = UserSchedule(userID=sbu1,scheduleID=sch1)
usi.save()
usi = UserSchedule(userID=sbu1,scheduleID=sch2)
usi.save()
usi = UserSchedule(userID=sbu1,scheduleID=sch3)
usi.save()


user2 = User(id=2, username='user2', first_name='firstUser2', last_name='lastUser2', email='user2@gmail.com',last_login='2013-12-12 08:15:16+00:00', is_superuser=0, is_staff=0, is_active=1, date_joined='2013-10-10 00:00:00+00:00')
user2.set_password('pass')
user2.save()
sbu2 = StudyBuddyUser(user_id=2,phone = 1234567891,school_name = 'University of Florida', year = 5)
sbu2.save()
usi = UserSchedule(userID=sbu2,scheduleID=sch2)
usi.save()
usi = UserSchedule(userID=sbu2,scheduleID=sch3)
usi.save()
usi = UserSchedule(userID=sbu2,scheduleID=sch4)
usi.save()
usi = UserSchedule(userID=sbu2,scheduleID=sch5)
usi.save()


user3 = User(id=3, username='user3', first_name='firstUser3', last_name='lastUser3', email='user3@gmail.com',last_login='2013-12-12 08:15:16+00:00', is_superuser=0, is_staff=0, is_active=1, date_joined='2013-10-10 00:00:00+00:00')
user3.set_password('pass')
user3.save()
sbu3 = StudyBuddyUser(user_id=3,phone = 1234567891,school_name = 'University of Florida', year = 5)
sbu3.save()

user4 = User(id=4, username='user4', first_name='firstUser4', last_name='lastUser4', email='user4@gmail.com',last_login='2013-12-12 08:15:16+00:00', is_superuser=0, is_staff=0, is_active=1, date_joined='2013-10-10 00:00:00+00:00')
user4.set_password('pass')
user4.save()
sbu4 = StudyBuddyUser(user_id=4,phone = 1234567891,school_name = 'University of Florida', year = 5)
sbu4.save()

user5 = User(id=5, username='user5', first_name='firstUser5', last_name='lastUser5', email='user5@gmail.com',last_login='2013-12-12 08:15:16+00:00', is_superuser=0, is_staff=0, is_active=1, date_joined='2013-10-10 00:00:00+00:00')
user5.set_password('pass')
user5.save()
sbu5 = StudyBuddyUser(user_id=5,phone = 1234567891,school_name = 'University of Florida', year = 5)
sbu5.save()

exit()

HERE

echo
