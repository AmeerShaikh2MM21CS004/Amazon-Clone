from django.db import models

# Create your models here.
class Footer_Block(models.Model):
    Heading=models.CharField(max_length=50,blank=True)
    Desc=models.CharField(max_length=255,blank=True)