from django.db import models

# Create your models here.

class Post(models.Model): # Two fields
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    #If we wanted to use a regular file here the only difference 
    # will be to change ImageField to FileField.

    #The location of the uploaded image will be in MEDIA_ROOT/images. 
    # In Django, the MEDIA_ROOT setting is where we define the location of all 
    # user uploaded items.

   # def __str__(self): 
     #   return self.title
# a __str__ method so that the title appears in our Django admin later on
