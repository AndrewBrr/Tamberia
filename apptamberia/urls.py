from django.urls import path
from apptamberia.views import portal, register_request, login_request, registrarUsuario

urlpatterns = [
    path('portal/', portal, name='Portal'),
    path('registro/', register_request, name='Registrarse'),
    path('registrarUsuario/', registrarUsuario, name='registrarUsuario'),
    path('iniciar_sesion/', login_request, name='Iniciar Sesion'),
]
