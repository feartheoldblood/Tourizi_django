import pytest
from tasks.models import UsuarioPersonalizado
from django.urls import reverse
from django.contrib.auth import get_user_model, authenticate
import stripe

@pytest.mark.django_db
def test_user_creation():
    user = UsuarioPersonalizado.objects.create_user(
        username = 'Cesar123',
        nombre = 'Cesar',
        apellido = 'Capcha',
        pais = 'Perú',
        es_Guia = False,
        es_Cliente = True,
        password = '12345',
        is_staff=False,

    )
    assert user.username == 'Cesar123'


@pytest.mark.django_db
def test_user_creation():
    user = UsuarioPersonalizado.objects.create_user(
        username = 'Cesar123',
        nombre = 'Cesar',
        apellido = 'Capcha',
        pais = 'Perú',
        es_Guia = False,
        es_Cliente = True,
        password = '12345',
        is_staff=False,

    )
    assert user.username == 'Cesar123'


@pytest.fixture
def user_data(db):
    # Crear un usuario de prueba en la base de datos
    user = get_user_model().objects.create_user(
        username='Cesar123',
        nombre='Cesar',
        apellido='Capcha',
        pais='Perú',
        es_Guia=False,
        es_Cliente=True,
        password='12345',
        is_staff=False,
    )
    yield user

@pytest.mark.django_db
def test_login_success(client, user_data):
    # Obtener las URLs necesarias
    login_url = reverse('login')
    home_url = reverse('home')

    # Realizar una solicitud POST al formulario de inicio de sesión con las credenciales válidas
    response = client.post(login_url, {'username': 'Cesar123', 'password': '12345'})

    # Verificar que la respuesta redirija al URL de éxito
    assert response.status_code == 302  # Código de estado de redirección
    assert response.url == home_url

    # Verificar que el usuario esté autenticado
    user = authenticate(username='Cesar123', password='12345')
    assert user is not None
    assert user.is_authenticated

stripe.api_key ="sk_test_51NIMdQISVJQQrOv3EsOWJnwvlYWt2oaZG6OePSoEpuVJNYN71cRD3LOXIElOuaz24YdVNCy1VqmNXFQS6Uy8eKIk00vY2jAwkf"

@pytest.mark.django_db
def test_create_payment_intent():
    

    payment_intent = stripe.PaymentIntent.create(
        amount=600,
        currency="usd",
        payment_method="pm_card_visa",
    )
    # Verifica que el pago se haya creado exitosamente
    assert payment_intent.status == "requires_confirmation"
