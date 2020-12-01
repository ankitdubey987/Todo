from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from user import models
from django.contrib.auth.models import User

@receiver(post_save,sender=User)
def create_profile_handler(sender,instance,created,**kwargs):
    if not created:
        return
    # Create the profile object, only if it is newly created
    profile = models.Profile(user = instance)
    profile.save()