from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class StudyBuddyUser(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=10)
    school_name = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField(null=True)
    schedule = models.ForeignKey('UserSchedule', null=True, blank=True)
    about_me = models.CharField(max_length=1000)

    def __unicode__(self):
	return self.user.username

User.profile = property(lambda u: StudyBuddyUser.objects.get_or_create(user=u)[0])

class UserSchedule(models.Model):
	userID = models.ForeignKey(StudyBuddyUser)
	scheduleID = models.ForeignKey('Schedule')

	class Meta:
		unique_together = (('userID','scheduleID'),)
	
   	def __unicode__(self):
                return u'%s\'s schedule object %s' % (self.userID, self.scheduleID)

class Schedule(models.Model):
	scheduleID = models.AutoField(primary_key=True)

	mondayStart = models.TimeField(null=True, blank=True)
	mondayEnd = models.TimeField(null=True, blank=True)

	tuesdayStart = models.TimeField(null=True, blank=True)
	tuesdayEnd = models.TimeField(null=True, blank=True)

	wednesdayStart = models.TimeField(null=True, blank=True)
	wednesdayEnd = models.TimeField(null=True, blank=True)

	thursdayStart = models.TimeField(null=True, blank=True)
	thursdayEnd = models.TimeField(null=True, blank=True)

	fridayStart = models.TimeField(null=True, blank=True)
	fridayEnd = models.TimeField(null=True, blank=True)

	saturdayStart = models.TimeField(null=True, blank=True)
	saturdayEnd = models.TimeField(null=True, blank=True)

	sundayStart = models.TimeField(null=True, blank=True)
	sundayEnd = models.TimeField(null=True, blank=True)

	def __unicode__(self):
		return "Schedule with ID: "+str(self.scheduleID)

class CourseSection(models.Model):
	courseID = models.ForeignKey('CourseName')
	semester = models.ForeignKey('Semester')
	sectionNumber = models.AutoField(primary_key=True)
	regularScheduleID = models.ForeignKey(Schedule, related_name='regular')
	discussionScheduleID = models.ForeignKey(Schedule, related_name='discussion', null=True, blank=True)
	
	def __unicode__(self):
		return str(self.sectionNumber)

class CourseName(models.Model):
	courseID = models.CharField(primary_key=True, max_length=10)
	courseName = models.CharField(max_length=100)

	def __unicode__(self):
		return self.courseID

class Semester(models.Model):
	semester = models.CharField(primary_key = True, max_length = 15)
	startDate = models.DateField()
	endDate = models.DateField()

	def __unicode__(self):
		return self.semester

class StudyBuddyRequest(models.Model):
	requesterUserID = models.ForeignKey(StudyBuddyUser, related_name='requester')
	requesteeUserID = models.ForeignKey(StudyBuddyUser, related_name='requestee')
	courseID = models.ForeignKey('CourseName')
	semester = models.ForeignKey('Semester')
	sectionNumber = models.ForeignKey('CourseSection')
	status = models.CharField(max_length=1)

	class Meta:
		unique_together = (('requesterUserID', 'requesteeUserID', 'courseID', 'semester', 'sectionNumber'),)
