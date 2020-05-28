from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# def home(request):
#     return HttpResponse("Hello, This is my first web page")

# def about(request):
#     return HttpResponse("This is about page")

# def contacts(request):
#     return HttpResponse("Please contact here")

def home(request):
    name="Hello,"
    return render(request,"firstapp/home.html",{"name":name})    