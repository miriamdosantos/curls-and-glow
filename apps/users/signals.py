from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal to create a UserProfile instance when a User is created.

    Args:
        sender (Model): The model class that sent the signal.
        instance (User): The actual instance of the User model.
        created (bool): Indicates if a new record was created.
        **kwargs: Additional keyword arguments.
    """
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal to save the UserProfile instance when the User is saved.

    Args:
        sender (Model): The model class that sent the signal.
        instance (User): The actual instance of the User model.
        **kwargs: Additional keyword arguments.
    """
    instance.profile.save()
