from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate, get_user_model
from .forms import UserLoginForm, UserSignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http.response import HttpResponse, JsonResponse
from .models import Servicio, UsuarioPersonalizado, CustomAccountManager
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#from django.contrib.auth.decorators import login_required

# Create your views here.


""" def hello(request):
    return render(request, 'signup.html', {
        'form': UserCreationForm
    }) """


""" def task_detail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Servicio, pk=task_id, user=request.user) 
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html', {'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Servicio, pk=task_id, user=request.user) 
            form = TaskForm(request.POST, instance=task)
            form.save()       
            return redirect('home')
        except ValueError:
            return render(request, 'task_detail.html', {'task': task, 'form': form,
            'error':"Error updating task"})
"""

""""def complete_task(request, task_id):
    task = get_object_or_404(Servicio, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks') """


""""def delete_task(request, task_id):
    task = get_object_or_404(Servicio, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')"""


def home(request):
    return render(request, 'home.html')


def signin(request):

        if request.method == 'GET':
            return render(request, 'signin.html', {
            'form': AuthenticationForm
            })
        else:

            login_form = UserLoginForm(request.POST or None)
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Has iniciado sesion correctamente')
                    return redirect('tasks.html')
                else:
                    messages.warning(
                    request, 'Correo Electronico o Contrasena invalida')
                    return redirect('home')

            messages.error(request, 'Formulario Invalido')
            return redirect('home')

def signup(request):
        
    if request.method == 'GET':
            return render(request, 'register.html')
    else:

        signup_form = UserSignUpForm(request.POST or None)
        if signup_form.is_valid():
            username = signup_form.cleaned_data.get('username')
            nombre = signup_form.cleaned_data.get('nombre')
            apellido = signup_form.cleaned_data.get('apellido')
            password = signup_form.cleaned_data.get('password')
            pais = signup_form.cleaned_data.get('password')
            try:
                user = get_user_model().objects.create(
                    username = username,
                    nombre = nombre,
                    apellido = apellido,
                    password= password,
                    pais = pais,

                )
                login(request, user)
                return redirect('tasks.html')

            except Exception as e:
                print(e)
                return JsonResponse({'detail': f'{e}'})

        messages.warning(request, 'Las Contrasenas no coinciden')
        return redirect('tasks')


        """if request.method == 'GET':
        return render(request, 'register.html')
        else:
        signup_form = UserSignUpForm(request.POST or None)
        if signup_form.is_valid():
            username = signup_form.cleaned_data.get('username')
            nombre = signup_form.cleaned_data.get('nombre')
            apellido = signup_form.cleaned_data.get('apellido')
            password = signup_form.cleaned_data.get('password')
            try:
                user = UsuarioPersonalizado.objects.create_user(
                    username=username,
                    nombre=nombre,
                    apellido=apellido,
                    password=password,
                )
                login(request, user)
                return redirect('tasks.html')
            except Exception as e:
                print(e)
                return JsonResponse({'detail': f'{e}'})

        messages.warning(request, 'Las Contraseñas no coinciden')
        return redirect('tasks')"""








    









    """if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # register user
                
                check = UsuarioPersonalizado.objects.filter(id = request.user.id)
                if len(check) > 0:
                    user = UsuarioPersonalizado.objects.create(
                    #username=User.objects.get(username=request.POST["username"]), password=request.POST['password1'])
                    username = User.objects.create(username = request.POST["username"]), password = request.POST["password1"])

                #nombre = request.POST['nombre'],
                    #apellido = request.POST['apellido'], pais = request.POST['pais'], es_Guia = request.POST['es_Guia'],
                    #es_Cliente = request.POST['es_Cliente']
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:

                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'user already existed',
                })

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Password do not match',
        })"""
        



def tasks(request):
    return render(request, 'tasks.html', {'tasks': tasks})

def tasks_completed(request):
    return render(request, 'tasks.html', {'tasks': tasks})



"""

def create_task(request):

    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': TaskForm
        })
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html', {
                'form': TaskForm,
                'error': 'Pleade provide valed data'
            })
"""

def signout(request):
    logout(request)
    return redirect('home')






    
    """if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
        else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password incorect'
            })
        else:
            login(request, user)
            return redirect('tasks')
"""
