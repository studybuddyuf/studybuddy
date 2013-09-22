from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    school = models.CharField(max_length=50)
    class_year = models.PositiveSmallIntegerField(max_length=1)
