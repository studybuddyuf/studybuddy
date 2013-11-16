#!/bin/sh

# Only run the script if it is being run from the same directory as the studyBuddy.db file
if ! test -s ./databaseScript.sh
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


#adding operating systems
cn = CourseName(courseID='COP4600',courseName='Operating Systems')
cn.save()
sch4 = Schedule(scheduleID=4, mondayStart='09:35',mondayEnd='10:25',wednesdayStart='09:35', wednesdayEnd='10:25', fridayStart='09:35', fridayEnd='10:25')
sch4.save()
sch5 = Schedule(scheduleID=5, tuesdayStart='09:35',tuesdayEnd='10:25')
sch5.save()
cs = CourseSection(courseID=cn,semester=fall13,regularScheduleID=sch4, discussionScheduleID=sch5)
cs.save()

#adding numerical analysis
cn = CourseName(courseID='COT4501',courseName='Numerical Analysis')
cn.save()
sch6 = Schedule(scheduleID=6, mondayStart='10:40',mondayEnd='11:30',wednesdayStart='10:40', wednesdayEnd='11:30', fridayStart='10:40', fridayEnd='11:30')
sch6.save()
sch7 = Schedule(scheduleID=7, tuesdayStart='09:35',tuesdayEnd='10:25')
sch7.save()
cs = CourseSection(courseID=cn,semester=fall13,regularScheduleID=sch6, discussionScheduleID=sch7)
cs.save()

#adding digital logic
cn = CourseName(courseID='EEL3701',courseName='Digital Logic')
cn.save()
sch8 = Schedule(scheduleID=8, mondayStart='03:00',mondayEnd='03:50',wednesdayStart='03:00', wednesdayEnd='03:50', fridayStart='03:00', fridayEnd='03:50')
sch8.save()
sch9 = Schedule(scheduleID=9, tuesdayStart='08:30',tuesdayEnd='09:20')
sch9.save()
cs = CourseSection(courseID=cn,semester=fall13,regularScheduleID=sch8, discussionScheduleID=sch9)
cs.save()

#adding linear algebra
cn = CourseName(courseID='MAS3114',courseName='Linear Algebra')
cn.save()
sch10 = Schedule(scheduleID=10, mondayStart='03:00',mondayEnd='03:50',wednesdayStart='03:00', wednesdayEnd='03:50', fridayStart='03:00', fridayEnd='03:50')
sch10.save()
sch11 = Schedule(scheduleID=11, tuesdayStart='01:55',tuesdayEnd='02:45')
sch11.save()
cs = CourseSection(courseID=cn,semester=fall13,regularScheduleID=sch10, discussionScheduleID=sch11)
cs.save()

#adding calculus 1
cn = CourseName(courseID='MAC2311',courseName='Calculus 1')
cn.save()
sch12 = Schedule(scheduleID=12, mondayStart='03:00',mondayEnd='03:50',wednesdayStart='03:00', wednesdayEnd='03:50', fridayStart='03:00', fridayEnd='03:50')
sch12.save()
sch13 = Schedule(scheduleID=13, tuesdayStart='01:55',tuesdayEnd='02:45')
sch13.save()
cs = CourseSection(courseID=cn,semester=fall13,regularScheduleID=sch12, discussionScheduleID=sch13)
cs.save()

#adding calculus 2
cn = CourseName(courseID='MAC2312',courseName='Calculus 2')
cn.save()
sch14 = Schedule(scheduleID=14, mondayStart='09:35',mondayEnd='10:25',wednesdayStart='09:35', wednesdayEnd='10:25', fridayStart='09:35', fridayEnd='10:25')
sch14.save()
sch15 = Schedule(scheduleID=15, tuesdayStart='04:05',tuesdayEnd='04:55')
sch15.save()
cs = CourseSection(courseID=cn,semester=fall13,regularScheduleID=sch14, discussionScheduleID=sch15)
cs.save()

