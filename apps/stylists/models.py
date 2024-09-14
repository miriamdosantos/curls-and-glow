from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Stylist(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    photo = CloudinaryField('image',default='placeholder')
    availabilities = models.ManyToManyField('Availability') # represent the intermediate table Stylists_Availability

    def __str__(self):
        return f" Stylist: {self.name}"

class Availability(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    day_of_week = models.CharField(max_length=9, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = ('day_of_week', 'start_time', 'end_time') # to not allow duplication
        ordering = ['day_of_week', 'start_time']
    
    def __str__(self):
        return f"{self.day_of_week} {self.start_time} to {self.end_time}"
