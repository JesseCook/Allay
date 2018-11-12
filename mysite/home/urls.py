from django.urls import path
from . import views

urlpatterns = [
        path('home/', views.home, name='home-home'),
        path('about/', views.about, name='home-about'),
        path('feeling-submission/', views.feeling, name='home-feeling-submission'),
    ]
