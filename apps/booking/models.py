from django.db import models
from apps.users.models import UserProfile
from apps.services.models import Service
from apps.stylists.models import Stylist
from cloudinary.models import CloudinaryField


# Create your models here.
# bookings/models.py



class Offer(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    code = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title

class Booking(models.Model):
    STATUS_CHOICES = [
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
        ('Completed', 'Completed'),
        ('Updated', 'Updated')
    ]

    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    stylish = models.ForeignKey(Stylist, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, null=True, blank=True)  # Referência correta ao modelo Offer
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Confirmed')  # Confirmed como padrão
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Booking by {self.full_name} with {self.stylish.name} on {self.date_time}"
    
class Testimonial(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    rating = models.IntegerField()
    message = models.TextField()
    photo = CloudinaryField('image', default ='https://res.cloudinary.com/dx21s72fa/image/upload/v1727857392/w0wngka886ke3rcyr5gd.png', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Testimonial for {self.booking.full_name}, referente: {self.booking.service} by: {self.booking.stylish}"