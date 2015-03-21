from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^car/?$', views.CarList.as_view()),
    url(r'^user/?$', views.UserList.as_view()),
    url(r'^message/?$', views.MessageList.as_view()),
)