"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# from django.urls import path,include
from django.urls import path
from home.views import indexView
from aboutus.views import aboutusView
from ContactUs.views import ContactUsView
from Accounts.views import AccountsView
from blog.views import blogView

urlpatterns = [
    # path('',include('home.urls')),
    # path('about/',include('aboutus.urls')),
    path('',indexView,name='home'),
    path('aboutus/',aboutusView,name='aboutus'),
    path('contactus/',ContactUsView,name='contactsUs'),
    path('accounts/',AccountsView,name='Accounts'),
    path('blog/',blogView,name='blog'),
    
]
