from django.contrib import admin
from user_contact.models import UseerDetails

# Register your models here.
class UserDetailsAdmin(admin.ModelAdmin):
        list_display=('username','password',)

admin.site.register(UseerDetails,UserDetailsAdmin)   
                   
