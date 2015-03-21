from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MediaHackDay.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^as-api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^as-api/v1.0/', include('autoscout.urls')),
    url(r'^api/v1.0/', include('frontendapi.urls')),
    url(r'^login/?$', 'django.contrib.auth.views.login'),
    url(r'^logout/?$', 'django.contrib.auth.views.logout'),
    url(r'^hello/?$', TemplateView.as_view(template_name="hello.html")),
)
