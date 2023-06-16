
from django.contrib import admin
from django.urls import path
#cambio pasarela
from tasks.views import (
    CreateCheckoutSessionView,
    ProductLandingPageView,
    SuccessView,
    CancelView,
    stripe_webhook
)
#fin cambio pasarela
from tasks import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name= 'home'),
    path('signup/', views.signup, name ='signup' ),
    path('tasks/', views.tasks, name ='tasks' ),
    path('tasks_completed/', views.tasks_completed, name ='tasks_completed' ),
    path('logout/', views.signout, name ='logout' ),
    path('signin/', views.signin, name ='signin' ),
    path('tasks/create/', views.create_task, name ='create_task' ),
    path('tasks/<int:task_id>/', views.task_detail , name= 'task_detail'),
    path('tasks/<int:task_id>/complete', views.complete_task, name= 'complete_task'),
    path('tasks/<int:task_id>/delete', views.delete_task  , name= 'delete_task'),
    #INICIO PASARELA
    path('', ProductLandingPageView.as_view(), name='landing-page'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('webhooks/stripe/', stripe_webhook, name='stripe-webhook'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    #FIN PASARELA

] 


