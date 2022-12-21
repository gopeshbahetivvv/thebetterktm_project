import email
from email.policy import default
import numbers
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Problem(models.Model):
    name= models.CharField(max_length=70)
    emailid= models.EmailField(max_length=200)
    number=models.CharField(max_length=16)
    subject=models.CharField(max_length=200, default='')
    problemtext=models.CharField(max_length=1000)
    anonymity=models.BooleanField()
    upvote=models.IntegerField(default=0)
    iptracker = models.JSONField(default='')

    def __str__(self):
        return self.subject

# class User(models.Model):
#     userip = models.JSONField()

#     def __str__(self):
#         return self.userip
