from django.contrib import admin
from django.urls import path
from siteapp1 import views

urlpatterns = [
    path('', views.index , name="home"),
    path('MyReports', views.MyReports , name="MyReports")
]