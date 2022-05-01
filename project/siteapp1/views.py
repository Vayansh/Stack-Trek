from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from datetime import datetime
from siteapp1.models import uploadData
from siteapp1.models import siteusers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
#def index(request):

    #return HttpResponse("this is homepage")

def home(request):
    if request.method == "POST":
       
        bp = request.POST.get('bp')
        sugar = request.POST.get('sugar')
        chole = request.POST.get('chole')
        bmi = request.POST.get('bmi')
        smoke = request.POST.get('smoke')
        drink = request.POST.get('drink')
        data = uploadData(bp=bp, sugar=sugar, chole=chole, bmi=bmi, smoke=smoke, drink=drink)
        data.save()
        return render(request, 'homepage.html')
    return render(request, 'homepage.html')

def MyReports(request):
    return HttpResponse("Your reports")

def landing(request):
    if request.method!="POST":
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
           else:
               return render(request, 'index.html')
    