from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    """
    Model to store additional information about the user.

    Attributes:
        user (User): One-to-one relationship with the User model.
        phone_number (str): User's phone number, optional field.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone_number = models.CharField(
        max_length=15, blank=True, null=True
    )  # Phone number field

    def __str__(self):
        """
        String representation of the UserProfile instance.

        Returns:
            str: Formatted string containing the username and email.
        """
        return f"{self.user.username}, {self.user.email}"
