from django.shortcuts import render
from apps.booking.models import Offer
from apps.services.models import Service
from apps.stylishs.models import Stylish

# Create your views here.
def home (request):
    offers = Offer.objects.all()
    services = Service.objects.all().order_by('title')
    stylishs = Stylish.objects.all
    context ={
        'offers':offers,
        'services':services,
        'stylishs': stylishs
    }
    
    return render(request, 'services/index.html', context)