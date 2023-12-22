from django.contrib import admin
from django.urls import path,include
from home import views

#Django admin header configuration
admin.site.site_title="Welcome to Chinthana's dashboard"
admin.site.site_header="Developer Chinthana"
admin.site.index_title="Welcome to this portal Chinthana"

urlpatterns = [
  
    path('',views.home,name='home'),
    path('about',views.About,name='about'),
    path('projects',views.Projects,name='projects'),
    path('contact/',views.contact_view,name='contact'),

]