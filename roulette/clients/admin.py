from django.contrib import admin
from .models import Client

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    '''Admin View for Client'''

    list_display = ('name', 'email', 'fone')
    list_filter = ('name', 'email', 'fone')
    search_fields = ('name', 'email', 'fone')
    date_hierarchy = 'created_at'
    ordering = ('created_at',)