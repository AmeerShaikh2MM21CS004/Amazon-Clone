from django.contrib import admin
from amazon_footer_data.models import Footer_Block
# Register your models here.

class AdminFooterBlock1(admin.ModelAdmin):
    list_dislpay=('Heading','Desc')

admin.site.register(Footer_Block,AdminFooterBlock1)  

