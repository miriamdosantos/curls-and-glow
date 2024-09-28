from .models import Booking
from django import forms

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('date_time','full_name', 'email', 'service', 'stylish', 'offer')

        widgets = {
            'date_time': forms.SplitDateTimeWidget(
                date_attrs={'type': 'date', 'class': 'form-control'},
                time_attrs={'type': 'time', 'class': 'form-control'}
            ),
        }
