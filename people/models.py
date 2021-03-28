from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.

"""
{
    "username":"@suriya",
    "first_name":"suriya",
    "last_name":"s",
    "email":"suriya@gmail.com",
    "password":"suriya"
}
"""

class Friend(models.Model):
    username_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    username_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    friend_status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.username_from)+" - "+str(self.username_to)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
