from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate, get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http.response import HttpResponse, JsonResponse
from .models import Servicio, UsuarioPersonalizado
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View
from .forms import FormularioUsuario, FormularioLogin, ServicioForm, CambiarPasswordForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from tasks.mixins import (
    LoginYSuperStaffMixin, ValidarPermisosMixin, LoginMixin
)
from django.http import JsonResponse
from .models import Guia

def home(request):
    return render(request, 'home.html')

def somos(request):
    return render(request, 'somos.html')

def lugares(request):
    return render(request, 'lugares.html')

def rate_guia(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        guia_id = request.POST.get('guia_id')

        try:
            guia = Guia.objects.get(id=guia_id)
            guia.actualizar_calificacion(float(rating))
        except Guia.DoesNotExist:
            return JsonResponse({'error': 'Guia no encontrado.'}, status=404)

        # Devuelve una respuesta JSON con un mensaje de éxito
        return JsonResponse({'message': 'Calificación guardada exitosamente.'})

    # Si la solicitud no es POST, devuelve una respuesta JSON con un mensaje de error
    return JsonResponse({'error': 'Método no permitido.'}, status=405)

class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('home')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


class ListadoUsuario(ListView):
    model = UsuarioPersonalizado
    template_name = 'listar_usuario.html'

    def get_queryset(self):
        return self.model.objects.filter(is_active=True)


class signup(CreateView):
    model = UsuarioPersonalizado
    form_class = FormularioUsuario
    template_name = 'crear_usuario.html'
    success_url = reverse_lazy('servicio')


class crearservicio(CreateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'create_servicio.html'
    success_url = reverse_lazy('tasks')


def tasks(request):
    return render(request, 'tasks.html', {'tasks': tasks})


def signout(request):
    logout(request)
    return redirect('home')


class CambiarPassword(LoginMixin, View):
    template_name = 'cambiar_password.html'
    form_class = CambiarPasswordForm
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = UsuarioPersonalizado.objects.filter(id=request.user.id)
            if user.exists():
                user = user.first()
                user.set_password(form.cleaned_data.get('password1'))
                user.save()
                logout(request)
                return redirect(self.success_url)
            return redirect(self.success_url)
        else:
            form = self.form_class(request.POST)
            return render(request, self.template_name, {'form': form})




def miraflores(request):


    return render(request, 'show_Miraflores.html')

  
