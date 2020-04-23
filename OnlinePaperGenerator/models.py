from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class subject(models.Model):
    subject_code = models.IntegerField(primary_key=True)
    subject_name = models.CharField(max_length=100)
    sem = models.IntegerField()
    faculty = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.subject_name