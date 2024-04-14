from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def AccountsView(request):
    template = loader.get_template('accounts.html')
    return HttpResponse(template.render())

def registerView(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())

def loginView(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())