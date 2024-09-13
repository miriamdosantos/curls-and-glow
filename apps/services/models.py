from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.TimeField()
    photo = CloudinaryField('image',default='placeholder')
    

    def __str__(self):
        return self.title