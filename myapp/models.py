from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# note that when creating Goals and SubGoals, need to asign objects
# to ForeignKeys, for example
"""
Goal.object.create(username = User.objects.get(username = 'somename'), name = '',discription = '', status = '', ,)
"""


class Goal(models.Model):
    name = models.CharField(max_length=100)
    discription = models.CharField(max_length=1000)
    statuse = models.BooleanField(default=False)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
