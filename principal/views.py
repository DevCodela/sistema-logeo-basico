from django.views.generic import TemplateView, DetailView, View
from django.http import HttpResponseRedirect 
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render


class MyLogin(View):

    def post(self, request, *args, **kwargs):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect("/privado/")
			else:
				return render(request,'principal/noactivo.html')
		else:
			return render(request,'principal/nousuario.html')


class Cerrar(View):	

	def get(self, request, *args, **kwargs):
		logout(request)
		return HttpResponseRedirect('/')

class Privado(View):

	def get(self, request, *args, **kwargs):
		usuario=request.user
		return render(request,'principal/privado.html',{'usuario':usuario})


class UsuarioDetailView(DetailView):
	model = User
	context_object_name = 'usuario'
	template_name = "principal/privado.html"


class IndexAboutView(TemplateView):
    template_name = "base.html"
