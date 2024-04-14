from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
# def index(request):
#     return HttpResponse('Hello, world')


#Rendering an HTML page | Template

def indexView(request):
    template =loader.get_template('index.html')
    return HttpResponse(template.render())