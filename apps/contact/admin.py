from django.contrib import admin
from .models import ContactMessage

# Register your models here.


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """
    Admin interface for managing ContactMessage instances.

    This class defines how ContactMessage entries are displayed
    in the Django admin panel, including the fields shown and filters
    available for searching and sorting.

    Attributes:
        list_display (tuple): Fields to display in the list view.
        list_filter (tuple): Fields to filter the list view.
        search_fields (tuple): Fields that can be searched in the list view.
    """

    list_display = (
        "name",
        "email",
        "subject",
        "created_at",
        "status",
        "response",
    )  # Fields displayed in the admin list view
    list_filter = ("status", "created_at")  # Filters available in the admin list view
    search_fields = (
        "name",
        "email",
        "subject",
        "message",
    )  # Fields that can be searched in the admin list view
