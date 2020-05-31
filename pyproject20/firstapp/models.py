from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError

# Create your models here.
# models are in form of class

class Signup(models.Model):
    email=models.EmailField(max_length=40)
    password=models.CharField(max_length=20)
    repeatpassword=models.CharField(max_length=20)

    class Meta:
        verbose_name = "Signup"
        verbose_name_plural = "Signup" #to fix admin plural show
    
    def __str__(self):
        return self.email

class Session(models.Model):
    session = models.CharField(max_length=40,unique=True,primary_key=True)
    
    class Meta:
        verbose_name = "Field of study"
        verbose_name_plural = "Fields of study"
    
    def __str__(self):
        return self.session


class Student(models.Model):
    name = models.CharField(max_length=25,unique=False)
    session=models.ForeignKey("Session",on_delete=models.PROTECT)


class Register(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    repeat_email = models.EmailField(max_length=50)
    
    class Meta:
        verbose_name_plural="Register"
    
    def __str__(self):
        return self.first_name
        
       
    
    
