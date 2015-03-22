from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

import geosimple


TODAYS_GAS_PRICE = 1.436 # euro


class GeoUserManager(UserManager, geosimple.GeoManager):
    pass


class User(AbstractUser):
    last_known_position = geosimple.GeohashField(blank=True, null=True)
    previous_known_position = geosimple.GeohashField(blank=True, null=True)
    social_score = models.IntegerField(blank=True, null=True)
    eco_score = models.CharField(default='neutral', max_length=255)  # good, neutral, medium, bad
    current_behaviour = models.CharField(max_length=255, default='0')
    engine_status = models.CharField(max_length=255)
    vim = models.CharField(max_length=255)
    speed = models.CharField(max_length=255, default=0)
    avatar = models.ImageField(
        'Profilephoto',
        upload_to='user_avatars/',
        blank=True,
    )
    km_total = models.IntegerField(default=0)
    total_fuel_consumption = models.IntegerField(default=0)
    car_model = models.CharField(max_length=255, default='')
    average_usage =  models.IntegerField(default=0) # 1 / average_usage

    geo_objects = GeoUserManager()


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


class Trip(models.Model):
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()
    user = models.ForeignKey(User)
    kilometers = models.IntegerField(default=0)
    fuel_consumption = models.FloatField(default=0)
    economy = models.CharField(default='economical', max_length=255)  # costly, economical

    def save(self, *args, **kwargs):
        # FIXME update statistics
        return super(Trip, self).save(*args, **kwargs)


