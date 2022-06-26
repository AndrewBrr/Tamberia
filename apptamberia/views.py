from django.shortcuts import render
from apptamberia.models import Productos, Clientes, Pedidos
from django.http import HttpResponse
from django.template import loader
from apptamberia.forms import Formulario_Productos
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>//PORTAL DE LA PAGINA//>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
def portal(request):
    
    plantilla = loader.get_template('apptamberia/portal.html')
    pantalla_inicio = plantilla.render()
    return HttpResponse(pantalla_inicio)

def portal_2(request):

    plantilla = loader.get_template('apptamberia/portal_2.html')
    pantalla_loged = plantilla.render()
    return HttpResponse(pantalla_loged)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>//REGISTRO Y LOGIN DE USUARIO>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

from apptamberia.forms import UserRegisterForm
def register_request(request): 

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
    
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'apptamberia/portal_2.html')

        else:
            return render(request, 'apptamberia/portal.html', {'mensaje': f'error detectado al introducir los datos, for favor asegurate de que sean correctos o validos'})
    else:
        form = UserRegisterForm()
        return render(request, 'apptamberia/registro.html', {'form': form})


from apptamberia.forms import Formulario_Usuario
#def registrarUsuario(request):
    
    #if request.method == 'POST':
        #form_registro = Formulario_Usuario(request.POST)
        #print(form_registro)

        #if form_registro.is_valid:
            #datos = form_registro.cleaned_data

            #usuario = Usuarios(nombre=datos['nombre'], apellido=datos['apellido'], direccion=datos['direccion'], email=datos['email'], telefono=datos['telefono'])
            #usuario.save()

            #respuesta = 'Te has registrado correctamente'
            #return render(request, 'apptamberia/portal.html', respuesta)
    #else: 
        #form_registro = Formulario_Usuario()
    #return render(request, 'apptamberia/registrarUsuario.html', {'form_registro':form_registro})


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>//CRUD PARA LA CREACION DE USUARIO LUEGO DEL REGISTRO//>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class clienteLista(ListView):

    model = Clientes
    template_name = 'apptamberia/cliente_list.html'

class clienteDetalles(DetailView):

    model = Clientes
    template_name = 'apptamberia/clienteDetalles.html'
    fields = ['nombre', 'apellido', 'email', 'telefono']  

class clienteCrear(CreateView):

    model = Clientes
    success_url = reverse_lazy('cliente_lista')
    fields = ['nombre', 'apellido', 'email', 'telefono']   

class clienteEditar(UpdateView):

    model = Clientes
    template_name = reverse_lazy('cliente_editar')
    fields = ['nombre', 'apellido', 'email', 'telefono']  

class clienteBorrar(DeleteView):

    model = Clientes
    success_url = reverse_lazy('cliente_borrar')
    

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>//LOGIN//>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
def login_request(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data= request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('contraseña')

            user = authenticate(username=user, contraseña=password)

            if user is not None:
                login(request, user)
                return render(request, 'apptamberia/portal_2.html', {'mensaje': f'Bienvenido a TAMBERIA ALEMANA {username}'})
            else:
                return render(request, 'apptamberia/login.html', {"mensaje": "error al ingresar los datos, asegurese de ingresar los datos correctamente"})

        else:
            return render(request, 'apptamberia/portal.html', {"mensaje": "error de formulario"})
    else:
        form = AuthenticationForm()
        return render(request, 'apptamberia/login.html', {'form': form})


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>VER INFO DE USUARIO EN EL PERFIL>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def clientes(request):
    
    client = Clientes(nombre = 'nombre', apellido = 'apellido', email = 'email', telefono = 0)
    client.save()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>LISTA DE PRODUCTOS PARA EL CATALOGO>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def productos(request):
    
    sardo = Productos(nombre = 'sardo', calidad = 'duro', tipo = 'horma', precio = 1200)
    sardo.save()

def reggianos(request):
    reggiano = Productos(nombre = 'reggiano', calidad = 'duro', tipo = 'horma', precio = 3000)
    reggiano.save()

def  provolones(request):
    provolone = Productos(nombre = 'provolone', calidad = 'duro', tipo = 'duro', precio = 2000)
    provolone.save()

def verCatalogo(request):
    
    catalogo = Productos.objects.all()
    contexto = {'catalogo': catalogo}

    return render(request, 'apptamberia/catalogo.html', contexto)

def formularioProductos(request):
    
    if request.method == 'POST':
        formulario = Formulario_Productos(request.POST)
        print(formulario)

        if formulario.is_valid:
            datos = formulario.cleaned_data

            producto = Productos(nombre=datos['nombre'], calidad=datos['calidad'], tipo=datos['tipo'], precio=datos['precio'])
            producto.save()
            

            respuesta = 'Datos registrados correctamente'
            return render(request, 'apptamberia/portal.html', {'mensaje': f'Producto archivado correctamente'})
            
            

    else: 
        formulario = Formulario_Productos()
    return render(request, 'apptamberia/formularioProductos.html', {'formulario':formulario})

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  REGISTRO DE PEDIDOS DE LOS CLIENTES >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

from apptamberia.forms import Formulario_Pedidos


def formularioPedidos(request):

    if request.method=='POST':
        form_pedido = Formulario_Pedidos(request.POST)
        print(form_pedido)

        if form_pedido.is_valid():

            campos = form_pedido.cleaned_data

            pedido = Pedidos(cliente=campos['cliente'], direccion=campos['direccion'], email=campos['email'], telefono=campos['telefono'], pedido=campos['pedido'])
            pedido.save()

            return render(request, 'apptamberia/portal_2.html', {'mensaje': 'pedido registrado correctamente'})
        
    else:
        form_pedido = Formulario_Pedidos()
        return render(request, 'apptamberia/formularioPedidos.html', {'form_pedido': form_pedido})



def pedidos(request):

    lista_pedidos = Pedidos.objects.all()
    contexto = {'lista_pedidos': lista_pedidos}

    return render(request, 'apptamberia/pedidos.html')

