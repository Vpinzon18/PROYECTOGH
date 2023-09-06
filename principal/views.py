from django.shortcuts import render

def holamundo(request):
    context={}
    return render(request, 'index.html', context)


def holamundo1(request):
    context={}
    return render(request, 'login.html', context)