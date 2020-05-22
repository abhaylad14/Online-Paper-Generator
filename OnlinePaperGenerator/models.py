from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class subject(models.Model):
    subject_code = models.CharField(default = "", max_length=15)
    subject_name = models.CharField(max_length=100)
    sem = models.IntegerField()
    faculty = models.CharField(max_length=50,null=True, blank=True)

    def __str__(self):
        return self.subject_name

class questionbank(models.Model):
    subject_code = models.CharField(default = "", max_length=15)
    chapterno = models.IntegerField(default=0)
    marks = models.IntegerField(default=0)
    difficulty = models.CharField(max_length = 10)
    priority = models.CharField(max_length = 10)
    content = models.CharField(max_length = 500)

    def __str__(self):
        return self.content

