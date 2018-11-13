from django.urls import path
from . import views

urlpatterns = [
        path('home/', views.home, name='home-home'),
        path('about/', views.about, name='home-about'),
        path('feeling-submission/', views.feeling, name='home-feeling-submission'),
        path('anxiety-overview/', views.anxietyOverview, name='home-anxiety-overview'),
        path('depression-overview/', views.depressionOverview, name='home-depression-overview'),
    ]
