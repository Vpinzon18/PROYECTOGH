from django.shortcuts import render, redirect, get_object_or_404
from pyexpat.errors import messages
from django.contrib import messages 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.models import User
from django.http import HttpResponse  
from principal.functions import handle_uploaded_file  #functions.py
from principal.forms import FormularioForm, AseguramientoForm ,HistorialEducativoForm,FamiliarForm , FamiliarDiscapacidadForm, SituacionesAfectableForm, MascotasForm, TransportesForm, RecursosDigitalesForm, AppAprendizajeForm, OfrecimientosForm, DesarrolloPersonalForm, ReconocimientoEmpresarialForm, ActividadesCulturalesForm, ActividadesSaludForm, TiempoLibreForm, EnfermedadesForm , DeportesForm, MolestiasSeisMesesForm, MolestiasVozForm,SintomasAudicionForm, ContratacionForm
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.views.generic.edit import FormView
from .models import formularioForm ,contratacionForm,historialeducativoFormn,actividadesculturalesForm,deporteForm,molestaseismesesForm,sintomasaudicionForm,molestiasvozForm,enfermedadesForm, tiempolibreForm, actividadessaludForm, reconocimientoempresarialForm, aseguramientoForm,familiarForm, familiardiscapacidadForm, situacionesafectableForm, mascotasForm,transorteForm, recursosdigitales, appaprendizajeForm, ofrecimientoForm, desarrollopersonalForm
import logging
from django.core.paginator import Paginator


def inicio(request):
    context={}
    return render(request, 'index.html', context)

def usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})

def formularioII(request):
    context={}
    return render(request, 'formulario.html', context) 

def datos(request):
    # Obtener todos los usuarios en la base de datos
    bdcolaboradore = User.objects.all()
    form = formularioForm.objects.all()

    return render(request, 'datos.html', {'bdcolaboradore': bdcolaboradore, 'form': form})


def Info_Familiar_DB(request,idUser_id):
    
    familiar_Info = familiarForm.objects.filter(idUser_id=idUser_id)
    
    return render(request, 'bd_colaboradores_hijos.html', {'familiar_Info': familiar_Info,'idUser_id':idUser_id} )

def Info_Mascotas_DB(request, idUser_id):
    
    Mascotas_Info = mascotasForm.objects.filter(idUser_id=idUser_id)
    
    return render(request, 'bd_colaboradores_mascotas.html', {'Mascotas_Info': Mascotas_Info, 'idUser_id':idUser_id})

















def DataColaboradores(request):
    context={}
    return render(request, 'datacolaboradores.html', context) 
# ESTE ES LA CONSULTA PARA EL MODULO DE DB COLABORADORES ESTA CONSULTA OBTINENE TODOS LOS DATOS REGISTRADOS TANTO EN EL FOMRULARIO COM ADATOS ADICIONALES AÑADIDOS POR LOS USUARIOS DE GESTION HUMANA
def bd_colaboradores_Contratacion(request,idUser_id):
    try:
        form_con = contratacionForm.objects.filter(idUser_id=idUser_id)
        formulario_Contratacion = [ContratacionForm(instance=form_con) for form_con in form_con]
        print("Estos son los formularios Mascotas:", formulario_Contratacion)
    except contratacionForm.DoesNotExist:
        formulario_Contratacion = None
    return render(request, 'bd_colaboradores_Contratacion.html',{'idUser_id':idUser_id,'formulario_Contratacion':formulario_Contratacion })
  
def bd_colaboradores_Educacion(request,idUser_id):
    try:
        form_edu = historialeducativoFormn.objects.filter(idUser_id=idUser_id)
        formulario_Educacion = [HistorialEducativoForm(instance=form_edu) for form_edu in form_edu]
        print("Estos son los formularios Mascotas:", formulario_Educacion)
    except historialeducativoFormn.DoesNotExist:
        formulario_Educacion = None
    return render(request, 'bd_colaboradores_Educacion.html',{'idUser_id':idUser_id,'formulario_Educacion':formulario_Educacion })
  
