from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

@receiver(post_save, sender=get_user_model())
def create_profile_for_new_user(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)
