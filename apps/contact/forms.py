from .models import ContactMessage
from django import forms


class ContactForm(forms.ModelForm):
    """
    Form for submitting a contact message.

    This form is based on the ContactMessage model and includes
    fields for the user to fill out when sending a message.

    Attributes:
        Meta (class): Contains metadata about the form, including
        the model to use and the fields to include.
    """

    class Meta:
        model = ContactMessage  # Model associated with the form
        fields = ("name", "email", "subject", "message")  # Fields included in the form
