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
from principal.views import inicio, usuarios, formularioII, datos, certificados, prueba,DataColaboradores, PowerBi,bd_colaboradores,Contratacion,ActualizacionDatosColaboradores
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
    path('ActualizacionDatosColaboradores/<int:idUser_id>/', ActualizacionDatosColaboradores, name='ActualizacionDatosColaboradores'),





   








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
