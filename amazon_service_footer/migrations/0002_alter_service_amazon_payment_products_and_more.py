# Generated by Django 5.1.1 on 2024-10-12 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon_service_footer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='amazon_payment_products',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='service',
            name='get_to_know_us',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='service',
            name='let_us_help_you',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='service',
            name='make_money_with_us',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
