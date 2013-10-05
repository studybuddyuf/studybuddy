from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class StudyBuddyUser(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=10)
    school_name = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField(null=True)

User.profile = property(lambda u: StudyBuddyUser.objects.get_or_create(user=u)[0])
