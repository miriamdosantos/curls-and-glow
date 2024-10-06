from django.db import models
from apps.users.models import UserProfile
from apps.services.models import Service
from apps.stylists.models import Stylist
from cloudinary.models import CloudinaryField

# Create your models here.
# bookings/models.py


class Offer(models.Model):
    """
    Model representing a special offer for services.

    Attributes:
        title (str): The title of the offer.
        description (str): A description of the offer.
        discount_percentage (Decimal): The percentage discount offered.
        code (str): The promotional code associated with the offer.
        start_date (date): The start date of the offer.
        end_date (date): The end date of the offer.
    """

    title = models.CharField(max_length=255)
    description = models.TextField()
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    code = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        """Return a string representation of the Offer instance."""
        return self.title


class Booking(models.Model):
    """
    Model representing a booking made by a user.

    Attributes:
        user_profile (UserProfile): The user profile associated with the booking.
        full_name (str): The full name of the user making the booking.
        email (str): The email address of the user making the booking.
        service (Service): The service being booked.
        stylish (Stylist): The stylist assigned to the booking.
        date_time (datetime): The date and time of the booking.
        created_on (datetime): The timestamp when the booking was created.
        offer (Offer, optional): The offer applied to the booking.
        status (str): The current status of the booking.
    """

    STATUS_CHOICES = [
        ("Confirmed", "Confirmed"),
        ("Cancelled", "Cancelled"),
        ("Completed", "Completed"),
        ("Updated", "Updated"),
    ]

    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    stylish = models.ForeignKey(Stylist, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    offer = models.ForeignKey(
        Offer, on_delete=models.CASCADE, null=True, blank=True
    )  # Referência correta ao modelo Offer
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default="Confirmed"
    )  # Confirmed como padrão

    class Meta:
        """Meta class to define model behavior."""

        ordering = ["-created_on"]

    def __str__(self):
        """Return a string representation of the Booking instance."""
        return f"Booking by {self.user_profile} with {self.stylish.name} on {self.date_time}"


class Testimonial(models.Model):
    """
    Model representing a testimonial for a completed booking.

    Attributes:
        booking (Booking): The booking associated with the testimonial.
        rating (int): The rating given by the user (e.g., 1 to 5).
        message (str): The testimonial message provided by the user.
        photo (CloudinaryField): An optional photo associated with the testimonial.
        created_at (datetime): The timestamp when the testimonial was created.
    """

    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    rating = models.IntegerField()
    message = models.TextField()
    photo = CloudinaryField(
        "image",
        default="https://res.cloudinary.com/dx21s72fa/image/upload/v1727857392/w0wngka886ke3rcyr5gd.png",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the Testimonial instance."""
        return f"Testimonial for {self.booking.full_name}, referente: {self.booking.service} by: {self.booking.stylish}"
