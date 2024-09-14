from django.shortcuts import render
from apps.booking.models import Offer, Testimonial, Booking
from apps.services.models import Service
from apps.stylists.models import Stylist

# Create your views here.
def home (request):
    offers = Offer.objects.all()
    services = Service.objects.all().order_by('title')
    stylists = Stylist.objects.all
    testimonials = Testimonial.objects.all()
    bookings = Booking.objects.all()
    context ={
        'offers':offers,
        'services':services,
        'stylists': stylists,
        'testimonials': testimonials, 
        'bookings': bookings
    }
    
    return render(request, 'services/index.html', context)

def services (request):
    services = Service.objects.all().order_by('title')

    context = {
        'services': services
    }
    return render (request, 'services/services.html', context)
