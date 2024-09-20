from django.contrib import admin
from .models import ContactMessage
# Register your models here.
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'status', 'response')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')