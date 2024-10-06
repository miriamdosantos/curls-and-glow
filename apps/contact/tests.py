from django.test import TestCase
from django.urls import reverse
from apps.contact.models import ContactMessage  # Ensure to import your model
from apps.users.models import UserProfile
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactViewsTests(TestCase):
    """Tests for the Contact views functionality."""

    def setUp(self):
        """Set up the test case by creating example data for the ContactMessage model and users."""
        self.staff_user = User.objects.create_user(
            username="staffuser", password="password123", is_staff=True
        )
        self.regular_user = User.objects.create_user(
            username="regularuser", password="password123", is_staff=False
        )

        self.user_profile, _ = UserProfile.objects.get_or_create(user=self.regular_user)

        # Create a ContactMessage instance for testing
        self.contact_message = ContactMessage.objects.create(
            user_profile=self.user_profile,
            name="Miriam",
            email="mii.santos@yahoo.com.br",
            subject="Test Message",
            status="new",
        )

    def test_contact_view(self):
        """Test that the contact view works correctly and returns the expected template."""
        response = self.client.get(reverse("contact"))  # Test the URL 'contact'
        self.assertEqual(
            response.status_code, 200
        )  # Check that the status code is 200 (OK)
        self.assertTemplateUsed(
            response, "contact/contact.html"
        )  # Verify that the template used is 'contact/contact.html'

    def test_contact_message_creation(self):
        """Test that a contact message can be created correctly."""
        self.client.login(
            username="regularuser", password="password123"
        )  # Log in as a regular user
        response = self.client.post(
            reverse("contact"),
            data={
                "name": "Test User",
                "email": "test@example.com",
                "subject": "Test Subject",
                "message": "Test message body",
            },
        )
        self.assertEqual(
            response.status_code, 302
        )  # Check for redirection after submission
        self.assertTrue(
            ContactMessage.objects.filter(email="test@example.com").exists()
        )  # Check if the message was saved

    def test_contact_message_without_name(self):
        """Test that the contact message fails validation without a name."""
        response = self.client.post(
            reverse("contact"),
            data={
                "email": "test@example.com",
                "subject": "Test Subject",
                "message": "Test message body",
            },
        )
        self.assertEqual(
            response.status_code, 200
        )  # Check that the form returns the same page
        self.assertFormError(
            response, "contact_form", "name", "This field is required."
        )  # Verify form error message

    def test_contact_message_without_email(self):
        """Test that the contact message fails validation without an email."""
        response = self.client.post(
            reverse("contact"),
            data={
                "name": "Test User",
                "subject": "Test Subject",
                "message": "Test message body",
            },
        )
        self.assertEqual(
            response.status_code, 200
        )  # Check that the form returns the same page
        self.assertFormError(
            response, "contact_form", "email", "This field is required."
        )  # Verify form error message

    def test_contact_message_without_subject(self):
        """Test that the contact message fails validation without a subject."""
        response = self.client.post(
            reverse("contact"),
            data={
                "name": "Test User",
                "email": "test@example.com",
                "message": "Test message body",
            },
        )
        self.assertEqual(
            response.status_code, 200
        )  # Check that the form returns the same page
        self.assertFormError(
            response, "contact_form", "subject", "This field is required."
        )  # Verify form error message

    def test_contact_message_without_message(self):
        """Test that the contact message fails validation without a message."""
        response = self.client.post(
            reverse("contact"),
            data={
                "name": "Test User",
                "email": "test@example.com",
                "subject": "Test Subject",
            },
        )
        self.assertEqual(
            response.status_code, 200
        )  # Check that the form returns the same page
        self.assertFormError(
            response, "contact_form", "message", "This field is required."
        )  # Verify form error message
