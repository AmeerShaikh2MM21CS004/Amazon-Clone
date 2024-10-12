from django.db import models

# Create your models here.

class Shopping_section(models.Model):
     category_name=models.CharField(max_length=50,blank=True)
     shop_categ_img=models.FileField(upload_to='shopping_category/',max_length=500,blank=True,null=True,default=None)