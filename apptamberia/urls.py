from django.urls import path
from apptamberia.views import portal, register_request, login_request, usuarioCrear, usuarioLista, usuarioDetalles, usuarioEditar, usuarioBorrar
from apptamberia.views import productos, verCatalogo, formularioProductos
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('portal/', portal, name='Portal'),

    path('registro/', register_request, name='Registrarse'),
    #path('registrarUsuario/', registrarUsuario, name='registrarUsuario'),
    path('iniciar_sesion/', login_request, name='Iniciar Sesion'),
    path('logout/', LogoutView.as_view(template_name='apptamberia/logout.html'), name='logout'),
    
    path('usuario/list/', usuarioLista.as_view(), name='usuario_lista'),
    path('usuario/<pk>', usuarioDetalles.as_view(), name='usuario_detalles'),
    path('usuario/nuevo/', usuarioCrear.as_view(), name='usuario_crear'),
    path('usuario/edicion/<pk>', usuarioEditar.as_view(), name='usuario_editar'),
    path('usuario/borrar/<pk>', usuarioBorrar.as_view(), name='usuario_borrar'),

    path('verCatalogo/', verCatalogo, name=('catalogo')),
    path('formularioProducto/', formularioProductos, name='Agregar Producto')


]
