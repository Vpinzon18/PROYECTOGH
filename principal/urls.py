"""
URL configuration for principal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from principal import views
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', login, name="login"),
    path('inicio/', views.inicio, name="inicio"),
    path('usuarios/', views.usuarios, name="usuarios"),
    path('prueba/', views.prueba, name="prueba"),
    path('PowerBi/', views.PowerBi, name="PowerBi"),
    path('bd_colaboradores/<int:idUser_id>/', views.bd_colaboradores, name='bd_colaboradores'),
    path('bd_claboradores_hijos/<int:idUser_id>/', views.editar_familiar, name='editar_familiar'),
    path('ActualizacionDatosColaboradores/<int:idUser_id>/', views.ActualizacionDatosColaboradores, name='ActualizacionDatosColaboradores'),
    
   
# region  #! URL'S PARA EL MODULO DE DATOS DE EMPEADOS


    #  ?  urls para la vista con una tabla de todos los colaboradores¡
    path('datos/', views.datos, name="datos"),


    #  ?  urls para la vista de edicion de datos de familiares 
    path("Info_Familiar_DB/<int:idUser_id>/", views.Info_Familiar_DB, name="Info_Familiar_DB"),
    path('editar_familiar/<int:familiar_id>/', views.editar_familiar, name='editar_familiar'),
    path('eliminar_familiar/<int:familiar_id>/', views.eliminar_familiar, name='eliminar_familiar'),
    path('agregar_familiar/<int:idUser_id>/', views.agregar_familiar, name='agregar_familiar'),

    #  ? Urls para las vistas de edicion de datos de mascotas 
    path("Info_Mascotas_DB/<int:idUser_id>/", views.Info_Mascotas_DB, name="Info_Mascotas_DB"),
    path('Vista_Edicion_Mascotas/<int:id_mascota>/', views.Vista_Edicion_Mascotas, name='Vista_Edicion_Mascotas'),
    path('agregar_mascota/<int:idUser_id>/', views.agregar_mascota, name='agregar_mascota'),
    path('eliminar_mascota/<int:id_mascota>/', views.eliminar_mascota, name='eliminar_mascota'),
    
    
    # ? Urls para las vistas de la edicion de los datos de educacion 
    path("Info_Educacion_DB/<int:idUser_id>/", views.Info_Educacion_DB, name="Info_Educacion_DB"),
    path('agregar_educacion/<int:idUser_id>/', views.agregar_educacion, name='agregar_educacion'),
    path('editar_educacion/<int:id_estudio>/', views.editar_educacion, name='editar_educacion'),
    path('eliminar_educacion/<int:id_estudio>/', views.eliminar_educacion, name='eliminar_educacion'),
    
    
    # ? Urls para las vistas de la edicion de los datos de CONTRATACION
    path("Info_Contratos_DB/<int:idUser_id>/", views.Info_Contratos_DB, name="Info_Contratos_DB"),
    path('agregar_contrato/<int:idUser_id>/', views.agregar_contrato, name='agregar_contrato'),
    path('editar_contrato/<int:id_Contrato>/', views.editar_contrato, name='editar_contrato'),
    path('eliminar_contrato/<int:id_Contrato>/', views.eliminar_contrato, name='eliminar_contrato'),

    # ? Urls para las vistas de la edicion de los datos de OOPT
    path("Info_OOPT_DB/<int:idUser_id>/", views.Info_OOPT_DB, name="Info_OOPT_DB"),
    path('agregar_oopt/<int:idUser_id>/', views.agregar_oopt, name='agregar_oopt'),
    path('editar_oopt/<int:id_oopt>/', views.editar_oopt, name='editar_oopt'),
    path('eliminar_oopt/<int:id_oopt>/', views.eliminar_oopt, name='eliminar_oopt'),

    # ? Urls para las vistas de la edicion de los datos de la EXPERIENCIA LABORAL 
    path("Info_experiencias_laborales_DB/<int:idUser_id>/", views.Info_experiencias_laborales_DB, name="Info_experiencias_laborales_DB"),
    path('agregar_experiencia/<int:idUser_id>/', views.agregar_experiencia, name='agregar_experiencia'),
    path('editar_experiecncia/<int:id_experiencia>/', views.editar_experiecncia, name='editar_experiecncia'),
    path('eliminar_experiencia/<int:id_experiencia>/', views.eliminar_experiencia, name='eliminar_experiencia'),

    # ? Urls para las vistas de la edicion de los datos de la EXPERIENCIA LABORAL 
    path("Info_Desempeno_DB/<int:idUser_id>/", views.Info_Desempeno_DB, name="Info_Desempeno_DB"),
    path('agregar_desempeno/<int:idUser_id>/', views.agregar_desempeno, name='agregar_desempeno'),
    path('editar_desempeno/<int:id_evaluacion>/', views.editar_desempeno, name='editar_desempeno'),
    path('eliminar_desempeno/<int:id_evaluacion>/', views.eliminar_desempeno, name='eliminar_desempeno'),

#    endregion   

# region #! URL'S PARA EL MODULO DE CERTIFICADOS LABORALES 

    #  ?  urls para la presentacion de la vista de certificados
    path("Info_Certificados_DB/<int:idUser_id>/", views.Info_Certificados_DB, name="Info_Certificados_DB"),
    path("GeneracionCertificadoLaboral/<int:id_Contrato>/", views.GeneracionCertificadoLaboral.as_view(), name="GeneracionCertificadoLaboral"),

# endregion

    path('', views.signin, name='signin'),
    path('signin/',views.signin, name='signin'),
    path('signout/',views.signout, name='signout'),
    path('signup/',views.signup, name='signup'),
    path('profile/',views.profile, name='profile'),
    path('registrarUsuario/', views.registrarUsuario),
    path('edicionUsuario/<id>', views.edicionUsuario),
    path('eliminarUsuario/<id>', views.eliminarUsuario),
    path('editarUsuario/', views.editarUsuario)
    
    
    
    #path('', views.home)
]
