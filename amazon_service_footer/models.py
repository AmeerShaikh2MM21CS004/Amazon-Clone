from django.db import models

# Create your models here.
class Service(models.Model):
    get_to_know_us = models.CharField(max_length=50, blank=True)
    make_money_with_us = models.CharField(max_length=50, blank=True)
    amazon_payment_products = models.CharField(max_length=50, blank=True)
    let_us_help_you = models.CharField(max_length=50, blank=True)
