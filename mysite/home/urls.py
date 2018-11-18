from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='home'),
        path('about/', views.about, name='home-about'),
        path('anxiety-overview/feeling-submission/', views.feeling, name='home-anxiety-feeling-submission'),
        path('depression-overview/feeling-submission/', views.feeling, name='home-depression-feeling-submission'),
        path('anxiety-overview/', views.anxietyOverview, name='home-anxiety-overview'),
        path('depression-overview/', views.depressionOverview, name='home-depression-overview'),
        path('day-list/', views.dayList.as_view(), name='day-list'),
    ]
