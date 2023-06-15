from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http.response import HttpResponse, JsonResponse
from .models import Servicio, UsuarioPersonalizado
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import FormularioUsuario, FormularioLogin
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect

#from django.contrib.auth.decorators import login_required

# Create your views here.



def home(request):
    return render(request, 'home.html')



class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    #model = UsuarioPersonalizado
    success_url = reverse_lazy('tasks')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,**kwargs)

    def form_valid(self,form):
        login(self.request,form.get_user())
        return super(Login, self).form_valid(form)
    


class ListadoUsuario(ListView):
    model = UsuarioPersonalizado
    template_name = 'listar_usuario.html'
    
    def get_queryset(self):
        return self.model.objects.filter(is_active = True)

class signup(CreateView):
        model = UsuarioPersonalizado
        form_class = FormularioUsuario
        template_name = 'crear_usuario.html'
        success_url = reverse_lazy('listar_usuarios')
        



def tasks(request):
    return render(request, 'tasks.html', {'tasks': tasks})


def signout(request):
    logout(request)
    return redirect('home')



 





  
