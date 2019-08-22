from django.db.models.signals import post_save
from accounts.models import Profile
from django.contrib.auth.models import User
from django.dispatch import receiver

# creates a new Profile whenever a new user registers
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
# updates the user Profile information whenever a user changes their information
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()