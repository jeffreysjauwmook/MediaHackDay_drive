from django.forms import widgets
from rest_framework import serializers
from models import User,Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message

