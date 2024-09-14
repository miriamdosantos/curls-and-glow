from django.shortcuts import render
from apps.booking.models import Offer, Testimonial, Booking
from apps.services.models import Service
from apps.stylishs.models import Stylish

# Create your views here.
def home (request):
    offers = Offer.objects.all()
    services = Service.objects.all().order_by('title')
    stylishs = Stylish.objects.all
    testimonials = Testimonial.objects.all()
    bookings = Booking.objects.all()
    context ={
        'offers':offers,
        'services':services,
        'stylishs': stylishs,
        'testimonials': testimonials, 
        'bookings': bookings
    }
    
    return render(request, 'services/index.html', context)