# bookings/forms.py

from django import forms
from .models import Testimonial


class TestimonialForm(forms.ModelForm):
    """
    Form for submitting a testimonial.

    This form is based on the Testimonial model and allows users to 
    submit a rating, message, and optional photo.

    Attributes:
        Meta (class): Configuration for the ModelForm, including
                      the model and fields to be included in the form.
    """
    class Meta:
        model = Testimonial  # Model associated with the form
        fields = ["rating", "message", "photo"]  # Fields to be included in the form
        widgets = {
            "message": forms.Textarea(attrs={"rows": 4}),  # Textarea for the message with 4 rows
            "rating": forms.Select(
                choices=[(i, str(i)) for i in range(1, 6)]  # Rating from 1 to 5
            ),
        }
