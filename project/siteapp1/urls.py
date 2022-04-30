from django.contrib import admin
from django.urls import path
from siteapp1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', views.home , name="home"),
    path('MyReports', views.MyReports , name="MyReports"),
    path('', views.landing, name="landing")
    
]