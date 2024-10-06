from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.views.generic.edit import UpdateView
from django.utils import timezone

from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from datetime import datetime, timedelta
from django.utils import timezone
from django.urls import reverse_lazy
from dateutil import parser  # Import parser from the dateutil library
from datetime import datetime, timedelta
from apps.services.models import Service
from apps.stylists.models import Stylist, Availability
from apps.users.models import UserProfile
from .models import Booking, Offer, Testimonial
from apps.users.models import UserProfile
from .forms import TestimonialForm


# Helper function to calculate free booking slots based
# on availability and existing bookings
def get_free_slots(
    selected_date_obj,
    available_slots,
    booked_slots,
    duration_if_booked=timedelta(hours=2),
    interval_if_free=timedelta(minutes=30),
):
    """
    Find free time slots by checking available and booked slots
    for a given stylist and date.

    Parameters:
    - selected_date_obj (datetime): The date selected for the booking.
    - available_slots (QuerySet):
    Availability slots for the stylist on the selected day.
    - booked_slots (QuerySet):
    Existing bookings for the stylist on the selected day.
    - duration_if_booked (timedelta):
    The duration to skip if a slot is booked (default 2 hours).
    - interval_if_free (timedelta):
    The interval between free slots (default 30 minutes).

    Returns:
    - free_slots (list): List of free time slots for booking.
    """
    free_slots = []

    # Get the current time for comparison
    now = datetime.now()

    # Iterate through each availability slot
    for availability in available_slots:
        current_time = datetime.combine(selected_date_obj, availability.start_time)
        end_time = datetime.combine(selected_date_obj, availability.end_time)

        # Calculate the last available time for booking (1 hour before the end
        # of availability)
        last_booking_time = end_time - timedelta(hours=1)

        # Start from the availability start time
        while current_time < end_time:
            # If we're on the current day and current_time is in the past, skip
            # it
            if selected_date_obj.date() == now.date() and current_time < now:
                current_time += interval_if_free
                continue

            # Check if the time slot is already booked
            is_booked = booked_slots.filter(
                date_time__time=current_time.time()
            ).exists()

            # Add the time to free_slots if not booked and before the last
            # booking time
            if not is_booked and current_time <= last_booking_time:
                free_slots.append(current_time.time())  # Append the free slot

            # Skip to the next slot based on booking or availability
            if is_booked:
                current_time += duration_if_booked  # If booked, skip by 2 hours
            else:
                current_time += (
                    interval_if_free  # Otherwise, move to the next slot in 30 minutes
                )

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
    context = {"stylists": stylists}
    return render(request, "booking/booking.html", context)


# View to select a booking date and show available time slots
def select_date(request):
    """
    Handle the date selection for booking and display available time slots
    based on stylist availability.

    Parameters:
    - request (HttpRequest): The incoming request.

    Returns:
    - HttpResponse: Renders the 'select_time.html' template with available time slots.
    If no date is selected or there is an error, it redirects back to the booking page.
    """
    # Retrieve all available services
    services = Service.objects.all()

    # Check if the request method is POST
    if request.method == "POST":
        # Get the selected stylist ID from the POST data
        selected_stylist_id = request.POST.get("selected_stylist_id")
        # Get the selected date from the POST data
        selected_date = request.POST.get("date-calendar")

        # Validate selected date
        if not selected_date:
            messages.error(request, "No date selected. Please select a valid date.")
            return redirect("booking")

        # Attempt to convert the selected date string into a datetime object
        try:
            selected_date_obj = datetime.strptime(selected_date, "%Y-%m-%d")
        except ValueError:
            messages.error(request, "Invalid date format. Please try again.")
            return redirect("booking")

        # Get the name of the day of the week for the selected date
        day_of_week_name = selected_date_obj.strftime("%A")

        # Fetch availability slots and booked slots based on stylist selection
        if selected_stylist_id == "":
            # When no stylist is selected, fetch all available stylists
            available_slots = Availability.objects.filter(day_of_week=day_of_week_name)
            booked_slots = Booking.objects.filter(date_time__date=selected_date_obj)

            # Get all stylists available for the selected date
            stylists = Stylist.objects.all()
            all_free_slots = []

            # Iterate through each stylist to find their free slots
            for stylist in stylists:
                # Filter available and booked slots for the current stylist
                stylist_available_slots = available_slots.filter(stylist=stylist)
                stylist_booked_slots = booked_slots.filter(stylish=stylist)
                # Get the free slots for the current stylist using a helper
                # function
                free_slots_for_stylist = get_free_slots(
                    selected_date_obj, stylist_available_slots, stylist_booked_slots
                )
                # Collect all free slots
                all_free_slots.extend(free_slots_for_stylist)

            # Format available slots for display, removing duplicates and
            # sorting
            # Remove duplicates and sort
            formatted_slots = sorted(set(all_free_slots))

        else:
            # If a stylist is selected, fetch their availability and bookings
            stylist_id = int(selected_stylist_id)
            available_slots = Availability.objects.filter(
                stylist__id=stylist_id, day_of_week=day_of_week_name
            )
            booked_slots = Booking.objects.filter(
                stylish__id=stylist_id, date_time__date=selected_date_obj
            )

            # Get free slots using the helper function
            free_slots = get_free_slots(
                selected_date_obj, available_slots, booked_slots
            )

            # Format available slots for display and sort them
            formatted_slots = sorted(free_slots)  # Sort

        # Convert time slots to the desired format (AM/PM) and ensure correct
        # order
        formatted_time_slots = [time.strftime("%I:%M %p") for time in formatted_slots]

        # Prepare the context for rendering the template
        context = {
            "selected_date": selected_date,
            "selected_stylist_id": selected_stylist_id,
            "available_times": formatted_time_slots,
            "services": services,
        }

        # Render the 'select_time.html' template with the context
        return render(request, "booking/select_time.html", context)

    # Redirect back to the booking page if the request method is not POST
    return redirect("booking")


