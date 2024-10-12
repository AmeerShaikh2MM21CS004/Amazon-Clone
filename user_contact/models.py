from django.db import models

# Create your models here.

class UseerDetails(models.Model):
    username=models.CharField(max_length=50,blank=True)
    password=models.CharField(max_length=50,blank=True)