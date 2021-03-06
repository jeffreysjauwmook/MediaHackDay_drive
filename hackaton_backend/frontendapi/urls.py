from django.conf.urls import patterns, url
from rest_framework import routers
from . import views

router = routers.SimpleRouter()

urlpatterns = patterns('',
    url(r'^message/?$', views.MessageList.as_view()),
    url(r'^message-update/(?P<pk>\d+)/$', views.MessageUpdate.as_view()),
    url(r'^nearby-cars/?$', views.NearbyCarsList.as_view()),
    url(r'^my-behaviour/?$', views.MyBehaviour.as_view()),
    url(r'^my-location/?$', views.MyLocation.as_view()),
    #FIXME make it real filtered messages, and set messages as read
    url(r'^get-messages/?$', views.MessageList.as_view()),
    url(r'^car-status/?$', views.CarStatus.as_view()),
    url(r'^statistics/?$', views.Statistics.as_view()),
    url(r'^trip-history/?$', views.TripHistory.as_view()),

)
router.register(r'user', views.UserViewSet)

urlpatterns += router.urls
