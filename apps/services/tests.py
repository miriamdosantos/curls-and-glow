from django.test import TestCase
from django.urls import reverse
from .models import Service

class ServicesViewsTests(TestCase):
    """Tests for the Services views functionality."""

    def setUp(self):
        """Set up the test case by creating example data for the Service model."""
        Service.objects.create(title="Serviço 1")  # Create a Service instance with title "Serviço 1"
        Service.objects.create(title="Serviço 2")  # Create a Service instance with title "Serviço 2"

    def test_home_view(self):
        """Test that the home view works correctly and returns the expected template."""
        response = self.client.get(reverse('home'))  # Test the URL 'home'
        self.assertEqual(response.status_code, 200)  # Check that the status code is 200 (OK)
        self.assertTemplateUsed(response, 'services/index.html')  # Verify that the template used is 'services/index.html'

    def test_services_view(self):
        """Test that the services view works correctly and returns the expected template and content."""
        response = self.client.get(reverse('services'))  # Test the URL 'services'
        self.assertEqual(response.status_code, 200)  # Check that the status code is 200 (OK)
        self.assertTemplateUsed(response, 'services/services.html')  # Verify that the template used is 'services/services.html'
        self.assertContains(response, "Serviço 1")  # Check that the expected content ("Serviço 1") is in the response
