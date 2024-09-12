from django.shortcuts import render
from apps.booking.models import Offer

# Create your views here.
def home (request):
    offers = Offer.objects.all()
    context ={
        'offers':offers
    }
    
    return render(request, 'services/index.html', context)