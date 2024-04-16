from django.db import models


# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=50 ,null=False,blank=False,default='0')
    email = models.EmailField(max_length=50 ,null=False,blank=False,default='0')
    phone = models.CharField(max_length=10,null=False,blank=False,default='0')
    content = models.TextField(max_length=100,null=False,blank=False,default='0')
    date = models.DateTimeField(auto_now_add=True)