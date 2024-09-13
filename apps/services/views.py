from django.shortcuts import render
from apps.booking.models import Offer
from apps.services.models import Service

# Create your views here.
def home (request):
    offers = Offer.objects.all()
    services = Service.objects.all().order_by('title')
    context ={
        'offers':offers,
        'services':services
    }
    
    return render(request, 'services/index.html', context)