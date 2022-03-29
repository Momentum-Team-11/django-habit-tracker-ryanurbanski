from .models import Habit, Record
from django import forms


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = (
            'goal_name',
            'goal_value', 
            'goal units',
            'goal_date',
            'track_daily',
            'track_monthly',
            'track_yearly',
            )

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ("goal_value")

