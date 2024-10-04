from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Offer, Booking, Testimonial
# Register your models here.

admin.site.register(Offer)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'service', 'stylish', 'date_time', 'status', 'created_on')  # Campos a serem exibidos na lista
    list_filter = ('status', 'service', 'date_time')  # Adiciona filtros na barra lateral
    search_fields = ('full_name', 'email')  # Campos pesquisáveis
    ordering = ('-created_on',)
@admin.register(Testimonial)
class StylishAdmin(admin.ModelAdmin):
    list_display = ('booking', 'rating','message',  'created_at')
