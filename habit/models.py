from django.db import models

from config import settings


class Habit(models.Model):
    goal_name = models.CharField(max_length=200)
    goal_value = models.IntegerField()
    goal_units = models.CharField(max_length=20)
    # current_value = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    goal_date = models.DateField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # track_daily = models.BooleanField(default=True, null=True)
    # track_monthly = models.BooleanField(default=False, null=True)
    # track_yearly = models.BooleanField(default=False, null=True)
    
    def __str__(self):
        return self.goal_name

class Record(models.Model):
    """ Everyday this will save a single snapshot of the habit's progress """
    value = models.IntegerField
    date = models.DateTimeField(auto_now_add=True)
    habit = models.ForeignKey(Habit, related_name='record', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.value} {self.date}"
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["value", "date", "habit"])
        ]


