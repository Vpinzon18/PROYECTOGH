from django.shortcuts import render, redirect
from pyexpat.errors import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.models import User

##(request, 'login.html', context)

def inicio(request):
    context={}
    return render(request, 'index.html', context)


def usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})


def formulario(request):
    context={}
    return render(request, 'formulario.html', context) 

def datos(request):
    context={}
    return render(request, 'datos.html', context)

def certificados(request):
    context={}
    return render(request, 'certificados.html', context)


def signup(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/formulario')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
   
def home(request): 
    return render(request, 'home.html')
   
  
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
    