# def bd_colaboradores_mascotas(request,idUser_id):
#     try:
#         form_M = mascotasForm.objects.filter(idUser_id=idUser_id)
#         formulario_Mascotas = [MascotasForm(instance=Form_Mas--) for Form_Mas in form_M]
#         print("Estos son los formularios Mascotas:", formulario_Mascotas)
#     except mascotasForm.DoesNotExist:
#         formulario_Mascotas = None
#     return render(request, 'bd_colaboradores_mascotas.html',{'idUser_id':idUser_id,'formulario_Mascotas':formulario_Mascotas })
 
 
        


def agregar_familiar(request, idUser_id):
    if request.method == 'POST':
        form = FamiliarForm(request.POST)
        
        if form.is_valid():
            familiar = form.save(commit=False)
            familiar.idUser_id = idUser_id  # Asigna el ID del usuario que estás editando al familiar
            familiar.save()  # Esto creará un nuevo registro de familiar en la base de datos asociado al usuario que estás editando
            return redirect('datos')  # Redirige a donde desees después de agregar

    else:
        form = FamiliarForm()  # Crea una instancia de formulario vacía para mostrar en el formulario HTML

    return render(request, 'AgregarFamiliar.html', {'familiar_formulario': form})




def editar_familiar(request, familiar_id):
    try:
        familiar = familiarForm.objects.get(id_Familiar=familiar_id)
        if request.method == 'POST':
            form = FamiliarForm(request.POST, instance=familiar)  # Reemplaza "TuFormulario" con el nombre real de tu formulario
            if form.is_valid():
                form.save()  # Esto actualizará automáticamente el familiar existente
                return redirect('datos')  # Redirige a donde desees después de guardar

        else:
            form = FamiliarForm(instance=familiar)  # Reemplaza "TuFormulario" con el nombre real de tu formulario

    except familiarForm.DoesNotExist:
        form = None

    return render(request, 'Editar_Info_familiar_DB.html', {'familiar_formulario': form})

def eliminar_familiar(request, familiar_id):
    try:
        familiar = familiarForm.objects.get(id_Familiar=familiar_id)
        familiar.delete()  # Esto eliminará el familiar
        return redirect('datos')  # Redirige a donde desees después de eliminar

    except familiarForm.DoesNotExist:
        familiar = None  # Define "familiar" como None por defecto # Puedes manejar esta situación de acuerdo a tus necesidades

    return render(request, 'datos.html', {'familiar': familiar})




# def editar_familiar(request, familiar_id):
#     # Obtén el familiar de la base de datos usando el ID proporcionado
#     try:
#         familiar = familiarForm.objects.get(familiar_id=familiar_id)
#     except familiarForm.DoesNotExist:
#         # Puedes manejar el caso en que el familiar no existe
#         return HttpResponse("Familiar no encontrado")

#     # Verifica si el usuario tiene permiso para editar este familiar (opcional)

#     # Procesa el formulario de edición si se envía a través de POST
#     if request.method == 'POST':
#         form = FamiliarForm(request.POST, instance=familiar)
#         if form.is_valid():
#             form.save()
#             # Redirige a la página de detalle del familiar o a donde desees
#             return HttpResponseRedirect('/Info_Familiar_DB/' + str(familiar_id))
    
#     # Si no es una solicitud POST, muestra el formulario de edición
#     else:
#         form = FamiliarForm(instance=familiar)
    
#     return render(request, 'editar_familiar.html', {'form': form, 'familiar': familiar})





# def Actualizar_Hjios(request, idUser_id):
#     if not request.user.is_authenticated:
#         return redirect('/') 
    
#     if request.method == 'POST':
        
#         form_f = familiarForm.objects.filter(idUser_id=idUser_id)
#         formularios_familiares = [FamiliarForm(request.POST, instance=form) for form in form_f]
        
#         if  all([f.is_valid() for f in formularios_familiares]):
            
#             for f, form_familiar in zip(form_f, formularios_familiares):
#                 form_familiar.save()
                
#             return redirect('datos')
#         else:
#             print("Error en los formularios. Revise los campos.")
#             for f in formularios_familiares:
#                 messages.error(request, f"Error en formulario familiar: {f.errors.as_text()}")
#     else:
#             form_f = familiarForm.objects.filter(idUser_id=idUser_id)
#             formularios_familiares = [FamiliarForm(instance=form) for form in form_f]
       
#     return render(request, 'bd_colaboradores_hijos.html',{'idUser_id':idUser_id,'formularios_familiares':formularios_familiares} )

