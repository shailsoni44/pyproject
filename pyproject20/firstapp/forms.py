from django import forms
from django.core import validators
from django.forms import ModelForm
from firstapp.models import Register

# def checkpass(password):  #Worked
#     #password=self.cleaned_data['password']
#     if len(password)<=5:
#         raise forms.ValidationError("Please choose password with less than 5 charactors")

def checkpass(password):
    uc=0
    lc=0
    sc=0
    nu=0
    for i in range(len(password)):
        if password[i].isalnum():
            if password[i].islower():
                lc+=1
            elif password[i].isupper():
                uc+=1
            elif password[i].isdigit():
                nu+=1
        else:
            sc+=1
    if lc < 1 or uc < 1 or sc < 2 or nu < 1:
        raise forms.ValidationError("Please inclued atlease 1 uppercase, lowercase and numrical value as well as 2 special charactors")
        

# def name(fname):
#     if fname[0].lower()!="a":
#         raise forms.ValidationError("Name Should start with a")

# Normal form
# class Registerform(forms.Form):
#     first_name = forms.CharField(label="Enter your first name", validators=[name])
#     last_name = forms.CharField(label="Enter your last name")
#     email = forms.EmailField(max_length=50)
#     repeat_email = forms.EmailField(max_length=50)
#     password = forms.CharField(widget=forms.PasswordInput, validators=[checkpass]) # , validators=[validators.MinLengthValidator(6)])
#     #text = forms.CharField(widget=forms.Textarea)

    # def checkpass(self):  #NOT WORKING INSIDE CLASS
    #     #password=self.cleaned_data['password']
    #     if len(self.cleaned_data['password'])<=5:
    #         raise forms.ValidationError("Please choose password with less than 5 charactors")
        
    # def clean(self):
    #     email=self.cleaned_data['email']
    #     remail=self.cleaned_data['repeat_email']
    #     if email!=remail:
    #         raise forms.ValidationError("email doesn't match")

    # def name(self): #NOT WORKING INSIDE CLASS
    #     name=forms.cleaned_data['first_name']
    #     if name[0].lower()!="a":
    #         raise forms.ValidationError("Name Should start with a")   
    # 

# Form using ModelForm
class Registerform(forms.ModelForm): 
    password = forms.CharField(widget=forms.PasswordInput, validators=[checkpass])
    class Meta:
        model=Register
        #fields="__all__"
        include=["first_name","last_name","email","repeat_email"]
        exclude=[]

    def clean(self):
        email=self.cleaned_data['email']
        remail=self.cleaned_data['repeat_email']
        if email!=remail:
            raise forms.ValidationError("email doesn't match")        