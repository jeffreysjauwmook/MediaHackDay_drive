from models import trip_entry
from frontendapi.models import User
from serializers import TripEntrySerializer
from rest_framework import generics


class EntryList(generics.ListCreateAPIView):
    queryset = trip_entry.objects.all()
    serializer_class = TripEntrySerializer

    def post(self, request):
        ret = super(EntryList, self).post(request)
        user = User.objects.get(vim=request.POST['vim'])
        user.km_total = request.POST['km_total']
        user.total_fuel_consumption = request.POST['fuel_total']
        heavy = request.POST['heavy'] == 'true'

        score = user.eco_score

        if score == 'good':
            if heavy:
                user.eco_score = 'neutral'
        elif score == 'neutral':
            if heavy:
                user.eco_score = 'medium'
            else:
                user.eco_score = 'good'
        elif score == 'medium':
            if heavy:
                user.eco_score = 'bad'
            else:
                user.eco_score = 'neutral'
        elif score == 'bad':
            if not heavy:
                user.eco_score = 'medium'
        else:
            user.eco_score = 'neutral'
        user.save()
        return ret
