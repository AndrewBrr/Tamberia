from django.urls import path
from apptamberia.views import portal, register_request, login_request, clienteCrear, clienteLista, clienteDetalles, clienteEditar, clienteBorrar, portal_2, pedidos
from apptamberia.views import productos, verCatalogo, formularioProductos, formularioPedidos
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('portal/', portal, name='Portal'),
    
    path('registro/', register_request, name='Registrarse'),
    #path('registrarUsuario/', registrarUsuario, name='registrarUsuario'),
    path('iniciar_sesion/', login_request, name='Iniciar Sesion'),
    path('logout/', LogoutView.as_view(template_name='apptamberia/logout.html'), name='logout'),
    
    path('clientes/list/', clienteLista.as_view(), name='clientes_lista'),
    path('clientes/<pk>', clienteDetalles.as_view(), name='cliente_detalles'),
    path('cliente/nuevo/', clienteCrear.as_view(), name='cliente_crear'),
    path('cliente/edicion/<pk>', clienteEditar.as_view(), name='cliente_editar'),
    path('cliente/borrar/<pk>', clienteBorrar.as_view(), name='cliente_borrar'),

    path('verCatalogo/', verCatalogo, name=('catalogo')),
    path('formularioProducto/', formularioProductos, name='Agregar Producto'),
    
    path('portal_2/', portal_2, name='portal_2'),

    path('formularioPedidos/', formularioPedidos, name='agregar_pedido'),
    path('pedidos/', pedidos, name=('pedidos'))


]
