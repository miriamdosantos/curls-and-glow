from django.contrib import admin
from .models import Stylist, Availability


# Register your models here.
@admin.register(Stylist)
class StylistAdmin(admin.ModelAdmin):
    """
    Admin interface for the Stylist model.

    Attributes:
        list_display (tuple): Fields to display in the list view.
    """

    list_display = ("name", "bio")  # Fields to display in the list


@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    """
    Admin interface for the Availability model.

    Attributes:
        list_display (tuple): Fields to display in the list view.
    """

    list_display = (
        "day_of_week",
        "start_time",
        "end_time",
    )  # Fields to display in the list
