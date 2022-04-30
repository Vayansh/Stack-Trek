from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from datetime import datetime
from siteapp1.models import siteusers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
#def index(request):

    #return HttpResponse("this is homepage")

def home(request):
    return render(request, 'homepage.html')

def MyReports(request):
    return HttpResponse("Your reports")

def landing(request):
    return render(request, 'index.html')
    if request.method == "POST":
        if 'signupbutton' in request.POST:
           username = request.POST.get('username')
           email = request.POST.get('email')
           password = request.POST.get('password')
           siteuser = siteusers(username=username, email=email, password=password, date=datetime.today())
           siteuser.save()
           messages.success(request, 'Your account has been created')
           return render(request, 'index.html')
        
        if 'loginbutton' in request.POST:
           username = request.POST.get('username')
           password = request.POST.get('password')

           user = authenticate(username=username, password=password)
           if user is not None:
                return render(request, 'homepage.html')
    