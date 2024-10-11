from django.contrib import admin
from amazon_service_footer.models import Service

class ServiceSection1(admin.ModelAdmin):
    list_display=('get_to_know_us','make_money_with_us','amazon_payment_products','let_us_help_you')



admin.site.register(Service,ServiceSection1)    