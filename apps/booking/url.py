from django.urls import path
from . import views  # Import views from the current directory (booking app)
from .views import BookingUpdateView
urlpatterns = [
    path('confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),  # Confirmation page
    path('', views.book_appointment, name='book_appointment'),  # Final booking confirmation
    path('delete-appointment/<int:booking_id>/', views.delete_appointment, name='delete_appointment'),
    path('make-appointment/', views.make_appointment, name='booking'),  # Page to start booking
    path('my_bookings/', views.user_bookings, name='user_bookings'),
    path('select-date/', views.select_date, name='select_date'),  # Page to select date and time
    path('edit-appointment/<int:pk>/', BookingUpdateView.as_view(), name='edit_appointment')
    
]
