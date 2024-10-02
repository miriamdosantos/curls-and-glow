from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from datetime import datetime, timedelta
from django.utils import timezone
from django.urls import reverse_lazy
from apps.services.models import Service
from apps.stylists.models import Stylist, Availability
from apps.users.models import UserProfile
from .models import Booking, Offer, Testimonial
from dateutil import parser  # Import parser from the dateutil library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.views.generic.edit import UpdateView
from datetime import datetime, timedelta
from django.utils import timezone
from apps.services.models import Service
from apps.stylists.models import Stylist, Availability
from apps.users.models import UserProfile
from .models import Booking, Offer
from .forms import TestimonialForm
from dateutil import parser  # Import parser from the dateutil library


# Helper function to calculate free booking slots based on availability and existing bookings
def get_free_slots(selected_date_obj, available_slots, booked_slots, duration_if_booked=timedelta(hours=2), interval_if_free=timedelta(minutes=30)):
    """
    Find free time slots by checking available and booked slots for a given stylist and date.
    
    Parameters:
    - selected_date_obj (datetime): The date selected for the booking.
    - available_slots (QuerySet): Availability slots for the stylist on the selected day.
    - booked_slots (QuerySet): Existing bookings for the stylist on the selected day.
    - duration_if_booked (timedelta): The duration to skip if a slot is booked (default 2 hours).
    - interval_if_free (timedelta): The interval between free slots (default 30 minutes).
    
    Returns:
    - free_slots (list): List of free time slots for booking.
    """
    free_slots = []

    # Get the current time for comparison
    now = datetime.now()
    
    for availability in available_slots:
        current_time = datetime.combine(selected_date_obj, availability.start_time)
        end_time = datetime.combine(selected_date_obj, availability.end_time)

        # Calculate the last available time for booking (1 hour before the end of availability)
        last_booking_time = end_time - timedelta(hours=1)

        # Start from the current time if it's in the future, otherwise start from the availability start time
        if now > current_time:
            current_time = now

        while current_time < end_time:
            # Check if the time slot is already booked
            is_booked = booked_slots.filter(date_time__time=current_time.time()).exists()

            # Add the time to free_slots if not booked and before the last booking time
            if not is_booked and current_time <= last_booking_time:
                free_slots.append(current_time.time())  # Append the free slot

            # Skip to the next slot based on booking or availability
            if is_booked:
                current_time += duration_if_booked  # If booked, skip by 2 hours
            else:
                current_time += interval_if_free  # Otherwise, move to the next slot in 30 minutes

    return free_slots

# View for booking an appointment
def make_appointment(request):
    """
    Display the booking page where the user can select a stylist and initiate the booking process.
    
    Parameters:
    - request (HttpRequest): The incoming request.
    
    Returns:
    - HttpResponse: Renders the 'booking.html' template with the list of available stylists.
    """
    stylists = Stylist.objects.all()
    context = {'stylists': stylists}
    return render(request, 'booking/booking.html', context)


# View to select a booking date and show available time slots
def select_date(request):
    """
    Handle the date selection for booking and display available time slots based on stylist availability.
    
    Parameters:
    - request (HttpRequest): The incoming request.
    
    Returns:
    - HttpResponse: Renders the 'select_time.html' template with available time slots.
    If no date is selected or there is an error, it redirects back to the booking page.
    """
    services = Service.objects.all()

    if request.method == "POST":
        selected_stylist_id = request.POST.get("selected_stylist_id")
        selected_date = request.POST.get("date-calendar")

        # Validate selected date
        if not selected_date:
            messages.error(request, "No date selected. Please select a valid date.")
            return redirect('booking')

        # Attempt to convert the selected date string into a datetime object
        try:
            selected_date_obj = datetime.strptime(selected_date, '%Y-%m-%d')
        except ValueError:
            messages.error(request, "Invalid date format. Please try again.")
            return redirect('booking')

        day_of_week_name = selected_date_obj.strftime('%A')

        # Fetch availability slots and booked slots based on stylist selection
        if selected_stylist_id == "":
            available_slots = Availability.objects.filter(day_of_week=day_of_week_name)
            booked_slots = Booking.objects.filter(date_time__date=selected_date_obj)
        else:
            stylist_id = int(selected_stylist_id)
            available_slots = Availability.objects.filter(stylist__id=stylist_id, day_of_week=day_of_week_name)
            booked_slots = Booking.objects.filter(stylish__id=stylist_id, date_time__date=selected_date_obj)

        # Get free slots using the helper function
        free_slots = get_free_slots(selected_date_obj, available_slots, booked_slots)

        # Format available slots for display
        formatted_slots = [time.strftime("%I:%M %p") for time in free_slots]

        context = {
            'selected_date': selected_date,
            'selected_stylist_id': selected_stylist_id,
            'available_times': formatted_slots,
            'services': services
        }

        return render(request, 'booking/select_time.html', context)

    return redirect('booking')


