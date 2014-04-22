from django.views.generic import TemplateView
from django.http import HttpResponseRedirect 
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def mylogin(request):
	if request.method == 'POST':
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


@login_required(login_url='/mylogin')
def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/')

@login_required(login_url='/mylogin')
def privado(request):
	usuario=request.user
	return render(request,'principal/privado.html',{'usuario':usuario})

def perfil(request, username):
	usuario = request.user
	usuario_no_logueado = User.objects.get(username=username)
	if usuario == User.objects.get(username=username):
		return render(request,'principal/perfil.html', {'usuario':usuario})
	else:
		return render(request,'principal/perfil_no_logueado.html', {'usuario':usuario_no_logueado}) 


class IndexAboutView(TemplateView):
    template_name = "base.html"
