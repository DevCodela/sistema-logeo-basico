from django.conf.urls import patterns, include, url
from principal.views import IndexAboutView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexAboutView.as_view()),
    url(r'^login/$', 'principal.views.mylogin'),
    url(r'^cerrar/$', 'principal.views.cerrar'),
    url(r'^privado/$','principal.views.privado'),
    url(r'^(?P<username>[-\w]+)/$', 'principal.views.perfil'),
  
)

