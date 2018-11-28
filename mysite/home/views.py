from django.shortcuts import render
from django import forms
from home.forms import DayForm
from django.views import generic
from django.contrib import messages
from django.shortcuts import render, redirect
from home.models import *

# Want it so when user enters website, it immediately goes
# to login screen. May have a "rememember me" function or not later

def about(request):
    return render(request, 'home/about.html')


def home(request):
    return render(request, 'home/home.html')

def anxietyfeeling(request):
    if request.method == 'POST':
        form = DayForm(request.POST)
        form.fields["symptom"].initial = 'Anxiety'
        if form.is_valid():
            form.save()
            log = form.cleaned_data.get('log')
            messages.success(request,'Log submitted!')
            return redirect('home/anxiety-overview.html')
    else:
        form = DayForm()
    return render(request, 'home/feeling-submission.html', {'form': form})

def depressionfeeling(request):
    form = DayForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.POST.save()
            log = form.cleaned_data.POST.get('log')
            messages.success(request,'Log submitted!')
            return redirect('home/depression-overview.html')
    else:
        form = DayForm()
    return render(request, 'home/feeling-submission.html', {'form': form})


def anxietyOverview(request):
    return render(request, 'home/anxiety-overview.html')


def depressionOverview(request):
    return render(request, 'home/depression-overview.html')
  
  
class anxietyDayList(generic.ListView):
    model = Day
    context_object_name = 'anxiety_day_list' #custom name for day list as a template variable
    template_name = 'home/anxiety-overview.html' #custom template name/location

    def get_queryset(self):
        return Day.objects.filter(symptom='Anxiety',user=self.request.user)

class depressionDayList(generic.ListView):
    model = Day
    context_object_name = 'depression_day_list'
    template_name = 'home/depression-overview.html'

    def get_queryset(self):
        return Day.objects.filter(symptom='Depression',user=self.request.user)
