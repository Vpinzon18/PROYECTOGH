from django.shortcuts import render

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