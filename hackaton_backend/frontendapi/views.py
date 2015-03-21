from models import User, Message
from serializers import UserSerializer,MessageSerializer
from rest_framework import generics, views, response


# Create your views here.
class UserMixin(object):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class MessageMixin(object):

    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class UserList(UserMixin, generics.ListCreateAPIView):
    pass

class MessageList(MessageMixin, generics.ListCreateAPIView):
    pass


class NearbyCarsList(generics.ListAPIView):

    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        #FIXME filter nearby cars
        return User.objects.all()

class MyBehaviour(views.APIView):

    def get(self, request):
        my_behaviour = self.request.user.current_behaviour
        return response.Response(my_behaviour)


class MyLocation(views.APIView):

    def get(self, request):
        my_location = self.request.user.last_known_position
        return response.Response(my_location.as_dict())


class CarStatus(views.APIView):

    def get(self, request):
        return response.Response(request.user.engine_status)
