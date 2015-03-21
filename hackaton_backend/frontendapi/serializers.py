from django.forms import widgets
from rest_framework import serializers
from models import User,Message,Car


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message