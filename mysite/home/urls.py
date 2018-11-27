from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='home'),
        path('about/', views.about, name='home-about'),
        path('anxiety-overview/feeling-submission/', views.feeling, name='home-anxiety-feeling-submission'),
        path('depression-overview/feeling-submission/', views.feeling, name='home-depression-feeling-submission'),
        path('anxiety-overview/', views.anxietyDayList.as_view(), name='home-anxiety-overview'),
        path('depression-overview/', views.depressionDayList.as_view(), name='home-depression-overview'),
    ]

