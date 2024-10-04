from django.contrib import admin
from .models import UserProfile
from apps.booking.models import Booking, Testimonial
from apps.contact.models import ContactMessage

# Register your models here.
class BookingInline(admin.TabularInline):
    model = Booking
    extra = 0  # Número de formulários extras a serem exibidos

class ContactMessageInline(admin.TabularInline):
    model = ContactMessage
    extra = 0

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ( 'user_display','phone_number') 
    inlines = [BookingInline, ContactMessageInline]

    def user_display(self, obj):
        return f"{obj.user.username} ({obj.user.email})"
    user_display.short_description = 'User Info'

    