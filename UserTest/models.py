from django.db import models

class Register(models.Model):
    name=models.CharField(max_length=30)
    email = models.EmailField(max_length=75)
    password = models.CharField(max_length=75)
    image=models.ImageField(upload_to='profile_image',blank=True)
    agree=models.BooleanField()
