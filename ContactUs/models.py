from django.db import models
from django.db.models import

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=50 ,null=False,blank=False,default='0')
    email = models.EmailField(max_length=50 ,null=False)
    phone = models.CharField(max_length=10)
    content = models.TextField(max_length=)