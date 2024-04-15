from django.db import models

# Create your models here.
class MyBlog(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=50)
    image =models.TextField()
    views = models.IntegerField(default=7)
    
    
    
    #Commands
    # -python manage.py makemigrations | blog ...(if there are many models in the project, add a name after make migrations)
    # -python manage.py migrate ...send the models to the database