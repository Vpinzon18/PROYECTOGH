from django.shortcuts import render
from principal.models import nuevoUsuario
from pyexpat.errors import messages

def login(request):
    context={}
    return render(request, 'login.html', context)

def inicio(request):
    context={}
    return render(request, 'index.html', context)

def usuarios(request):
    context={}
    return render(request, 'usuarios.html', context)

def formulario(request):
    context={}
    return render(request, 'formulario.html', context) 

def datos(request):
    context={}
    return render(request, 'datos.html', context)

def certificados(request):
    context={}
    return render(request, 'certificados.html', context)

def paginalogin(request):
    if request.method=='POST':
        
        try:
            detalleUsuario=nuevoUsuario.objects.get(Documento=request.POST['correo'], Clave=request.POST['password'])
            print("Usuario=", detalleUsuario)
            request.session['Documento']= detalleUsuario.Documento
            return render(request, 'inicio') 
        except nuevoUsuario.DoesNotExist as e:
            messages.success(request, 'nombre de usuario o password no es correcto...!')
    return render(request, 'login')        