# View to finalize the a booking flow.


@login_required
def book_appointment(request):
    """
    Finalize the booking based on the selected date, time, and stylist.
    Create a booking record.

    Parameters:
    - request (HttpRequest): The incoming request containing form data for booking.

    Returns:
    - HttpResponseRedirect:
    Redirects to the booking confirmation page upon successful booking.
    If there's an error, redirects back to the date selection page.
    """
    # Check if the request method is POST
    if request.method == "POST":
        # Retrieve form data from the request
        # E.g., "09:00AM" or "07:30PM"
        selected_time = request.POST.get("time")
        selected_date = request.POST.get("selected_date")  # E.g., "Oct. 5, 2024"
        selected_stylist_id = request.POST.get("selected_stylist_id")
        selected_service_id = request.POST.get("service")
        coupon_code = request.POST.get("coupon")
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")

        # Normalize coupon code
        if coupon_code:
            coupon_code = coupon_code.strip().upper()

        # Retrieve the selected stylist and service using their IDs
        stylist = (
            get_object_or_404(Stylist, id=selected_stylist_id)
            if selected_stylist_id
            else None
        )
        service = get_object_or_404(Service, id=selected_service_id)

        # Validate the selected time and date
        if not selected_time or not selected_date:
            messages.error(request, "Selected time or date is empty.")
            return redirect("select_date")

        try:
            # Combine selected date and time into a datetime string and parse
            # it
            # E.g., "Oct. 5, 2024 09:00AM"
            combined_str = f"{selected_date} {selected_time}"
            selected_datetime = parser.parse(combined_str)
        except (ValueError, KeyError) as e:
            messages.error(request, f"Invalid date or time format: {e}")
            return redirect("select_date")

        # Check if the selected slot is already booked
        if Booking.objects.filter(
            stylish=stylist, date_time=selected_datetime
        ).exists():
            messages.error(request, "This time slot is already booked.")
            return redirect("select_date")

        # Retrieve the user's profile
        user_profile = get_object_or_404(UserProfile, user=request.user)

        # Check if a valid coupon code was provided
        offer_instance = None
        if coupon_code:
            try:
                offer_instance = Offer.objects.get(
                    code=coupon_code, end_date__gte=timezone.now()
                )
            except Offer.DoesNotExist:
                messages.error(request, "Invalid or expired coupon code.")
                return redirect("select_time")

        # Create the booking
        booking = Booking.objects.create(
            stylish=stylist,
            service=service,
            user_profile=user_profile,
            date_time=selected_datetime,
            offer=offer_instance,
            full_name=full_name,
            email=email,
        )

        # Redirect to the booking confirmation page
        return redirect("booking_confirmation", booking_id=booking.id)

    # Redirect back to the booking page if the request method is not POST
    return redirect("booking")


# View to display booking confirmation details


@login_required
def booking_confirmation(request, booking_id):
    """
    Display the booking confirmation page with the details of the appointment.

    Parameters:
    - request (HttpRequest): The incoming request.
    - booking_id (int): The ID of the confirmed booking.

    Returns:
    - HttpResponse: Renders the 'booking_confirmation.html'
    template with booking details.
    """
    # Retrieve the booking object based on the provided booking_id
    booking = get_object_or_404(Booking, id=booking_id)

    # Render the booking confirmation template with the booking details
    return render(
        request,
        "booking/booking_confirmation.html",
        {
            "selected_datetime": booking.date_time,
            "stylist": booking.stylish,
            "service": booking.service,
            "offer": booking.offer,
            "full_name": booking.full_name,
            "email": booking.email,
        },
    )


