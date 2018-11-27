from django.shortcuts import render
<<<<<<< HEAD
from django import forms
from home.forms import DayLogForm
=======
from django.views import generic
from home.models import *

>>>>>>> master

# Want it so when user enters website, it immediately goes
# to login screen. May have a "rememember me" function or not later

def about(request):
    return render(request, 'home/about.html')


def home(request):
    return render(request, 'home/home.html')

<<<<<<< HEAD
def anxietyfeeling(request):
    form = DayLogForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            log = form.cleaned_data.get('log')
            messages.success(request,'Log submitted!')
            return redirect('home/anxiety-overview.html')
    else:
        form = DayLogForm()
    return render(request, 'home/feeling-submission.html', {'form': form})

def depressionfeeling(request):
    form = DayLogForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.POST.save()
            log = form.cleaned_data.POST.get('log')
            messages.success(request,'Log submitted!')
            return redirect('home/depression-overview.html')
    else:
        form = DayLogForm()
    return render(request, 'home/feeling-submission.html', {'form': form})
=======

def feeling(request):
    return render(request, 'home/feeling-submission.html')
>>>>>>> master


def anxietyOverview(request):
    return render(request, 'home/anxiety-overview.html')


def depressionOverview(request):
    return render(request, 'home/depression-overview.html')

<<<<<<< HEAD


=======
class dayList(generic.ListView):
    model = Day
    context_object_name = 'day-list' #custom name for day list as a template variable
    template_name = 'home/day-list.html' #custom template name/location
>>>>>>> master
