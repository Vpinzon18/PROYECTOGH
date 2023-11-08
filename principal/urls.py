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
from principal.views import inicio, usuarios, Info_Mascotas_DB,formularioII,bd_colaboradores_Contratacion , editar_familiar,datos,bd_colaboradores_Educacion, certificados, prueba,DataColaboradores, PowerBi,bd_colaboradores,Contratacion,ActualizacionDatosColaboradores, Info_Familiar_DB
from principal import views
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', login, name="login"),
    path('inicio/', inicio, name="inicio"),
    path('usuarios/', usuarios, name="usuarios"),
    path('formularioII/', formularioII, name="formularioII"),
    path('datos/', datos, name="datos"),
    path('certificados/', certificados, name="certificados"),
    path('prueba/', prueba, name="prueba"),
    path('datos/DataColaboradores/', DataColaboradores, name="DataColaboradores"),
    path('PowerBi/', PowerBi, name="PowerBi"),
    path('bd_colaboradores/<int:idUser_id>/', bd_colaboradores, name='bd_colaboradores'),
    path('bd_claboradores_hijos/<int:idUser_id>/', editar_familiar, name='editar_familiar'),
    path('ActualizacionDatosColaboradores/<int:idUser_id>/', ActualizacionDatosColaboradores, name='ActualizacionDatosColaboradores'),
    path("bd_colaboradores_Educacion/<int:idUser_id>/", bd_colaboradores_Educacion, name="bd_colaboradores_Educacion"),
    path("bd_colaboradores_Contratacion/<int:idUser_id>/", bd_colaboradores_Contratacion, name="bd_colaboradores_Contratacion"),
   
   
#    urls para la vista de edicion de datos de familiares 
    path("Info_Familiar_DB/<int:idUser_id>/", Info_Familiar_DB, name="Info_Familiar_DB"),
    path('editar_familiar/<int:familiar_id>/', views.editar_familiar, name='editar_familiar'),
    path('eliminar_familiar/<int:familiar_id>/', views.eliminar_familiar, name='eliminar_familiar'),
    path('agregar_familiar/<int:idUser_id>/', views.agregar_familiar, name='agregar_familiar'),

    # Urls para las vistas de edicion de datos de mascotas 
    path("Info_Mascotas_DB/<int:idUser_id>/", Info_Mascotas_DB, name="Info_Mascotas_DB"),
    
    # Urls para las vistas de la edicion de los datos de educacion 
    




   








    path('Contratacion/<idUser_id>', Contratacion),
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