# def Agregar_Familiar(request):
#     FamiliarFormSet_Hijo = formset_factory(FamiliarForm, extra=1)
#     if request.method == 'POST':
#         user = request.user
#         form_data = request.POST.copy()
#         form_data['idUser'] = user.id
        
#         FamiliarFormSet_Hijo = FamiliarFormSet_Hijo(request.POST, prefix='familiar')
        
#         if FamiliarFormSet_Hijo.is_valid():
        
#              for familiar_formulario in FamiliarFormSet_Hijo:
#                  familiar_formulario.instance.idUser = user
#                  familiar_formulario.save()
#                  return HttpResponse("datos")
#              else:
#                   logger = logging.getLogger('principal')
#                   logger.error("Error en el formulario.")
#                   for familiar_formulario in FamiliarFormSet_Hijo:
#                       for error in familiar_formulario.errors:
#                        logger.error(f"FamiliarForm: {error}: {familiar_formulario.errors[error]}")
                       
#         else:
#              FamiliarFormSet_Hijo = FamiliarFormSet_Hijo(prefix='familiar_formulario')
             
#         return render (request, "bd_claboradores_hijos.html",{'FamiliarFormSet_Hijo': FamiliarFormSet_Hijo,})
                
    

def bd_colaboradores(request, idUser_id):
    print("este es el form", idUser_id)  
    try:
        # formulario sociodemografico
        form_Sociodemografico = formularioForm.objects.get(idUser_id=idUser_id)
        print("este es el form", form_Sociodemografico)
        form = FormularioForm(instance=form_Sociodemografico)
        print("este es el form", form)
        # formulario aseguramiento
        form_aseguramiento = aseguramientoForm.objects.filter(idUser_id=idUser_id)
        form_a = AseguramientoForm(instance=form_aseguramiento[0]) 
        print("este es el form aseguramiento", form_a)
        # formualrio familiares
       
        # formulario discapacidad familiar
        form_d = familiardiscapacidadForm.objects.filter(idUser_id=idUser_id)
        formulario_discapacidad = FamiliarDiscapacidadForm(instance=form_d[0]) 
        print("este es el form aseguramiento", formulario_discapacidad)
        # formulario de situaciones afectables
        form_s = situacionesafectableForm.objects.filter(idUser_id=idUser_id)
        formulario_situacion = SituacionesAfectableForm(instance=form_s[0]) 
        print("este es el form situacoiones afectables", formulario_situacion)
        # formulario mascotas
        
        # formulario transportes
        form_t = transorteForm.objects.filter(idUser_id=idUser_id)
        transporte_form = TransportesForm(instance=form_t[0]) 
        print("este es el form transporte", transporte_form)
        # formulario recursos digitales
        form_recur = recursosdigitales.objects.filter(idUser_id=idUser_id)
        recursos_form = RecursosDigitalesForm(instance=form_recur[0]) 
        print("este es el form recursos", recursos_form)
        # formulario recursos para aprendizaje 
        form_apre = appaprendizajeForm.objects.filter(idUser_id=idUser_id)
        appaprendizaje_form = AppAprendizajeForm(instance=form_apre[0]) 
        print("este es el form aplicaciones para aprendizaje", appaprendizaje_form)
        # formulario ofrecimientos empresariales 
        form_ofre = ofrecimientoForm.objects.filter(idUser_id=idUser_id)
        ofrecimientos_form = OfrecimientosForm(instance=form_ofre[0]) 
        print("este es el form aplicaciones para los ofreciminetos empresarioes ", ofrecimientos_form)
        # formulario desarrollo personal 
        form_desa = desarrollopersonalForm.objects.filter(idUser_id=idUser_id)
        desarrollopersonal_form = DesarrolloPersonalForm(instance=form_desa[0]) 
        print("este es el form aplicaciones para los desarrollos personales ", desarrollopersonal_form)
        # formulario Reconocmienot 
        form_reco = reconocimientoempresarialForm.objects.filter(idUser_id=idUser_id)
        reconocimientoempresarial_form = ReconocimientoEmpresarialForm(instance=form_reco[0]) 
        print("este es el form aplicaciones para los desarrollos personales ", reconocimientoempresarial_form)
        # formulario actividades culturales
        form_cultu = actividadesculturalesForm.objects.filter(idUser_id=idUser_id)
        actividadesculturales_form = ActividadesCulturalesForm(instance=form_cultu[0]) 
        print("este es el form aplicaciones para las activiadades culturales ", actividadesculturales_form)
        # formulario actividades Salud 
        form_salud = actividadessaludForm.objects.filter(idUser_id=idUser_id)
        actividadessalud_form = ActividadesSaludForm(instance=form_salud[0]) 
        print("este es el form aplicaciones para las activiadades de salud", actividadessalud_form)
        # formulario actividades Tiempo libre
        form_libre = tiempolibreForm.objects.filter(idUser_id=idUser_id)
        tiempolibre_form = TiempoLibreForm(instance=form_libre[0]) 
        print("este es el form aplicaciones para las activiadades de tiempo libre", tiempolibre_form)
         # formulario Enfermedades diagnosticadas
        form_enfe = enfermedadesForm.objects.filter(idUser_id=idUser_id)
        enfermedades_form = EnfermedadesForm(instance=form_enfe[0]) 
        print("este es el form aplicaciones para las activiadades de tiempo libre", enfermedades_form)
        # formulario deportes en practica 
        form_depo = deporteForm.objects.filter(idUser_id=idUser_id)
        deportes_form = DeportesForm(instance=form_depo[0]) 
        print("este es el form aplicaciones para las activiadades deportivas ", deportes_form)
        # formulario molestias en los ultimos 6 meses 
        form_mole = molestaseismesesForm.objects.filter(idUser_id=idUser_id)
        molestiasseismeses_form = MolestiasSeisMesesForm(instance=form_mole[0]) 
        print("este es el form  para las molestias en los ultimos seis meses  ", molestiasseismeses_form)
        # formulario molestias en los ultimos 6 meses en la voz 
        form_voz = molestiasvozForm.objects.filter(idUser_id=idUser_id)
        molestiasvoz_form = MolestiasVozForm(instance=form_voz[0]) 
        print("este es el form para las molestias en los ultimos seis meses en la VOZ ", molestiasvoz_form)
        # formulario CAMBIOS  en los ultimos 6 meses en la voz 
        form_saudicio = sintomasaudicionForm.objects.filter(idUser_id=idUser_id)
        sintomasaudicion_form = SintomasAudicionForm(instance=form_saudicio[0]) 
        print("este es el form sintomas de audicion", sintomasaudicion_form)
    except formularioForm.DoesNotExist and  aseguramientoForm.DoesNotExist and  familiarForm.DoesNotExist:
        form = None
        form_a = None
        
        formulario_discapacidad = None
        formulario_situacion = None
        
        transporte_form = None
        recursos_form = None
        appaprendizaje_form = None
        ofrecimientos_form = None
        desarrollopersonal_form = None
        reconocimientoempresarial_form = None
        actividadesculturales_form = None
        actividadessalud_form = None
        tiempolibre_form = None
        enfermedades_form= None
        deportes_form= None
        molestiasseismeses_form = None
        molestiasvoz_form = None
        sintomasaudicion_form = None
    
    return render(request, 'bd_colaboradores.html',
                  {'form': form,
                   'idUser_id': idUser_id,
                   'form_a':form_a ,
                    
                    'formulario_discapacidad':formulario_discapacidad,
                    'formulario_situacion':formulario_situacion,
                    'transporte_form':transporte_form,
                    'recursos_form': recursos_form,
                    'appaprendizaje_form': appaprendizaje_form,
                    'ofrecimientos_form': ofrecimientos_form,
                    'desarrollopersonal_form': desarrollopersonal_form,
                    'reconocimientoempresarial_form': reconocimientoempresarial_form,
                    'actividadesculturales_form': actividadesculturales_form,
                    'actividadessalud_form':actividadessalud_form,
                    'tiempolibre_form':tiempolibre_form,
                    'enfermedades_form':enfermedades_form,
                    'deportes_form': deportes_form,
                    'molestiasseismeses_form': molestiasseismeses_form,
                    'molestiasvoz_form': molestiasvoz_form,
                    'sintomasaudicion_form':sintomasaudicion_form
                
                   })

 # Importa el módulo de mensajes

