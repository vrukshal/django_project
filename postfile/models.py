from django.db import models

# Create your models here.
class PostFile1(models.Model): # Two fields
    title = models.TextField()
    cover = models.FileField(upload_to='files/')
