from django.urls import path
from firstapp import views

urlpatterns = [
    #1 url
    #2 file
    path("home",views.home, name="home"),
    # path("about",views.about),
    # path("contact_us",views.contacts, name="contact"),
    path("register",views.form_view, name="register"),
    path("success",views.success, name="success"),
    path("destroy/<int: id>",views.destroy, name="destroy"),
]