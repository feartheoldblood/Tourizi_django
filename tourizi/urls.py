"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from tasks.views import ListadoUsuario, signup, Login, crearservicio, CambiarPassword
from tasks import views
from products.views import (
    CreateCheckoutSessionView,
    ProductLandingPageView,
    SuccessView,
    CancelView,
    stripe_webhook,
    StripeIntentView,
    delete2,
)
from django.conf import settings
from django.conf.urls.static import static

#from django.shortcuts import redirect


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name= 'home'),
    #path('signup/', views.signup, name ='signup' ),
    path('somos/', views.somos, name= 'somos'),
    path('lugares/', views.lugares, name= 'lugares'),
    path('tasks/', views.tasks, name ='tasks' ),

    path('logout/', views.signout, name ='logout' ),
    #path('signin/', views.signin, name ='signin' ),
    path('listado_usuarios/', ListadoUsuario.as_view(), name ='listar_usuarios'),
    path('registrar_usuario/', signup.as_view(), name = 'registrar_usuario'),
    path('login/', Login.as_view(), name = 'login'),
    path('crear_servicio/', crearservicio.as_view(), name = 'servicio' ),
    path('cambiar_password/',CambiarPassword.as_view(), name='cambiar_password'),
    #path('servicio/', views.crearservicio, name='servicio')
    path('landing_page/', ProductLandingPageView.as_view(), name='landing-page'),
    path('create-checkout-session/<int:pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('create-payment-intent/<pk>/', StripeIntentView.as_view(), name='create-payment-intent'),
    path('webhooks/stripe/', stripe_webhook, name='stripe-webhook'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('Miraflores/', views.miraflores, name='miraflores'),
    path('delete2/<int:pk>', delete2, name='delete2'),
    path('calificar_guia/', views.rate_guia, name='rate_guia'),
] 
# Otras rutas de URL de tu proyecto

#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, #document_root=settings.MEDIA_ROOT)
#def redirect_to_landing(request):
#    if request.user.is_authenticated:
#        return redirect('landing-page')
#    else:
#        return redirect('login')