#adding calculus 3
cn = CourseName(courseID='MAC2313',courseName='Calculus 3')
cn.save()
sch16 = Schedule(scheduleID=16, mondayStart='12:50',mondayEnd='01:40',wednesdayStart='12:50', wednesdayEnd='01:40', fridayStart='12:50', fridayEnd='01:40')
sch16.save()
sch17 = Schedule(scheduleID=17, tuesdayStart='01:55',tuesdayEnd='02:45')
sch17.save()
cs = CourseSection(courseID=cn,semester=fall13,regularScheduleID=sch16, discussionScheduleID=sch17)
cs.save()

#adding human sexuality
cn = CourseName(courseID='FOS2001',courseName='Mans Food')
cn.save()
sch18 = Schedule(scheduleID=18, mondayStart='08:30',mondayEnd='09:20',wednesdayStart='08:30', wednesdayEnd='09:20', fridayStart='08:30', fridayEnd='09:20')
sch18.save()
sch19 = Schedule(scheduleID=19, tuesdayStart='01:55',tuesdayEnd='02:45')
sch19.save()
cs = CourseSection(courseID=cn,semester=fall13,regularScheduleID=sch18, discussionScheduleID=sch19)
cs.save()

#adding human sexuality
cn = CourseName(courseID='ANT2301',courseName='Human Sexuality')
cn.save()
sch20 = Schedule(scheduleID=20, mondayStart='04:05',mondayEnd='06:00',wednesdayStart='03:00', wednesdayEnd='03:50', fridayStart='03:00', fridayEnd='03:50')
sch20.save()
sch21 = Schedule(scheduleID=21, tuesdayStart='01:55',tuesdayEnd='02:45')
sch21.save()
cs = CourseSection(courseID=cn,semester=fall13,regularScheduleID=sch20, discussionScheduleID=sch21)
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

user6 = User(id=6, username='Bobooshki', first_name='John', last_name='Williams', email='user6@gmail.com',last_login='2013-12-12 08:15:16+00:00', is_superuser=0, is_staff=0, is_active=1, date_joined='2013-10-10 00:00:00+00:00')
user6.set_password('pass')
user6.save()
sbu6 = StudyBuddyUser(user_id=6,phone = 1234555891,school_name = 'University of Florida', year = 2)
sbu6.save()
usi = UserSchedule(userID=sbu6,scheduleID=sch1)
usi.save()
usi = UserSchedule(userID=sbu6,scheduleID=sch2)
usi.save()
usi = UserSchedule(userID=sbu6,scheduleID=sch3)
usi.save()
usi = UserSchedule(userID=sbu6,scheduleID=sch4)
usi.save()
usi = UserSchedule(userID=sbu6,scheduleID=sch16)
usi.save()
usi = UserSchedule(userID=sbu6,scheduleID=sch17)
usi.save()

user7 = User(id=7, username='coolman123', first_name='Craig', last_name='David', email='user7@gmail.com',last_login='2013-12-12 08:15:16+00:00', is_superuser=0, is_staff=0, is_active=1, date_joined='2013-10-10 00:00:00+00:00')
user7.set_password('pass')
user7.save()
sbu7 = StudyBuddyUser(user_id=7,phone = 1234562391,school_name = 'University of Florida', year = 2)
sbu7.save()
usi = UserSchedule(userID=sbu7,scheduleID=sch3)
usi.save()
usi = UserSchedule(userID=sbu7,scheduleID=sch5)
usi.save()
usi = UserSchedule(userID=sbu7,scheduleID=sch6)
usi.save()
usi = UserSchedule(userID=sbu7,scheduleID=sch7)
usi.save()
usi = UserSchedule(userID=sbu7,scheduleID=sch20)
usi.save()
usi = UserSchedule(userID=sbu7,scheduleID=sch21)
usi.save()

user8 = User(id=8, username='soSlick234', first_name='Sean', last_name='Parker', email='user8@gmail.com',last_login='2013-12-12 08:15:16+00:00', is_superuser=0, is_staff=0, is_active=1, date_joined='2013-10-10 00:00:00+00:00')
user8.set_password('pass')
user8.save()
sbu8 = StudyBuddyUser(user_id=8,phone = 1234999891,school_name = 'University of Florida', year = 4)
sbu8.save()
usi = UserSchedule(userID=sbu8,scheduleID=sch1)
usi.save()
usi = UserSchedule(userID=sbu8,scheduleID=sch2)
usi.save()
usi = UserSchedule(userID=sbu8,scheduleID=sch6)
usi.save()
usi = UserSchedule(userID=sbu8,scheduleID=sch7)
usi.save()
usi = UserSchedule(userID=sbu8,scheduleID=sch14)
usi.save()
usi = UserSchedule(userID=sbu8,scheduleID=sch15)
usi.save()

