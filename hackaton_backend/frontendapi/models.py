from django.db import models
from django.contrib.auth.models import AbstractUser

import geosimple


class User(AbstractUser):
    last_known_position = geosimple.GeohashField(blank=True, null=True)
    previous_known_position = geosimple.GeohashField(blank=True, null=True)
    social_score = models.IntegerField(blank=True, null=True)
    current_behaviour = models.CharField(max_length=255, default='0')
    engine_status = models.CharField(max_length=255)
    vim = models.CharField(max_length=255)
    speed = models.CharField(max_length=255, default=0)
    avatar = models.ImageField(
        'Profilephoto',
        upload_to='user_avatars/',
        blank=True,
    )

    geo_objects = geosimple.GeoManager()


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sender')
    receiver = models.ForeignKey(User, related_name='receiver')
    sent_at = models.DateTimeField()
    delivered_at = models.DateTimeField()
    payload = models.CharField(max_length=255)  # sorry, thanks, no problem, wtf
    delivered = models.BooleanField(
        help_text='Delivered to receiver',
        default=False
    )
    in_reply_to = models.ForeignKey(
        'Message', blank=True, null=True, related_name='follow_up_message'
    )

