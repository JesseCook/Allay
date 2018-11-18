from django.shortcuts import render
from django.views import generic
from home.models import *

# Want it so when user enters website, it immediately goes
# to login screen. May have a "rememember me" function or not later

def about(request):
    return render(request, 'home/about.html')


def home(request):
    return render(request, 'home/home.html')


def feeling(request):
    return render(request, 'home/feeling-submission.html')


def anxietyOverview(request):
    return render(request, 'home/anxiety-overview.html')


def depressionOverview(request):
    return render(request, 'home/depression-overview.html')

class dayList(generic.ListView):
    model = Day
    context_object_name = 'day-list' #custom name for day list as a template variable
    template_name = 'home/day-list.html' #custom template name/location
