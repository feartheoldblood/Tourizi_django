from typing import Any, Dict
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm, UsuarioCustomForm
from .models import Servicio, UsuarioPersonalizado
from django.utils import timezone

#cambios pasarela
import stripe
from django.conf import settings
from django.views.generic import TemplateView
from django.views import View
from django.http import JsonResponse
from .models import Product
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_SECRET_KEY

class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"

class ProductLandingPageView(TemplateView):
    template_name = "landing.html"
    #define productos Test Product
    def get_context_data(self, **kwargs):
        product = Product.objects.get(name="Test Product") 
        context = super(ProductLandingPageView, self).get_context_data(**kwargs)
        context.update({
            "product": product,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })
        return context


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        product_id = self.kwargs["pk"]
        product = Product.objects.get(id=product_id)
        print(product)
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': product.price,
                        'product_data': {
                            'name': product.name,
                            # 'images': ['https://i.imgur.com/EHyR2nP.png'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                "product_id": product.id
            },
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })
####
@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        customer_email = session["customer_details"]["email"]
        product_id = session["metadata"]["product_id"]

        product = Product.objects.get(id=product_id)

        send_mail(
            subject="Here is your product",
            message=f"Thanks for your purchase. Here is the product you ordered. The URL is {product.url}",
            recipient_list=[customer_email],
            from_email="matt@test.com"
        )

        # TODO - decide whether you want to send the file or the URL
    
    elif event["type"] == "payment_intent.succeeded":
        intent = event['data']['object']

        stripe_customer_id = intent["customer"]
        stripe_customer = stripe.Customer.retrieve(stripe_customer_id)

        customer_email = stripe_customer['email']
        product_id = intent["metadata"]["product_id"]

        product = Product.objects.get(id=product_id)

        send_mail(
            subject="Here is your product",
            message=f"Thanks for your purchase. Here is the product you ordered. The URL is {product.url}",
            recipient_list=[customer_email],
            from_email="matt@test.com"
        )

    return HttpResponse(status=200)
#fin cambios pasarela



#from django.contrib.auth.decorators import login_required

# Create your views here.


def hello(request):
    return render(request, 'signup.html', {
        'form': UserCreationForm
    })


def task_detail(request, task_id):
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

def complete_task(request, task_id):
    task = get_object_or_404(Servicio, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')


def delete_task(request, task_id):
    task = get_object_or_404(Servicio, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')


def home(request):
    return render(request, 'home.html')


def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # register user
                user = UsuarioPersonalizado.objects.create(
                    username=User.objects.get(username=request.POST["username"]), password=request.POST['password1'])
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
        })


def tasks(request):
    tasks = Servicio.objects.filter(user=request.user)
    return render(request, 'tasks.html', {'tasks': tasks})

def tasks_completed(request):
    tasks = Servicio.objects.filter(user=request.user).order_by('-datecompleted')
    return render(request, 'tasks.html', {'tasks': tasks})



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


def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
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

