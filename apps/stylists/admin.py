from django.contrib import admin
from .models import Stylist, Availability
# Register your models here.
@admin.register(Stylist)
class StylishAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')

@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ('day_of_week', 'start_time', 'end_time')