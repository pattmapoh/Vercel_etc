from django.urls import path
from . import views
urlpatterns = [
    # Define your URL patterns here
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('students/', views.students_list, name='students_list'),
    path('subjects/', views.subjects_list, name='subjects_list')
]
