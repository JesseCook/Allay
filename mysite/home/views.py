from django.shortcuts import render
from django import forms
from home.forms import DayLogForm

# Want it so when user enters website, it immediately goes
# to login screen. May have a "rememember me" function or not later

def about(request):
    return render(request, 'home/about.html')

def home(request):
    return render(request, 'home/home.html')

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

def anxietyOverview(request):
    return render(request, 'home/anxiety-overview.html')
    
def depressionOverview(request):
    return render(request, 'home/depression-overview.html')