def ActualizacionDatosColaboradores(request, idUser_id):
    # Asegúrate de que el usuario esté autenticado
    if not request.user.is_authenticated:
        return redirect('/')  # Redirige al inicio de sesión si el usuario no está autenticado

    try:
        form1 = formularioForm.objects.get(idUser_id=idUser_id)
    except formularioForm.DoesNotExist:
        # Manejo de errores si no se encuentra el formulario
        print("El formulario no existe.")
        messages.error(request, "El formulario no existe.")  # Agrega un mensaje de error
        return HttpResponse("El formulario no existe.")

    try:
        form_aseguramiento = aseguramientoForm.objects.get(idUser_id=idUser_id)
    except aseguramientoForm.DoesNotExist:
        form_aseguramiento = None

    try:
        form_d = familiardiscapacidadForm.objects.get(idUser_id=idUser_id)
    except familiardiscapacidadForm.DoesNotExist:
        form_d = None

    print("Datos del formulario de discapacidad:", form_d)  # Agrega este print

    if request.method == 'POST':
        form = FormularioForm(request.POST, instance=form1)
        form_a = AseguramientoForm(request.POST, instance=form_aseguramiento)
        form_d = FamiliarDiscapacidadForm(request.POST, instance=form_d)

        # Agrega la lógica de actualización de los formularios familiares
        form_f = familiarForm.objects.filter(idUser_id=idUser_id)
        formularios_familiares = [FamiliarForm(request.POST, instance=form) for form in form_f]

        if form.is_valid() and form_a.is_valid() and form_d.is_valid() and all([f.is_valid() for f in formularios_familiares]):
            form.save()
            form_a.save()
            form_d.save()
            for f, form_familiar in zip(form_f, formularios_familiares):
                form_familiar.save()
            print("Los formularios se han actualizado con éxito.")
            return redirect('datos')  # Redirige a la lista de formularios u otra vista que desees
        else:
            print("Error en los formularios. Revise los campos.")
            messages.error(request, "Error en los formularios. Revise los campos: {}".format(form.errors.as_text() + form_a.errors.as_text() + form_d.errors.as_text()))
            # Agrega errores de formularios familiares a los mensajes
            for f in formularios_familiares:
                messages.error(request, f"Error en formulario familiar: {f.errors.as_text()}")
    else:
        form = FormularioForm(instance=form1)
        form_a = AseguramientoForm(instance=form_aseguramiento)
        form_discapacidad = FamiliarDiscapacidadForm(instance=form_d)

        # Obtén los formularios familiares para mostrar en la plantilla
        form_f = familiarForm.objects.filter(idUser_id=idUser_id)
        formularios_familiares = [FamiliarForm(instance=form) for form in form_f]

    # Aquí creas un contexto con los datos de los formularios para pasar a la plantilla
    context = {
        'form': form,
        'form_a': form_a,
        'form_d': form_d,
        'formularios_familiares': formularios_familiares,
        'idUser_id': idUser_id,
    }

    return render(request, 'bd_colaboradores.html', context)


