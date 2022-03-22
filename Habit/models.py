from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import dateline


class User(AbstractUser):
    def __str__(self):
        return self.username

class Habit(models.Model):
    goal_name = models.CharField(max_length=200)
    goal_value = models.IntegerField(max_length=10)
    goal_units = models.CharField(max_length=20)
    current_value = models.IntegerField(default=0, max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    goal_date = models.DateTimeField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    track_daily = models.BooleanField(default=True, null=True)
    track_monthly = models.BooleanField(default=False, null=True)
    track_yearly = models.BooleanField(default=False, null=True)
    
    def __str__(self):
        return self.goal

class Record(models.Model):
    """ Everyday this will save a single snapshot of the habit's progress """
    pass