user9 = User(id=9, username='BillyBoy', first_name='Billy', last_name='Joe', email='user9@gmail.com',last_login='2013-12-12 08:15:16+00:00', is_superuser=0, is_staff=0, is_active=1, date_joined='2013-10-10 00:00:00+00:00')
user9.set_password('pass')
user9.save()
sbu9 = StudyBuddyUser(user_id=9,phone = 2244567891,school_name = 'University of Florida', year = 3)
sbu9.save()
usi = UserSchedule(userID=sbu9,scheduleID=sch2)
usi.save()
usi = UserSchedule(userID=sbu9,scheduleID=sch3)
usi.save()
usi = UserSchedule(userID=sbu9,scheduleID=sch8)
usi.save()
usi = UserSchedule(userID=sbu9,scheduleID=sch9)
usi.save()

user10 = User(id=10, username='gogo123', first_name='Jill', last_name='Baker', email='user10@gmail.com',last_login='2013-12-12 08:15:16+00:00', is_superuser=0, is_staff=0, is_active=1, date_joined='2013-10-10 00:00:00+00:00')
user10.set_password('pass')
user10.save()
sbu10 = StudyBuddyUser(user_id=10,phone = 1234562391,school_name = 'University of Florida', year = 2)
sbu10.save()
usi = UserSchedule(userID=sbu10,scheduleID=sch4)
usi.save()
usi = UserSchedule(userID=sbu10,scheduleID=sch5)
usi.save()
usi = UserSchedule(userID=sbu10,scheduleID=sch6)
usi.save()
usi = UserSchedule(userID=sbu10,scheduleID=sch7)
usi.save()

user11 = User(id=11, username='crazyMan', first_name='Sue', last_name='Bell', email='user11@gmail.com',last_login='2013-12-12 08:15:16+00:00', is_superuser=0, is_staff=0, is_active=1, date_joined='2013-10-10 00:00:00+00:00')
user11.set_password('pass')
user11.save()
sbu11 = StudyBuddyUser(user_id=11,phone = 1234999891,school_name = 'University of Florida', year = 4)
sbu11.save()
usi = UserSchedule(userID=sbu11,scheduleID=sch2)
usi.save()
usi = UserSchedule(userID=sbu11,scheduleID=sch3)
usi.save()
usi = UserSchedule(userID=sbu11,scheduleID=sch4)
usi.save()
usi = UserSchedule(userID=sbu11,scheduleID=sch5)
usi.save()
usi = UserSchedule(userID=sbu11,scheduleID=sch10)
usi.save()
usi = UserSchedule(userID=sbu11,scheduleID=sch11)
usi.save()

user12 = User(id=12, username='CutiePatooti', first_name='Jane', last_name='Jerry', email='user12@gmail.com',last_login='2013-12-12 08:15:16+00:00', is_superuser=0, is_staff=0, is_active=1, date_joined='2013-10-10 00:00:00+00:00')
user12.set_password('pass')
user12.save()
sbu12 = StudyBuddyUser(user_id=12,phone = 2244567891,school_name = 'University of Florida', year = 3)
sbu12.save()
usi = UserSchedule(userID=sbu12,scheduleID=sch6)
usi.save()
usi = UserSchedule(userID=sbu12,scheduleID=sch7)
usi.save()
usi = UserSchedule(userID=sbu12,scheduleID=sch18)
usi.save()
usi = UserSchedule(userID=sbu12,scheduleID=sch19)
usi.save()
usi = UserSchedule(userID=sbu12,scheduleID=sch12)
usi.save()
usi = UserSchedule(userID=sbu12,scheduleID=sch13)
usi.save()

exit()

HERE

echo