# View to display cards of all user's appointment and within option to:
# Edit; Delete and Leave a Testimonial
@login_required
def user_bookings(request):
    """
    Retrieve and display all bookings for the logged-in user.

    If there are completed bookings without testimonials, a success message is shown
    encouraging the user to leave a testimonial.

    Parameters:
    - request (HttpRequest): The incoming request from the user.

    Returns:
    - HttpResponse: Renders the 'user_bookings.html'
    template with the user's bookings.
    """
    # Retrieve the user profile associated with the logged-in user
    user_profile = get_object_or_404(UserProfile, user=request.user)

    # Fetch all bookings associated with the user's profile
    bookings = Booking.objects.filter(user_profile=user_profile)

    # Initialize a flag to control if the testimonial message has been shown
    testimonial_message_shown = False

    # Loop through each booking to check for completed status
    for booking in bookings:
        # Check if the booking is completed and if a testimonial has not been left
        if (booking.status == "Completed" and not Testimonial.objects.filter(booking=booking).exists() and not testimonial_message_shown):
            # Show a success message encouraging the user to leave a testimonial
            messages.success(
                request,
                f"Booking for {booking.service.title} with {booking.stylish} is complete! You can now leave a testimonial.",
            )
            testimonial_message_shown = True  # Mark that the message has been shown

    # Render the user bookings template with the user's bookings
    return render(request, "booking/user_bookings.html", {"bookings": bookings})


# View to delete booking


@login_required
def delete_appointment(request, booking_id):
    """
    Handle the deletion of a booking appointment.
    This view confirms the deletion of a booking and removes it from the database
    if the user confirms the action. A success message is displayed upon successful
    deletion.

    Parameters:
    - request (HttpRequest): The incoming request from the user.
    - booking_id (int): The ID of the booking to be deleted.

    Returns:
    - HttpResponseRedirect:
    Redirects to the user's bookings page after successful deletion.
    - HttpResponse:
    Renders the confirmation page for deletion if the request method is not POST.
    """
    # Retrieve the booking associated with the provided booking ID
    booking = get_object_or_404(Booking, id=booking_id)

    # Check if the request method is POST for deletion confirmation
    if request.method == "POST":
        # Update the booking status to 'Cancelled' (this line has a typo, see
        # note below)
        booking.status = "Cancelled"  # Corrected from '==' to '=' for assignment
        booking.delete()  # Delete the booking record
        # Show success message
        messages.success(request, "Booking deleted successfully!")
        # Redirect to the user's bookings page
        return redirect("user_bookings")

    # Render the confirmation page for deletion
    return render(request, "booking/confirm_delete.html", {"booking": booking})


# View to update booking (edit button)
class BookingUpdateView(LoginRequiredMixin, UpdateView):
    """
    View to update a booking appointment.

    This view allows logged-in users to modify the details of their existing bookings.
    Upon successful update, the booking status is set to 'Updated'
     and a success message is displayed.

    Attributes:
    - model (Booking): The model associated with this view.
    - fields (list): The fields to be displayed in the update form.
    - template_name_suffix (str): Suffix for the template name, indicating this is an update form.
    """

    model = Booking
    fields = ["full_name", "email", "date_time", "service", "stylish"]
    template_name_suffix = "_update_form"

    def form_valid(self, form):
        """
        Handle the form submission when it is valid.

        This method is called when the submitted form passes validation.
        It updates the booking status and displays a success message.

        Parameters:
        - form (Form): The valid form instance containing the booking data.

        Returns:
        - HttpResponse: Redirects to the success URL after saving the updated booking.
        """
        response = super().form_valid(
            form
        )  # Calls the super class method to save the form
        self.object.status = "Updated"  # Update the booking status to 'Updated'
        self.object.save()  # Save the changes to the database
        # Add a success message
        messages.success(self.request, "Booking updated successfully!")
        return response

    def get_success_url(self):
        """
        Determine the URL to redirect to after a successful form submission.

        Returns:
        - str: The URL to redirect to, which is the user's bookings page.
        """
        return reverse_lazy("user_bookings")  # Redirect to the user's bookings page


@login_required
def leave_testimonial(request, booking_id):
    """
    Handle the submission of a testimonial for a specific booking.

    This view allows logged-in users to leave a testimonial for their completed booking.
    It processes both GET and POST requests.

    Parameters:
    - request (HttpRequest):
    The incoming request containing form data or for rendering the form.
    - booking_id (int):
    The ID of the booking for which the testimonial is being submitted.

    Returns:
    - HttpResponse:
    Renders the testimonial form or redirects upon successful submission.
    """
    # Retrieve the booking object based on the provided booking ID
    booking = get_object_or_404(Booking, pk=booking_id)

    if request.method == "POST":
        # Create a new testimonial form instance with the submitted data
        # Use the form to handle the data
        form = TestimonialForm(request.POST, request.FILES)

        if form.is_valid():
            # Save the new testimonial without committing to the database yet
            # Don't save yet, as we need to associate the booking
            new_testimonial = form.save(commit=False)
            new_testimonial.booking = (
                booking  # Associate the testimonial with the booking
            )
            new_testimonial.save()  # Save the testimonial

            # Show a success message upon successful submission
            messages.success(
                request, "Your testimonial has been successfully submitted!"
            )
            # Redirect to the user's bookings page after success
            return redirect("user_bookings")
        else:
            # Show an error message if the form contains errors
            messages.error(request, "Please correct the errors in the form.")
    else:
        # Initialize an empty form for the GET request
        form = TestimonialForm()

    # Render the testimonial form template with the booking and form context
    return render(
        request,
        "testimonial/leave_testimonial.html",
        {"booking": booking, "form": form},
    )
