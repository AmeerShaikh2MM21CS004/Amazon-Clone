from django.contrib import admin
from shopping_category.models import Shopping_section

# Register your models here.

class AdminShoppingDetailsBlock(admin.ModelAdmin):
    list_display=('category_name','shop_categ_img')

admin.site.register(Shopping_section,AdminShoppingDetailsBlock)    