def PowerBi(request):
    context={}
    return render(request, 'PowerBi.html', context)

def certificados(request):
    context={}
    return render(request, 'certificados.html', context)

def signup(request):
    if request.method == 'POST':
        # Crea un formulario con los campos adicionales
        form = UserCreationForm(request.POST)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        # Valida y guarda el formulario
        if form.is_valid():
            user = form.save()
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/usuarios')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})
  


def signin(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            msg2 = '¡Bienvenido! Has iniciado sesión con éxito.'
            messages.success(request,msg2 )  # Agrega el mensaje de bienvenida
            return redirect('inicio')  # Reemplaza 'inicio' con la URL correcta
        else:
            msg = 'Usuario o Contraseña Incorrecta'
            form = AuthenticationForm(request.POST)
            messages.error(request, msg)  # Agrega el mensaje de error
            return render(request, 'login.html', {'form': form})
    
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
    if request.method == 'POST':
        id = request.POST['txtid']
        Nombre = request.POST['txtNombre']
        Apellido = request.POST['txtApellido']
        Email = request.POST['txtEmail']
        Username = request.POST['txtUsername']
        Password = request.POST['txtPassword']
        Estado = request.POST.get('txtEstado')  # Recuperar el valor del checkbox

        usuario = User.objects.get(id=id)
        usuario.first_name = Nombre
        usuario.last_name = Apellido
        usuario.email = Email
        usuario.username = Username
        usuario.set_password(Password)

        # Verifica si el checkbox está marcado
        if Estado == 'on':
            usuario.is_active = True
        else:
            usuario.is_active = False

        usuario.save()

        return redirect('usuarios')

    # Si la solicitud no es POST, renderiza la página de edición
    return render(request, 'editar_usuario.html')

def prueba(request):
    FamiliarFormSet = formset_factory(FamiliarForm, extra=1)
    MascotasFormSet = formset_factory(MascotasForm, extra=1)
    EducacionFormSet = formset_factory(HistorialEducativoForm, extra=1)

    if request.method == 'POST':
        user = request.user
        form_data = request.POST.copy()
        form_data['idUser'] = user.id

        form = FormularioForm(form_data, request.FILES)
        familiar_formset = FamiliarFormSet(request.POST, prefix='familiar')
        mascota_formset = MascotasFormSet(request.POST, prefix='mascota')
        Educacion_FormSet = EducacionFormSet(request.POST, prefix='Educacion')
        aseguramiento_form = AseguramientoForm(request.POST)
        familiarDiscapacidad_form = FamiliarDiscapacidadForm(request.POST)
        situacionesafectable_form = SituacionesAfectableForm(request.POST)
        transporte_form = TransportesForm(request.POST)
        recursos_form = RecursosDigitalesForm(request.POST)
        appaprendizaje_form = AppAprendizajeForm(request.POST)
        ofrecimientos_form = OfrecimientosForm(request.POST)
        desarrollopersonal_form = DesarrolloPersonalForm(request.POST)
        reconocimientoempresarial_form = ReconocimientoEmpresarialForm(request.POST)
        actividadesculturales_form = ActividadesCulturalesForm(request.POST)
        actividadessalud_form = ActividadesSaludForm(request.POST)
        tiempolibre_form =TiempoLibreForm(request.POST)
        enfermedades_form = EnfermedadesForm(request.POST)
        deportes_form = DeportesForm(request.POST)
        molestiasseismeses_form = MolestiasSeisMesesForm(request.POST)
        molestiasvoz_form = MolestiasVozForm(request.POST)
        sintomasaudicion_form = SintomasAudicionForm(request.POST)

        if form.is_valid() and familiar_formset.is_valid() and Educacion_FormSet.is_valid() and aseguramiento_form.is_valid() and familiarDiscapacidad_form.is_valid() and situacionesafectable_form.is_valid() and mascota_formset.is_valid and transporte_form.is_valid() and recursos_form.is_valid() and appaprendizaje_form.is_valid() and ofrecimientos_form.is_valid() and desarrollopersonal_form.is_valid() and reconocimientoempresarial_form.is_valid and actividadesculturales_form.is_valid() and  actividadessalud_form.is_valid()  and  tiempolibre_form.is_valid() and enfermedades_form.is_valid() and deportes_form.is_valid() and molestiasseismeses_form.is_valid() and molestiasvoz_form.is_valid():
            form.instance.idUser = user
            form.save()

            for familiar_form in familiar_formset:
                familiar_form.instance.idUser = user
                familiar_form.save()
                
            for Educacion_Form in Educacion_FormSet:
                Educacion_Form.instance.idUser = user
                Educacion_Form.save()
                
            for mascota_form in mascota_formset:
                mascota_form.instance.idUser = user
                mascota_form.save()
            
            sintomasaudicion = sintomasaudicion_form.save(commit=False)  # Guardar manualmente el objeto aseguramiento
            sintomasaudicion.idUser = user
            sintomasaudicion.save()
            
            molestiasvoz = molestiasvoz_form.save(commit=False)  # Guardar manualmente el objeto aseguramiento
            molestiasvoz.idUser = user
            molestiasvoz.save()
            
            molestias = molestiasseismeses_form.save(commit=False)  # Guardar manualmente el objeto aseguramiento
            molestias.idUser = user
            molestias.save()
            
            deportes = deportes_form.save(commit=False)  # Guardar manualmente el objeto aseguramiento
            deportes.idUser = user
            deportes.save()
            
            enfermedades = enfermedades_form.save(commit=False)  # Guardar manualmente el objeto aseguramiento
            enfermedades.idUser = user
            enfermedades.save() 
            
            tiempolibre = tiempolibre_form.save(commit=False)  # Guardar manualmente el objeto aseguramiento
            tiempolibre.idUser = user
            tiempolibre.save() 
             
            actividadessalud = actividadessalud_form.save(commit=False)  # Guardar manualmente el objeto aseguramiento
            actividadessalud.idUser = user
            actividadessalud.save() 
             
            actividadesculturales = actividadesculturales_form.save(commit=False)  # Guardar manualmente el objeto aseguramiento
            actividadesculturales.idUser = user
            actividadesculturales.save()  
            
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
            for Educacion_Form in Educacion_FormSet:
                for error in Educacion_Form.errors:
                    logger.error(f"Educacion_Form: {error}: {Educacion_Form.errors[error]}")          
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
            for error in actividadesculturales_form.errors:
                logger.error(f"actividadesculturalesForm: {error}: {actividadesculturales_form.errors[error]}")
            for error in actividadessalud_form.errors:
                logger.error(f"ActividadesSaludForm: {error}: {actividadessalud_form.errors[error]}")
            for error in tiempolibre_form.errors:
                logger.error(f"TiempoLibreForm: {error}: {tiempolibre_form.errors[error]}")
            for error in enfermedades_form.errors:
                logger.error(f"EnfermedadesForm: {error}: {enfermedades_form.errors[error]}")
            for error in deportes_form.errors:
                logger.error(f"DeportesForm: {error}: {deportes_form.errors[error]}")
            for error in molestiasseismeses_form.errors:
                logger.error(f"MolestiasSeisMesesForm: {error}: {molestiasseismeses_form.errors[error]}")    
            for error in molestiasvoz_form.errors:
                logger.error(f"MolestiasVozForm: {error}: {molestiasvoz_form.errors[error]}") 
            for error in sintomasaudicion_form.errors:
                logger.error(f"SintomasAudicionForm: {error}: {sintomasaudicion_form.errors[error]}") 
    else:
        form = FormularioForm()
        familiar_formset = FamiliarFormSet(prefix='familiar')
        mascota_formset = MascotasFormSet(prefix='mascota')
        Educacion_FormSet = EducacionFormSet( prefix='Educacion')
        aseguramiento_form = AseguramientoForm()
        familiarDiscapacidad_form = FamiliarDiscapacidadForm()
        situacionesafectable_form = SituacionesAfectableForm()
        transporte_form = TransportesForm()
        recursos_form = RecursosDigitalesForm()
        appaprendizaje_form = AppAprendizajeForm()
        ofrecimientos_form = OfrecimientosForm()
        desarrollopersonal_form = DesarrolloPersonalForm()
        reconocimientoempresarial_form = ReconocimientoEmpresarialForm()
        actividadesculturales_form = ActividadesCulturalesForm()
        actividadessalud_form = ActividadesSaludForm()
        tiempolibre_form = TiempoLibreForm()
        enfermedades_form = EnfermedadesForm()
        deportes_form = DeportesForm()
        molestiasseismeses_form = MolestiasSeisMesesForm()
        molestiasvoz_form = MolestiasVozForm()
        sintomasaudicion_form = SintomasAudicionForm()
        
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
         'reconocimientoempresarial_form': reconocimientoempresarial_form,
         'actividadesculturales_form': actividadesculturales_form,
         'actividadessalud_form': actividadessalud_form,
         'tiempolibre_form':tiempolibre_form,
         'enfermedades_form':enfermedades_form,
         'deportes_form':deportes_form,
         'molestiasseismeses_form': molestiasseismeses_form,
         'molestiasvoz_form':molestiasvoz_form,
         'sintomasaudicion_form': sintomasaudicion_form,
         'Educacion_FormSet':Educacion_FormSet    
         })
    
def Contratacion(request): 
    if request.method == 'POST':
        user = request.user
        form_data = request.POST.copy()
        form_data['idUser'] = user.id

        contratacion_form = ContratacionForm(form_data, request.FILES)
        
        if contratacion_form.is_valid(): 
            contratacion_form.instance.idUser = user
            contratacion_form.save()

            return HttpResponse("La información se ha enviado correctamente")
        else:
            logger = logging.getLogger('principal')
            logger.error("Error en el formulario.")
    else:
        contratacion_form = ContratacionForm
        
    return render(
        request,
        "prueba.html",
        {'contratacion_form': contratacion_form,      
         })

def Paginador(request):
    form = formularioForm.objects.all()
    
    context = {
        'form':form 
        }
    return render(request, 'prueba.html', context)













