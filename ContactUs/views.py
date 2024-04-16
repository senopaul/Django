from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . models import ContactUs
# from ContactUs.models import ContactUs | this does same as above in 3
# Create your views here.

def ContactUsView(request):
    # if request.method == 'POST':
    #     newname= request.POST['name']
    #     add_name = ContactUs(name= new_name)
    #     add_name.save()
        
    #     # print(contact)
    # all_contact = ContactUs.objects.all() |#this gets everything in the db and put in the all to do
    # # print(all_contact) 
    template = loader.get_template('contactus.html')
    return HttpResponse(template.render())

