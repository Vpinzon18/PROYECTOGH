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
from principal.forms import FormularioForm, AseguramientoForm , FamiliarForm , FamiliarDiscapacidadForm, SituacionesAfectableForm, MascotasForm, TransportesForm, RecursosDigitalesForm, AppAprendizajeForm, OfrecimientosForm, DesarrolloPersonalForm, ReconocimientoEmpresarialForm, ActividadesCulturalesForm
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.views.generic.edit import FormView
import logging


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
    MascotasFormSet = formset_factory(MascotasForm, extra=1)

    if request.method == 'POST':
        user = request.user
        form_data = request.POST.copy()
        form_data['idUser'] = user.id

        form = FormularioForm(form_data, request.FILES)
        familiar_formset = FamiliarFormSet(request.POST, prefix='familiar')
        mascota_formset = MascotasFormSet(request.POST, prefix='mascota')
        aseguramiento_form = AseguramientoForm(request.POST)
        familiarDiscapacidad_form = FamiliarDiscapacidadForm(request.POST)
        situacionesafectable_form = SituacionesAfectableForm(request.POST)
        transporte_form = TransportesForm(request.POST)
        recursos_form = RecursosDigitalesForm(request.POST)
        appaprendizaje_form = AppAprendizajeForm(request.POST)
        ofrecimientos_form = OfrecimientosForm(request.POST)
        desarrollopersonal_form = DesarrolloPersonalForm(request.POST)
        reconocimientoempresarial_form = ReconocimientoEmpresarialForm(request.POST)

        if form.is_valid() and familiar_formset.is_valid() and aseguramiento_form.is_valid() and familiarDiscapacidad_form.is_valid() and situacionesafectable_form.is_valid() and mascota_formset.is_valid and transporte_form.is_valid() and recursos_form.is_valid() and appaprendizaje_form.is_valid() and ofrecimientos_form.is_valid() and desarrollopersonal_form.is_valid() and reconocimientoempresarial_form.is_valid():
            form.instance.idUser = user
            form.save()

            for familiar_form in familiar_formset:
                familiar_form.instance.idUser = user
                familiar_form.save()
                
            for mascota_form in mascota_formset:
                mascota_form.instance.idUser = user
                mascota_form.save()
             
            reconocimientoempresarial = reconocimientoempresarial_form.save(commit=False)  # Guardar manualmente el objeto aseguramiento
            reconocimientoempresarial.idUser = user
            reconocimientoempresarial.save()  
             
             
            desarrollopersonal = desarrollopersonal_form.save(commit=False)  # Guardar manualmente el objeto aseguramiento
            desarrollopersonal.idUser = user
            desarrollopersonal.save() 
                
            ofrecimiento = ofrecimientos_form.save(commit=False)  # Guardar manualmente el objeto aseguramiento
            ofrecimiento.idUser = user
            ofrecimiento.save()
            
            appaprendizaje = appaprendizaje_form.save(commit=False)  # Guardar manualmente el objeto aseguramiento
            appaprendizaje.idUser = user
            appaprendizaje.save()
            
            recursos = recursos_form.save(commit=False)  # Guardar manualmente el objeto aseguramiento
            recursos.idUser = user
            recursos.save()    
            
            transporte = transporte_form.save(commit=False)  # Guardar manualmente el objeto aseguramiento
            transporte.idUser = user
            transporte.save()
            
            aseguramiento = aseguramiento_form.save(commit=False)  # Guardar manualmente el objeto aseguramiento
            aseguramiento.idUser = user
            aseguramiento.save()
            
            familiarDiscapacidad = familiarDiscapacidad_form.save(commit=False)  # Guardar manualmente el objeto aseguramiento
            familiarDiscapacidad.idUser = user
            familiarDiscapacidad.save()
            
            situacionesafectable = situacionesafectable_form.save(commit=False)  # Guardar manualmente el objeto aseguramiento
            situacionesafectable.idUser = user
            situacionesafectable.save()

            return HttpResponse("La información se ha enviado correctamente")
        else:
            logger = logging.getLogger('principal')
            logger.error("Error en el formulario.")
            for error in form.errors:
                logger.error(f"Formulario: {error}: {form.errors[error]}")
            for familiar_form in familiar_formset:
                for error in familiar_form.errors:
                    logger.error(f"FamiliarForm: {error}: {familiar_form.errors[error]}")
            for mascota_form in mascota_formset:
                for error in mascota_form.errors:
                    logger.error(f"MascotasForm: {error}: {mascota_form.errors[error]}")        
            for error in aseguramiento_form.errors:
                logger.error(f"AseguramientoForm: {error}: {aseguramiento_form.errors[error]}")
            for error in familiarDiscapacidad_form.errors:
                logger.error(f"FamiliarDiscapacidadForm: {error}: {familiarDiscapacidad_form.errors[error]}")
            for error in situacionesafectable_form.errors:
                logger.error(f"SituacionesAfectableForm: {error}: {situacionesafectable_form.errors[error]}") 
            for error in transporte_form.errors:
                logger.error(f"TransporteForm: {error}: {transporte_form.errors[error]}") 
            for error in recursos_form.errors:
                logger.error(f"RecursosDigitalesForm: {error}: {recursos_form.errors[error]}")     
            for error in appaprendizaje_form.errors:
                logger.error(f"AppAprendizajeForm: {error}: {appaprendizaje_form.errors[error]}")     
            for error in ofrecimientos_form.errors:
                logger.error(f"OfrecimientosForm: {error}: {ofrecimientos_form.errors[error]}")  
            for error in desarrollopersonal_form.errors:
                logger.error(f"desarrollopersonalForm: {error}: {desarrollopersonal_form.errors[error]}")
            for error in reconocimientoempresarial_form.errors:
                logger.error(f"ReconocimientoEmpresarialForm: {error}: {reconocimientoempresarial_form.errors[error]}")
    else:
        form = FormularioForm()
        familiar_formset = FamiliarFormSet(prefix='familiar')
        mascota_formset = MascotasFormSet(prefix='mascota')
        aseguramiento_form = AseguramientoForm()
        familiarDiscapacidad_form = FamiliarDiscapacidadForm()
        situacionesafectable_form = SituacionesAfectableForm()
        transporte_form = TransportesForm()
        recursos_form = RecursosDigitalesForm()
        appaprendizaje_form = AppAprendizajeForm()
        ofrecimientos_form = OfrecimientosForm()
        desarrollopersonal_form = DesarrolloPersonalForm()
        reconocimientoempresarial_form = ReconocimientoEmpresarialForm()
        
    return render(
        request,
        "prueba.html",
        {'form': form,
         'familiar_formset': familiar_formset,
         'aseguramiento_form': aseguramiento_form,
         'familiarDiscapacidad_form':familiarDiscapacidad_form,
         'situacionesafectable_form':situacionesafectable_form,
         'mascota_formset':mascota_formset ,
         'transporte_form':transporte_form,
         'recursos_form':recursos_form,
         'appaprendizaje_form':appaprendizaje_form,
         'ofrecimientos_form': ofrecimientos_form,
         'desarrollopersonal_form': desarrollopersonal_form,
         'reconocimientoempresarial_form': reconocimientoempresarial_form
         })
















