from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . models import *
from django.contrib.auth.decorators import login_required 

# Create your views here.

def ContactUsView(request):
    allContact = ContactUs.objects.all()
    if request.method == 'POST':
        new_contact= request.POST['name']
        new_email = request.POST['email']
        new_phone = request.POST['phone']
        new_message = request.POST['message']
        context = {
            'new_contact':new_contact,
            'new_email':new_email,
            'new_phone':new_phone,
            'new_message':new_message,
            
        }
        context.save()
        
        
    def addContact(request):
        template = loader.get_template('add.html')
        return HttpResponse(template.render())
    
    @login_required    
    def about(request):
        template = loader.get_template('about.html')
        return HttpResponse(template.render())
    
    
    
    
    
    def updateContact(request):
        template = loader.get_template('update.html')
        return HttpResponse(template.render())
    
    
    
    
    
    
    
    
    def deleteContact(request):
        template = loader.get_template('delete.html')
        return HttpResponse(template.render())
        
        # add_name = ContactUs({'name':new_contact,'email':new_email,'phone':new_phone,'content':new_content}),
        # add_name.save()
        
    
    # if request.method == 'POST':
    #     new_contact= request.POST['name']
    #     add_contact = ContactUs({'name':'new_contact'}),
    #     add_contact.save()
        
        

    template = loader.get_template('contactus.html')
    return HttpResponse(template.render(context={'allContact':allContact}))



#.15 =|#this gets everything in the db and put in the all to do print(all_contact) 
# from ContactUs.models import ContactUs | another way of achieving number 4 above
    