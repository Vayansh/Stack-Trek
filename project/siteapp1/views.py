from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("this is homepage")

def MyReports(request):
    return HttpResponse("Your reports")