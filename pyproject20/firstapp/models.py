from django.db import models

# Create your models here.
# models are in form of class

class Signup(models.Model):
    email=models.EmailField(max_length=40)
    password=models.CharField(max_length=20)
    repeatpassword=models.CharField(max_length=20)
    class Meta:
        verbose_name = "Signup"
        verbose_name_plural = "Signup" #to fix admin plural show