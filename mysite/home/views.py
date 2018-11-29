from django.shortcuts import render
from django import forms
from django.db import IntegrityError
from django.http import HttpResponse
from django.urls import reverse
from home.forms import DayForm
from django.views import generic
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from home.models import *

# Want it so when user enters website, it immediately goes
# to login screen. May have a "rememember me" function or not later

def about(request):
    return render(request, 'home/about.html')

@login_required(login_url='login')
def home(request):
    return render(request, 'home/home.html')

@method_decorator(login_required(login_url='login'), name='dispatch')
# This view is used to enable the user to add new days for their anxiety.
class anxietyDayCreate(generic.CreateView):
    model = Day
    form_class = DayForm
    template_name = 'home/feeling-submission.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.symptom = Day.Anxiety
        try:
            return super(anxietyDayCreate,self).form_valid(form)
        except IntegrityError:
            form.add_error('log', 'You already have a rating and log today!')
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('home-anxiety-overview')

@method_decorator(login_required(login_url='login'), name='dispatch')
# This view is used to enable the user to add new days for their depression.
class depressionDayCreate(generic.CreateView):
    model = Day
    form_class = DayForm
    template_name = 'home/feeling-submission.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.symptom = Day.Depression
        try:
            return super(depressionDayCreate,self).form_valid(form)
        except IntegrityError:
            form.add_error('log', 'You already have a rating and log today!')
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('home-depression-overview')

@method_decorator(login_required(login_url='login'), name='dispatch')
class anxietyDayList(generic.ListView):
    model = Day
    context_object_name = 'anxiety_day_list' #custom name for day list as a template variable
    template_name = 'home/anxiety-overview.html' #custom template name/location

    def get_queryset(self):
        return Day.objects.filter(symptom='Anxiety',user=self.request.user)

@method_decorator(login_required(login_url='login'), name='dispatch')
class depressionDayList(generic.ListView):
    model = Day
    context_object_name = 'depression_day_list'
    template_name = 'home/depression-overview.html'

    def get_queryset(self):
        return Day.objects.filter(symptom='Depression',user=self.request.user)
