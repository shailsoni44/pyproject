from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from firstapp import forms
from .models import Register, Signup, Session
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer, SignupSerializer, SessionSerializer
from django.views.generic import TemplateView
from rest_framework import viewsets
from . import models
from . import serializers

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

def form_view(request):
    #form=forms.Registerform
    if request.method=="POST":
        form=forms.Registerform(request.POST)
        if form.is_valid():
            # print("Validation Successuful")
            # print("First Name: "+form.cleaned_data["first_name"])
            # print("Last Name: "+form.cleaned_data["last_name"])
            # print("Password: "+form.cleaned_data["password"], "\nAnd length of passwaord:", len(form.cleaned_data["password"]))
            try:
                form.save()
                return redirect("success")
            except:
                print("Error saving the form")
    else:
        form=forms.Registerform
    return render(request,"firstapp/index.html",{"form":form})

def success(request):
    people=Register.objects.all()
    return render(request,"firstapp/success.html",{'people':people})

def destroy(request,id):
    person=Register.object.get(id=id)
    person.delete()
    return redirect("/show")

def edit(request,id):
    people=Register.object.get(id=id)
    return render(request,"firstapp/success.html",{'people':people})

def random(request):
    data={1:{'name':'Shail','age':26}, 2:{'name':'abc','age':30}}
    return JsonResponse(data)        

class LoginList(APIView):
    def get(self,request):
        values=Register.objects.all()
        serializer=RegisterSerializer(values, many=True)
        return Response(serializer.data)

class SignupList(TemplateView):
    template_name='firstapp/index.html'

class RegisterViewSet(viewsets.ModelViewSet):
    queryset=models.Register.objects.all()
    serializer_class=serializers.RegisterSerializer    

class SessionViewSet(viewsets.ModelViewSet):
    queryset=models.Session.objects.all()
    serializer_class=serializers.SessionSerializer

class SignupViewSet(viewsets.ModelViewSet):
    queryset=models.Signup.objects.all()
    serializer_class=serializers.SignupSerializer