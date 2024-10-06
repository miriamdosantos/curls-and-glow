from django.contrib import admin

# Register your models here.
from .models import Offer, Booking, Testimonial

# Register the Offer model with the admin site.
admin.site.register(Offer)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Booking models.
    
    Attributes:
        list_display (tuple): Fields to be displayed in the list view.
        list_filter (tuple): Fields that can be used to filter the list.
        search_fields (tuple): Fields that can be searched.
        ordering (tuple): Default ordering of the displayed bookings.
    """
    list_display = (
        "full_name",
        "email",
        "service",
        "stylish",
        "date_time",
        "status",
        "created_on",
    )  # Campos a serem exibidos na lista
    list_filter = (
        "status",
        "service",
        "date_time",
    )  # Adiciona filtros na barra lateral
    search_fields = ("full_name", "email")  # Campos pesquisáveis
    ordering = ("-created_on",)  # Ordenação padrão


@admin.register(Testimonial)
class StylishAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Testimonial models.
    
    Attributes:
        list_display (tuple): Fields to be displayed in the list view.
    """
    list_display = ("booking", "rating", "message", "created_at")  # Campos a serem exibidos na lista
