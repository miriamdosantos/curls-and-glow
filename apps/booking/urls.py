from django.urls import path
from . import views  # Import views from the current directory (booking app)
from .views import BookingUpdateView

urlpatterns = [
    path(
        "confirmation/<int:booking_id>/",
        views.booking_confirmation,
        name="booking_confirmation",
    ),  # Confirmation page
    path(
        "", views.book_appointment, name="book_appointment"
    ),  # Final booking confirmation
    path(
        "delete-booking/<int:booking_id>/",
        views.delete_appointment,
        name="delete_appointment",
    ),
    path(
        "leave-testimonial/<int:booking_id>/",
        views.leave_testimonial,
        name="leave_testimonial",
    ),
    path(
        "make-booking/", views.make_appointment, name="booking"
    ),  # Page to start booking
    path("my_bookings/", views.user_bookings, name="user_bookings"),
    path(
        "select-time/", views.select_date, name="select_date"
    ),  # Page to select date and time
    path(
        "edit-booking/<int:pk>/", BookingUpdateView.as_view(), name="edit_appointment"
    ),
]
