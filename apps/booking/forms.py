from django import forms
from apps.services.models import Service

class AppointmentForm(forms.Form):
    time = forms.ChoiceField(label='Choose a time', required=True)
    service = forms.ModelChoiceField(queryset=Service.objects.all(), label='Select a Service', required=True)
    coupon = forms.CharField(max_length=100, required=False, label='Optional Coupon Code')
    
    def __init__(self, *args, **kwargs):
        available_times = kwargs.pop('available_times', [])
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['time'].choices = [(time, time) for time in available_times]
