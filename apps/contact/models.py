from django.db import models
from apps.users.models import UserProfile

# Create your models here.
class ContactMessage(models.Model):
    STATUS_CHOICES = [
    ('new', 'New'),
    ('read', 'Read'),
    ('responded', 'Responded'),
]
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True )
    name = models.CharField(max_length=200)
    email= models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    response = models.TextField(blank=True, null=True) # aditional fideld to allow admin asnwer
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.name} - {self.subject}"
