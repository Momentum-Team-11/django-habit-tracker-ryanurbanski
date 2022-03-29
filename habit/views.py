from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Habit, Record
# from .forms import DeckForm, CardForm



def base(request):
    return render(request, 'base.html')


def home(request):
    if request.user.is_authenticated:
        return redirect('list_habits')
    else:
        return render(request, 'home.html')


@login_required
def list_habits(request):
    habits = Habit.objects.all()
    user = request.user
    template = ''
    context = ''

    return render(request,'list_habits.html')