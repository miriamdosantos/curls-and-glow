from django.contrib import admin
from .models import UserProfile
from apps.booking.models import Booking
from apps.contact.models import ContactMessage


# Register your models here.
class BookingInline(admin.TabularInline):
    """
    Inline class to manage Booking objects within UserProfile.

    Attributes:
        model (Booking): The Booking model.
        extra (int): Number of empty forms to display (default is 0).
    """

    model = Booking  # Booking model
    extra = 0  # Number of extra forms to display


class ContactMessageInline(admin.TabularInline):
    """
    Inline class to manage ContactMessage objects within UserProfile.

    Attributes:
        model (ContactMessage): The ContactMessage model.
        extra (int): Number of empty forms to display (default is 0).
    """

    model = ContactMessage  # ContactMessage model
    extra = 0  # Number of extra forms to display


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin class to manage UserProfile instances.

    Attributes:
        list_display (tuple): Fields to display in the admin list view.
        inlines (list): List of inline models to display.
    """

    list_display = (
        "user_display",
        "phone_number",
    )  # Fields displayed in the admin list
    inlines = [BookingInline, ContactMessageInline]  # Inline models

    def user_display(self, obj):
        """
        Returns a formatted string containing the username and email.

        Args:
            obj (UserProfile): The UserProfile instance.

        Returns:
            str: Formatted user info string.
        """
        return f"{obj.user.username} ({obj.user.email})"

    user_display.short_description = (
        "User Info"  # Column header for the user_display method
    )
