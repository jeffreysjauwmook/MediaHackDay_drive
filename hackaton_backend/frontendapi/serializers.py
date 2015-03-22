from rest_framework import serializers
from models import User,Message, Trip


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
