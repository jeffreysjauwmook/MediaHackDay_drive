from django.shortcuts import render
from autoscout.models import trip_entry
from models import User, Car, Message
from serializers import UserSerializer,CarSerializer,MessageSerializer
from rest_framework import generics


# Create your views here.
class UserMixin(object):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MessageMixin(object):
    
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class CarMixin(object):
    
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarList(CarMixin, generics.ListCreateAPIView):
    pass

class UserList(UserMixin, generics.ListCreateAPIView):
    pass

class MessageList(MessageMixin, generics.ListCreateAPIView):
    pass