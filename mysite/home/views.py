from django.shortcuts import render

# Want it so when user enters website, it immediately goes
# to login screen. May have a "rememember me" function or not later

def about(request):
    return render(request, 'home/about.html')

def home(request):
    return render(request, 'home/home.html')