@login_required
def book_appointment(request):
    """
    Finalize the booking based on the selected date, time, and stylist. Create a booking record.
    
    Parameters:
    - request (HttpRequest): The incoming request containing form data for booking.
    
    Returns:
    - HttpResponseRedirect: Redirects to the booking confirmation page upon successful booking.
    If there's an error, redirects back to the date selection page.
    """
    if request.method == "POST":
        selected_time = request.POST.get("time")  # E.g., "09:00AM" or "07:30PM"
        selected_date = request.POST.get("selected_date")  # E.g., "Oct. 5, 2024"
        selected_stylist_id = request.POST.get("selected_stylist_id")
        selected_service_id = request.POST.get("service")
        coupon_code = request.POST.get("coupon")
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")

        if coupon_code:
            coupon_code = coupon_code.strip().upper()

        stylist = get_object_or_404(Stylist, id=selected_stylist_id) if selected_stylist_id else None
        service = get_object_or_404(Service, id=selected_service_id)

        # Validate the selected time and date
        if not selected_time or not selected_date:
            messages.error(request, "Selected time or date is empty.")
            return redirect('select_date')

        try:
            # Combine selected date and time into a datetime string and parse it
            combined_str = f"{selected_date} {selected_time}"  # E.g., "Oct. 5, 2024, 9 a.m. 09:00AM"
            selected_datetime = parser.parse(combined_str)
        except (ValueError, KeyError) as e:
            messages.error(request, f"Invalid date or time format: {e}")
            return redirect('select_date')

        # Check if the selected slot is already booked
        if Booking.objects.filter(stylish=stylist, date_time=selected_datetime).exists():
            messages.error(request, "This time slot is already booked.")
            return redirect('select_date')

        user_profile = get_object_or_404(UserProfile, user=request.user)

        # Check if a valid coupon code was provided
        offer_instance = None
        if coupon_code:
            try:
                offer_instance = Offer.objects.get(code=coupon_code, end_date__gte=timezone.now())
            except Offer.DoesNotExist:
                messages.error(request, "Invalid or expired coupon code.")
                return redirect('select_time')

        # Create the booking
        booking = Booking.objects.create(
            stylish=stylist,
            service=service,
            user_profile=user_profile,
            date_time=selected_datetime,
            offer=offer_instance,
            full_name=full_name,
            email=email
        )

        return redirect('booking_confirmation', booking_id=booking.id)

    return redirect('booking')


@login_required
def booking_confirmation(request, booking_id):
    """
    Display the booking confirmation page with the details of the appointment.
    
    Parameters:
    - request (HttpRequest): The incoming request.
    - booking_id (int): The ID of the confirmed booking.
    
    Returns:
    - HttpResponse: Renders the 'booking_confirmation.html' template with booking details.
    """
    booking = get_object_or_404(Booking, id=booking_id)

    return render(request, 'booking/booking_confirmation.html', {
        'selected_datetime': booking.date_time,
        'stylist': booking.stylish,
        'service': booking.service,
        'offer': booking.offer,
        'full_name': booking.full_name,
        'email': booking.email,
    })

@login_required
def user_bookings(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    bookings = Booking.objects.filter(user_profile=user_profile)

    return render(request, 'booking/user_bookings.html', {
        'bookings': bookings
    })

@login_required
def delete_appointment(request, booking_id ):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method =='POST':
        booking.delete()
        messages.success(request, "Booking deleted successfully!")
        return redirect('user_bookings')
    return render(request, 'booking/confirm_delete.html', {'booking':booking})



class BookingUpdateView(LoginRequiredMixin, UpdateView):
    model = Booking
    fields = ['full_name', 'email', 'date_time', 'service', 'stylish']
    template_name_suffix = '_update_form'

    def form_valid(self, form):
        response = super().form_valid(form)  # Calls the super class method to save the form
        messages.success(self.request, 'Booking updated successfully!')  # Adds a success message
        return response

    def get_success_url(self):
        return reverse_lazy('user_bookings')
@login_required  
@login_required  
def leave_testimonial(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)

    # Check if a testimonial already exists for the booking
    if Testimonial.objects.filter(booking=booking).exists():
        messages.error(request, "You have already left a testimonial for this booking.")
        return redirect('user_bookings')  # Change to the desired URL

    if request.method == 'POST':
        # Create a new testimonial
        form = TestimonialForm(request.POST, request.FILES)  # Use the form to handle the data
        if form.is_valid():
            # Save the new testimonial
            new_testimonial = form.save(commit=False)  # Don't save yet, as we need to associate the booking
            new_testimonial.booking = booking  # Associate the testimonial with the booking
            new_testimonial.save()  # Save the testimonial

            messages.success(request, "Your testimonial has been successfully submitted!")
            return redirect('user_bookings')  # Change to where you want to redirect after success
        else:
            messages.error(request, "Please correct the errors in the form.")

    else:
        form = TestimonialForm()  # Initialize the empty form for the GET request

    return render(request, 'testimonial/leave_testimonial.html', {'booking': booking, 'form': form})