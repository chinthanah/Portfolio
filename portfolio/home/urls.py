from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
  
    path('',views.home,name='home'),
    path('about',views.About,name='about'),
    path('projects',views.Projects,name='projects'),
    path('contact',views.Contact,name='contact'),

]