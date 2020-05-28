from django.urls import path
from firstapp import views

urlpatterns = [
    #1 url
    #2 file
    path("home",views.home, name="home"),
    # path("about",views.about),
    # path("contact_us",views.contacts, name="contact"),
]