from django.shortcuts import render, redirect, get_object_or_404
from .models import Idioma, Profesor, Clase # Importa todos los modelos

def inicio_centro_idiomas(request):
    return render(request, 'inicio.html')

def agregar_idioma(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        nivel = request.POST.get('nivel')
        region = request.POST.get('region')
        descripcion = request.POST.get('descripcion')
        codigo = request.POST.get('codigo')
        # bandera_img = request.FILES.get('bandera_img') # Para manejar imágenes, se necesita configurar MEDIA_ROOT y MEDIA_URL en settings.py

        idioma = Idioma(
            nombre=nombre,
            nivel=nivel,
            region=region,
            descripcion=descripcion,
            codigo=codigo,
            # bandera_img=bandera_img
        )
        idioma.save()
        return redirect('ver_idiomas')
    return render(request, 'idioma/agregar_idioma.html')

def ver_idiomas(request):
    idiomas = Idioma.objects.all()
    return render(request, 'idioma/ver_idiomas.html', {'idiomas': idiomas})

def actualizar_idioma(request, id_idioma):
    idioma = get_object_or_404(Idioma, pk=id_idioma)
    if request.method == 'POST':
        idioma.nombre = request.POST.get('nombre')
        idioma.nivel = request.POST.get('nivel')
        idioma.region = request.POST.get('region')
        idioma.descripcion = request.POST.get('descripcion')
        idioma.codigo = request.POST.get('codigo')
        # if 'bandera_img' in request.FILES:
        #    idioma.bandera_img = request.FILES['bandera_img']
        idioma.save()
        return redirect('ver_idiomas')
    return render(request, 'idioma/actualizar_idioma.html', {'idioma': idioma})

def borrar_idioma(request, id_idioma):
    idioma = get_object_or_404(Idioma, pk=id_idioma)
    if request.method == 'POST':
        idioma.delete()
        return redirect('ver_idiomas')
    return render(request, 'idioma/borrar_idioma.html', {'idioma': idioma})

# **IMPORTANTE**: Las funciones para Profesor y Clase se dejarán pendientes como se indicó.
# # Vistas para Profesor (PENDIENTE)
# def agregar_profesor(request):
#     pass
# def ver_profesores(request):
#     pass
# def actualizar_profesor(request, id_profesor):
#     pass
# def borrar_profesor(request, id_profesor):
#     pass

# # Vistas para Clase (PENDIENTE)
# def agregar_clase(request):
#     pass
# def ver_clases(request):
#     pass
# def actualizar_clase(request, id_clase):
#     pass
# def borrar_clase(request, id_clase):
#     pass