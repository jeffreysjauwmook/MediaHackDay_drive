from models import User, Message
from serializers import UserSerializer,MessageSerializer
from rest_framework import generics, views, response
from autoscout.models import trip_entry


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
    	user = User.objects.get(vim=123)
    	te = trip_entry.objects.filter(vim=123).order_by("id").reverse()[:5]
    	my_behaviour = int(user.current_behaviour)
    	print "current: " + str(my_behaviour)
        for t in te:
        	print t.id
        	print t.heavy
        	if t.heavy:
        		my_behaviour -= 1
        	else:
        		my_behaviour += 1
        print "New: " + str(my_behaviour)		
        if my_behaviour < 0:
        	my_behaviour = 0
        if my_behaviour > 10:
        	my_behaviour = 10

        user.current_behaviour = str(my_behaviour)	
        user.save()
        return response.Response(str(my_behaviour))


class MyLocation(views.APIView):

    def get(self, request):
        my_location = self.request.user.last_known_position
        return response.Response(my_location.as_dict())


class CarStatus(views.APIView):

    def get(self, request):
        return response.Response(request.user.engine_status)
