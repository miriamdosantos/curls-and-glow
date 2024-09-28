from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from datetime import datetime, timedelta
from apps.services.models import Service
from apps.stylists.models import Stylist, Availability
from .models import Booking
def make_appointment (request):
    stylists = Stylist.objects.all()

    context = {
        'stylists': stylists
    }

    return render(request, 'booking/booking.html', context)

def select_date(request):
    services = Service.objects.all()
    
    if request.method == "POST":
        selected_stylist_id = request.POST.get("selected_stylist_id")
        selected_date = request.POST.get("date")

        # Check if the date was provided
        if not selected_date:
            messages.error(request, "Please select a date.")
            return redirect('make_appointment')  # Redirects to the appointment page

        selected_date_obj = datetime.strptime(selected_date, '%Y-%m-%d')  # Convert date string to datetime object
        day_of_week_name = selected_date_obj.strftime('%A')  # Get the day of the week

        # Filter available slots based on stylist selection
        if selected_stylist_id:
            # If a stylist was selected, filter by stylist
            stylist_id = int(selected_stylist_id)
            available_slots = Availability.objects.filter(stylist__id=stylist_id, day_of_week=day_of_week_name)
            booked_slots = Booking.objects.filter(stylish__id=stylist_id, date_time__date=selected_date_obj)
        else:
            # If no stylist is selected, get all available slots for the day
            available_slots = Availability.objects.filter(day_of_week=day_of_week_name)
            booked_slots = Booking.objects.filter(date_time__date=selected_date_obj)

        # Prepare to find free slots
        default_duration = timedelta(hours=2)  # Default duration of 2 hours
        free_slots = []  # List to store available times

        # Loop through available slots to determine free times
        for availability in available_slots:
            current_time = datetime.combine(selected_date_obj, availability.start_time)
            end_time = datetime.combine(selected_date_obj, availability.end_time)

            while current_time + default_duration <= end_time:
                # Check if the time slot is booked
                is_booked = booked_slots.filter(date_time__time=current_time.time()).exists()

                if not is_booked:
                    free_slots.append(current_time.time())  # Add only the time if not booked

                current_time += timedelta(minutes=30)  # Increment by 30 minutes

        # Prepare context for rendering
        context = {
            'selected_date': selected_date,
            'selected_stylist_id': selected_stylist_id,
            'available_times': free_slots,
            'services': services
        }

        return render(request, 'booking/select_time.html', context)

    return redirect('booking') 