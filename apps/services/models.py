from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.TimeField(blank=True, null=True)
    photo = CloudinaryField("image", default="placeholder")

    ICON_MAP = {
        "Custom Curl Cuts": "fa-scissors",
        "Curl Treatment": "fa-shower",
        "Curl Finalization": "fa-spray-can",
    }

    def get_icon(self):
        return self.ICON_MAP.get(self.title, "fa-question-circle")

    def get_duration_display(self):
        """Converte o campo duration para uma string legível (e.g., '1h 45min')."""
        hours, minutes = self.duration.hour, self.duration.minute
        duration_str = []
        if hours > 0:
            duration_str.append(f"{hours}h")
        if minutes > 0:
            duration_str.append(f"{minutes}min")
        return " ".join(duration_str) or "0min"

    def __str__(self):
        return self.title
