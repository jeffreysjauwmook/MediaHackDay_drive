from models import User, Message, Trip, TODAYS_GAS_PRICE
from serializers import UserSerializer,MessageSerializer, TripSerializer
from rest_framework import generics, views, response, mixins, viewsets
from autoscout.models import trip_entry
from django.shortcuts import get_object_or_404


class MessageMixin(object):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class UserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer


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
        distance = 0.200  # kilometers
        try:
            return User.geo_objects.filter(
                previous_known_position__approx_distance_lt=(user.previous_known_position, distance)
            ).exclude(pk=user.pk)
        except:
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


class TripHistory(generics.ListAPIView):

    serializer_class = TripSerializer

    def get_queryset(self):
        return Trip.objects.filter(user__id=self.request.user.id).order_by('started_at')


class Statistics(views.APIView):

    def get(self, request):
        average = request.user.average_usage
        if average:
            price_per_600_km = 600.0 / average * TODAYS_GAS_PRICE
            total_cost = request.user.km_total / average * TODAYS_GAS_PRICE
        else:
            price_per_600_km = 0
            total_cost = 0
        d = dict(
            price_per_600_km=price_per_600_km,
            total_cost=total_cost,
            average_usage=request.user.average_usage, # one in avrgusage
            grand_total_km=request.user.km_total,
            todays_gas_price=TODAYS_GAS_PRICE
        )
        return response.Response(d)


