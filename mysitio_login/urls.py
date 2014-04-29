from django.conf.urls import patterns, include, url
from principal.views import IndexAboutView, MyLogin, Cerrar, Privado, UsuarioDetailView
from django.contrib import admin
from django.contrib.auth.decorators import login_required

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexAboutView.as_view()),
    url(r'^login/$', MyLogin.as_view(), name='my_login'),
    url(r'^cerrar/$', login_required(Cerrar.as_view()),name='cerrar'),
    url(r'^privado/$',login_required(Privado.as_view()),name='privado'),
    url(r'^(?P<pk>\d+)/$', UsuarioDetailView.as_view(), name='detalle_usuario'),
)

