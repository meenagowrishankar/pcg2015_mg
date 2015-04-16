from django.conf.urls import patterns, include, url
from django.contrib import admin
from votreg import views

urlpatterns = patterns('',
	    url(r'^admin/', include(admin.site.urls)),
	    url(r'^$', views.index, name='index'),
	    url(r'^state/(?P<state_name>[\w\-]+)/$', views.state, name='state')
	    )
