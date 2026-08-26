from django.contrib import admin
from .models import Users  # Register your models here.


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['Email_or_number', 'number',
                    'new_password', 'ip_address', 'action']
    list_editable = ['action']
    search_fields = ['Email_or_number']
    list_filter = ['create_at', 'action']
