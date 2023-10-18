from django.shortcuts import render, redirect
from pyexpat.errors import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.models import User
from django.http import HttpResponse  
from principal.functions import handle_uploaded_file  #functions.py
from principal.forms import FormularioForm, AseguramientoForm , FamiliarForm 
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.views.generic.edit import FormView
import logging


##(request, 'login.html', context)

def inicio(request):
    context={}
    return render(request, 'index.html', context)


def usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})



def formularioII(request):
    context={}
    return render(request, 'Formulariopag2.html', context) 

def datos(request):
    context={}
    return render(request, 'datos.html', context)

def certificados(request):
    context={}
    return render(request, 'certificados.html', context)


def signup(request):
  
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            
            return redirect('/usuarios')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
   
def home(request): 
    return render(request, 'usuarios.html')
   
  
def signin(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio') #profile
        else:
            msg = 'Usuario o Contraseña Incorrecta'
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
  
def profile(request): 
    return render(request, 'profile.html')
   
def signout(request):
    logout(request)
    return redirect('/')

def registrarUsuario(request):
    Nombre = request.POST['txtNombre']
    Apellido = request.POST['txtApellido']
    Email = request.POST['txtEmail']
    Username = request.POST['txtUsername']
    Password = request.POST['txtPassword']
    
    usuario = User.objects.create(
        first_name=Nombre, last_name=Apellido, email=Email, username=Username, password=Password)
    return redirect('usuarios')

    
def eliminarUsuario(request, id):
    usuario = User.objects.get(id=id)
    usuario.delete()    
    return redirect('usuarios')


def edicionUsuario(request, id):
    usuario = User.objects.get(id=id)
    return render(request, "edicionUsuario.html", {"usuario": usuario})


def editarUsuario(request):
    id = request.POST['txtid']
    Nombre = request.POST['txtNombre']
    Apellido = request.POST['txtApellido']
    Email = request.POST['txtEmail']
    Username = request.POST['txtUsername']
    
    
    usuario = User.objects.get(id=id)
    usuario.first_name = Nombre
    usuario.last_name = Apellido
    usuario.email = Email
    usuario.username = Username
    usuario.save()
    
    return redirect('usuarios')

 

def prueba(request):
    FamiliarFormSet = formset_factory(FamiliarForm, extra=1)

    if request.method == 'POST':
        user = request.user
        form_data = request.POST.copy()
        form_data['idUser'] = user.id

        form = FormularioForm(form_data, request.FILES)
        familiar_formset = FamiliarFormSet(request.POST, prefix='familiar')

        # Manejar el formulario AseguramientoForm
        aseguramiento_form = AseguramientoForm(request.POST)

        if form.is_valid() and familiar_formset.is_valid() and aseguramiento_form.is_valid():
            form.instance.idUser = user
            form.save()

            for familiar_form in familiar_formset:
                familiar_form.instance.idUser = user
                familiar_form.save()

            aseguramiento = aseguramiento_form.save(commit=False)  # Guardar manualmente el objeto aseguramiento
            aseguramiento.idUser = user
            aseguramiento.save()

            return HttpResponse("La información se ha enviado correctamente")
        else:
            logger = logging.getLogger('principal')
            logger.error("Error en el formulario.")
            for error in form.errors:
                logger.error(f"Formulario: {error}: {form.errors[error]}")
            for familiar_form in familiar_formset:
                for error in familiar_form.errors:
                    logger.error(f"FamiliarForm: {error}: {familiar_form.errors[error]}")
            for error in aseguramiento_form.errors:
                logger.error(f"AseguramientoForm: {error}: {aseguramiento_form.errors[error]}")

    else:
        form = FormularioForm()
        familiar_formset = FamiliarFormSet(prefix='familiar')
        aseguramiento_form = AseguramientoForm()

    return render(
        request,
        "prueba.html",
        {'form': form, 'familiar_formset': familiar_formset, 'aseguramiento_form': aseguramiento_form}
    )
















