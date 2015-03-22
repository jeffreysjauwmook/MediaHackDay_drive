from models import User, Message
from serializers import UserSerializer,MessageSerializer
from rest_framework import generics, views, response
from autoscout.models import trip_entry
from django.shortcuts import get_object_or_404


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
    """
    List of messages for current user
    """
    def get_queryset(self):
    	return Message.objects.filter(receiver = self.request.user)

class MessageUpdate(MessageMixin, generics.RetrieveUpdateAPIView):
    pass


class NearbyCarsList(generics.ListAPIView):

    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        distance = 0.100  # kilometers
        try:
            return User.geo_objects.filter(
                previous_known_position__approx_distance_lt=(user.previous_known_position, distance)
            ).exclude(pk=user.pk)
        except:
            raise
            return User.objects.none()



class MyBehaviour(views.APIView):

    def get(self, request):
    	user = User.objects.get(pk = request.user.id)
    	te = trip_entry.objects.filter(vim=user.vim, checked=False).order_by("id").reverse()[:5]
    	my_behaviour = int(user.current_behaviour)
    	#print "current: " + str(my_behaviour)
        for t in te:
        	print t.id
        	print t.heavy
        	if t.heavy:
        		my_behaviour -= 1
        	else:
        		my_behaviour += 1
        	t.checked = True
        	t.save()
        #print "New: " + str(my_behaviour)
        if my_behaviour < 0:
        	my_behaviour = 0
        if my_behaviour > 10:
        	my_behaviour = 10

        user.current_behaviour = str(my_behaviour)
        user.save()
        return response.Response(str(my_behaviour))


class MyLocation(views.APIView):

    def get(self, request):
    	try:
    	    u = User.objects.get(pk=request.user.id)
            my_location = u.last_known_position
            return response.Response(my_location.as_dict())
        except:
        	return response.Response("404")

    def post(self, request):
        a = request.POST.get('lat')
        b = request.POST.get('lng')
        speed = request.POST.get('speed')
        if not speed or not a or not b:
            return response.Response("404")

        u = get_object_or_404(User, pk=request.user.id)
        u.speed = speed
        u.previous_known_position = u.last_known_position
        u.last_known_position = (float(a), float(b))
        u.save()
        return response.Response("Ok")


class CarStatus(views.APIView):

    def get(self, request):
        return response.Response(request.user.engine_status)
