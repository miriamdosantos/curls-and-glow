from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Stylist(models.Model):
    """
    Model representing a stylist.

    Attributes:
        name (str): The name of the stylist.
        bio (str): A brief biography of the stylist.
        photo (CloudinaryField): The stylist's photo.
        availabilities (ManyToManyField): Availability slots for the stylist.
    """

    name = models.CharField(max_length=200)  # Stylist's name
    bio = models.TextField()  # Stylist's biography
    photo = CloudinaryField("image", default="placeholder")  # Stylist's photo
    availabilities = models.ManyToManyField(
        "Availability"
    )  # Represent the intermediate table Stylists_Availability

    def __str__(self):
        return f"Stylist: {self.name}"  # String representation of the stylist


class Availability(models.Model):
    """
    Model representing the availability of a stylist.

    Attributes:
        DAY_CHOICES (list): Choices for the days of the week.
        day_of_week (str): The day of the week.
        start_time (TimeField): The start time of availability.
        end_time (TimeField): The end time of availability.
    """

    DAY_CHOICES = [
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
        ("Sunday", "Sunday"),
    ]
    day_of_week = models.CharField(max_length=9, choices=DAY_CHOICES)  # Day of the week
    start_time = models.TimeField()  # Start time of availability
    end_time = models.TimeField()  # End time of availability

    class Meta:
        unique_together = (
            "day_of_week",
            "start_time",
            "end_time",
        )  # Prevent duplication of time slots
        ordering = ["day_of_week", "start_time"]  # Default ordering for availability

    def __str__(self):
        return f"{self.day_of_week} {self.start_time} to {self.end_time}"  # String representation of availability
