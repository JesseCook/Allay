from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='home'),
        path('about/', views.about, name='home-about'),
        path('anxiety-overview/feeling-submission/', views.anxietyfeeling, name='home-anxiety-feeling-submission'),
        path('depression-overview/feeling-submission/', views.depressionfeeling, name='home-depression-feeling-submission'),
        path('anxiety-overview/', views.anxietyOverview, name='home-anxiety-overview'),
        path('depression-overview/', views.depressionOverview, name='home-depression-overview'),
    ]

