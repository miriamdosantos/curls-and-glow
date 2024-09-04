from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Offer, Booking, Testimonial
# Register your models here.

admin.site.register(Offer)
admin.site.register(Booking)
@admin.register(Testimonial)
class StylishAdmin(admin.ModelAdmin):
    list_display = ('booking', 'rating','message',  'created_at')
