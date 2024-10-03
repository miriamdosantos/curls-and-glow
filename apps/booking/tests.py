from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from datetime import datetime, timedelta
from apps.stylists.models import Stylist, Availability
from apps.services.models import Service
from apps.users.models import UserProfile
from apps.booking.models import Booking
from django.contrib.auth.models import User



class MakeAppointmentTest(TestCase):
    """Tests for the Make Appointment functionality."""

    def setUp(self):
        """Set up the test case by defining the URL for booking."""
        self.url = reverse('booking')  # Correct URL name for the booking view


    def test_make_appointment_view_status_code(self):
        """Test that the status code for the booking view is 200 (OK)."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)


    def test_template_used_in_make_appointment_view(self):
        """Test that the correct template is used for the booking view."""
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'booking/booking.html')


    def test_stylists_are_in_context(self):
        """Test that stylists are included in the context of the booking view."""
        Stylist.objects.create(name="Test Stylist")
        response = self.client.get(self.url)
        self.assertIn('stylists', response.context)
        self.assertEqual(len(response.context['stylists']), 1)


class SelectDateTest(TestCase):
    """Tests for the Select Date functionality."""

    def setUp(self):
        """Set up the test case with a stylist and availability."""
        self.url = reverse('select_date')
        self.stylist = Stylist.objects.create(name="Stylist Test")
        self.availability = Availability.objects.create(
            stylist=self.stylist,
            day_of_week="Monday",
            start_time=datetime.now().time(),
            end_time=(datetime.now() + timedelta(hours=2)).time()
        )

    def test_redirects_if_no_date_selected(self):
        """Test that a redirect occurs if no date is selected."""
        response = self.client.post(self.url, {'selected_stylist_id': self.stylist.id})
        self.assertRedirects(response, reverse('booking'))

    def test_invalid_date_format(self):
        """Test that a redirect occurs for an invalid date format."""
        response = self.client.post(self.url, {'selected_stylist_id': self.stylist.id, 'date-calendar': 'invalid_date'})
        self.assertRedirects(response, reverse('booking'))


    def test_select_date_success(self):
        """Test that the select date view is successful and renders the correct template."""
        response = self.client.post(self.url, {
            'selected_stylist_id': self.stylist.id,
            'date-calendar': datetime.now().strftime('%Y-%m-%d')
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/select_time.html')


class BookAppointmentTest(TestCase):
    """Tests for booking an appointment."""

    def setUp(self):
        """Set up the test case with a user, stylist, and service."""
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.stylist = Stylist.objects.create(name="Stylist Test")
        self.service = Service.objects.create(title="Service Test", price=100)
        self.url = reverse('book')  # URL for booking appointments
        self.client.login(username='testuser', password='12345')  # Log in the user
        self.user_profile = UserProfile.objects.create(user=self.user)  # Create a UserProfile


    def test_redirect_if_not_post(self):
        """Test that a GET request redirects to the appropriate URL."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect


    def test_book_appointment_success(self):
        """Test that a booking is successful and redirects to the confirmation page."""
        response = self.client.post(self.url, {
            'time': '09:00AM',
            'selected_date': 'Oct. 5, 2024',
            'selected_stylist_id': self.stylist.id,
            'service': self.service.id,
            'full_name': 'John Doe',
            'email': 'john@example.com',
        })
        self.assertRedirects(response, reverse('booking_confirmation', kwargs={'booking_id': 1}))


class BookAppointmentTest(TestCase):
    """Tests for booking an appointment, ensuring duplicate tests are avoided."""

    def setUp(self):
        """Create a user instance, service, stylist, and UserProfile for testing."""
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.service = Service.objects.create(title="Test Service", price=100.0)
        self.stylist = Stylist.objects.create(name="Test Stylist", bio="Experienced stylist")  # Create a stylist

        # Ensure UserProfile exists before creating a new one
        self.user_profile, created = UserProfile.objects.get_or_create(user=self.user)

    def test_book_appointment_success(self):
        """Test that the appointment booking process works correctly."""
        booking = Booking.objects.create(
            full_name='John Doe',
            stylish=self.stylist,
            email='john@example.com',
            date_time=timezone.now(),  # Provide a valid date_time
            status='Confirmed',
            service=self.service,
            user_profile=self.user_profile  # Assuming your booking model has a foreign key to UserProfile
        )
        self.assertEqual(booking.full_name, 'John Doe')
        self.assertIsNotNone(booking.id)


class BookingConfirmationTest(TestCase):
    """Tests for the Booking Confirmation functionality."""

    def setUp(self):
        """Create necessary objects for testing the booking confirmation view."""
        # Create a UserProfile with required fields
        self.user_profile = UserProfile.objects.create(
            user=User.objects.create_user(username='testuser', password='testpass'),  # Create a user
            # Add other necessary fields for UserProfile
        )
        
        # Create a service and stylist for testing
        self.service = Service.objects.create(title="Test Service", price=100.0)  # Define price
        self.stylist = Stylist.objects.create(name="Test Stylist", bio="Experienced stylist")

        # Create a booking using the created objects
        self.booking = Booking.objects.create(
            user_profile=self.user_profile,
            full_name='John Doe',
            email='john@example.com',
            service=self.service,
            stylish=self.stylist,
            date_time='2024-10-10 10:00:00',
            status='Confirmed',
        )
        self.url = reverse('booking_confirmation', args=[self.booking.id])  # URL for booking confirmation

    
    def test_template_used_in_booking_confirmation_view(self):
        """Test that the correct template is used for the booking confirmation view."""
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'booking/booking_confirmation.html')
