from django.urls import path
from . import views  # Import views from the current directory (booking app)

urlpatterns = [
    path('confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),  # Confirmation page
    path('', views.book_appointment, name='book_appointment'),  # Final booking confirmation
    path('make-appointment/', views.make_appointment, name='booking'),  # Page to start booking
    path('select-date/', views.select_date, name='select_date'),  # Page to select date and time
    
]
