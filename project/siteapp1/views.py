from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'homepage.html')
    #return HttpResponse("this is homepage")

def MyReports(request):
    return HttpResponse("Your reports")

def landing(request):
    return render(request, 'index.html')