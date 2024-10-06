from django.db import models
from apps.users.models import UserProfile


# Create your models here.
class ContactMessage(models.Model):
    """
    Model to store contact messages from users.

    This model holds the information about messages sent by users
    through the contact form, including the user's profile,
    message content, and status.

    Attributes:
        STATUS_CHOICES (list): A list of possible statuses for the
        contact message.
        user_profile (ForeignKey): A link to the UserProfile model,
        allowing for association with a specific user.
        name (CharField): The name of the user sending the message.
        email (EmailField): The email address of the user.
        subject (CharField): The subject of the message.
        message (TextField): The content of the message.
        created_at (DateTimeField): The timestamp for when the message
        was created.
        response (TextField): An optional field for admin responses
        to the message.
        status (CharField): The current status of the message, with
        predefined choices.
    """

    STATUS_CHOICES = [
        ("new", "New"),  # The message has not been read yet
        ("read", "Read"),  # The message has been read
        ("responded", "Responded"),  # A response has been sent
    ]

    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, null=True, blank=True
    )  # User associated with the message
    name = models.CharField(max_length=200)  # Name of the user
    email = models.EmailField()  # User's email address
    subject = models.CharField(max_length=200)  # Subject of the message
    message = models.TextField()  # Content of the message
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # Timestamp of message creation
    response = models.TextField(
        blank=True, null=True
    )  # Additional field for admin response
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="new"
    )  # Current status of the message

    class Meta:
        ordering = ["-created_at"]  # Order messages by creation date, descending

    def __str__(self):
        return f"{self.name} - {self.subject}"  # String representation of the message
