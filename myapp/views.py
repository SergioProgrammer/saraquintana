from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def mi_vista(request):
    proyectos = [
        {"nombre": "Proyecto 1", "descripcion": "Descripción del Proyecto 1", "imagen": "images/imagen1.jpg"},
        {"nombre": "Proyecto 2", "descripcion": "Descripción del Proyecto 2", "imagen": "images/imagen2.jpg"},
        {"nombre": "Proyecto 3", "descripcion": "Descripción del Proyecto 3", "imagen": "images/imagen3.jpg"},
    ]
    return render(request, 'index.html', {"proyectos": proyectos})
