from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from apps.booking.forms import BookingForm
from apps.users.models import UserProfile
from apps.stylists.models import Stylist
def make_appointment (request):
    stylists = Stylist.objects.all()

    context = {
        'stylists': stylists
    }

    return render(request, 'booking/booking.html', context)
