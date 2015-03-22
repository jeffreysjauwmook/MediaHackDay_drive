from rest_framework import serializers
from models import User,Message, Trip
import datetime


class UserSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        ret = super(UserSerializer, self).to_representation(instance)
        ret['last_known_position'] = instance.last_known_position.as_dict()
        ret['previous_known_position'] = instance.last_known_position.as_dict()
        return ret

    class Meta:
        model = User


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message


class TripSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trip
        fields = ['kilometers', 'fuel_consumption', 'economy', 'ended_at']

    def to_representation(self, instance):
        ret = super(TripSerializer, self).to_representation(instance)
        today = datetime.datetime.today()
        yesterday = today - datetime.timedelta(days=1)
        if instance.ended_at.day == today.day:
            ret['ended_at'] = 'today'
        elif instance.ended_at.day == yesterday.day:
            ret['ended_at'] = 'yesterday'
        else:
            ret['ended_at'] = instance.ended_at.strftime('%d-%m-%Y')
        return ret


