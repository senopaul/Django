from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import MyBlog
# Create your views here.




#create a new blog
def blog(request):
    blog_all = MyBlog.objects.all()
    

def blogView(request):
    template = loader.get_template('blog.html')
    return HttpResponse(template.render())


#using the shell manage.py shell