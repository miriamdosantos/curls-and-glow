from django.shortcuts import render
from apps.booking.models import Offer, Testimonial, Booking
from apps.services.models import Service
from apps.stylists.models import Stylist


# Create your views here.
def home(request):
    """
    View for the home page that displays offers, services, stylists, testimonials, and bookings.

    Args:
        request: The HTTP request object.

    Returns:
        Rendered HTML page with the context data.
    """
    offers = Offer.objects.all()  # Fetch all offers
    services = Service.objects.all().order_by(
        "title"
    )  # Fetch and order all services by title
    stylists = Stylist.objects.all()  # Fetch all stylists
    testimonials = Testimonial.objects.all()  # Fetch all testimonials
    bookings = Booking.objects.all()  # Fetch all bookings

    context = {
        "offers": offers,
        "services": services,
        "stylists": stylists,
        "testimonials": testimonials,
        "bookings": bookings,
    }

    return render(request, "services/index.html", context)


def services(request):
    """
    View for the services page that displays all services.

    Args:
        request: The HTTP request object.

    Returns:
        Rendered HTML page with the context data containing services.
    """
    services = Service.objects.all().order_by(
        "title"
    )  # Fetch and order all services by title

    context = {"services": services}
    return render(request, "services/services.html", context)
