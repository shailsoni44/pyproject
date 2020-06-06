"""pyproject20 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
# from firstapp import views
from rest_framework import routers
from firstapp import views

router = routers.DefaultRouter()
router.register(r'registerapi',views.RegisterViewSet)
router.register(r'signupapi',views.SignupViewSet)
router.register(r'sessionapi',views.SessionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    #1 url
    #2 file
    # path("",views.home, name="home"),
    # path("about",views.about),
    # path("contact_us",views.contacts, name="contact"),
    path("firstapp/", include("firstapp.urls")),
    path('', include(router.urls)),
]
