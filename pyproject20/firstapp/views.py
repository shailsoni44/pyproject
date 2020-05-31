from django.shortcuts import render,redirect
from django.http import HttpResponse
from firstapp import forms
from .models import Register 

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
    people=Register.object.get(id=id)
    people.delete()
    return redirect("/show")

def edit(request,id):
    people=Register.object.get(id=id)
    return render(request,"firstapp/success.html",{'people':people})        