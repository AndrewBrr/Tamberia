from django.shortcuts import render
from apptamberia.models import Productos, Usuarios
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
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>//REGISTRO Y LOGIN DE USUARIO>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

from apptamberia.forms import UserRegisterForm
def register_request(request): 

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
    
            usuario = form.cleaned_data.get('username')
            form.save()
            return render(request, 'apptamberia/usuario/nuevo/.html')

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
class usuarioLista(ListView):

    model = Usuarios
    template_name = 'apptamberia/usuarios.html'

class usuarioDetalles(DetailView):

    model = Usuarios
    template_name = 'apptamberia/usuariosDetalle.html'
    fields = ['nombre', 'apellido', 'email', 'telefono']  

class usuarioCrear(CreateView):

    model = Usuarios
    success_url = reverse_lazy('usuario_list.html')
    fields = ['nombre', 'apellido', 'email', 'telefono']   

class usuarioEditar(UpdateView):

    model = Usuarios
    template_name = reverse_lazy('usuarios.html')
    fields = ['nombre', 'apellido', 'email', 'telefono']  

class usuarioBorrar(DeleteView):

    model = Usuarios
    success_url = reverse_lazy('usuarios.html')
    

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>//LOGIN//>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
def login_request(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data= request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            password = form.cleaned_data.get('contraseña')

            user = authenticate(username=usuario, contraseña=password)

            if user is not None:
                login(request, user)
                return render(request, 'apptamberia/portal.html', {'mensaje': f'Bienvenido a TAMBERIA ALEMANA {usuario}'})
            else:
                return render(request, 'apptamberia/login.html', {"mensaje": "error al ingresar los datos, asegurese de ingresar los datos correctamente"})

        else:
            return render(request, 'apptamberia/portal.html', {"mensaje": "error de formulario"})
    else:
        form = AuthenticationForm()
        return render(request, 'apptamberia/login.html', {'form': form})
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>VER INFO DE USUARIO EN EL PERFIL>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def usuarios(request):
    
    user = Usuarios(nombre = 'nombre', apellido = 'apellido', email = 'email', telefono = 0)
    user.save()

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

