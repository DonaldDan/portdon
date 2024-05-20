from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('upcoming/', views.upcoming, name='upcoming'),
    path('ongoing/', views.ongoing, name='ongoing'),
]
