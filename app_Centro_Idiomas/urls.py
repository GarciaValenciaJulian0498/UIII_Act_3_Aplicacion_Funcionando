from django.urls import path
from . import views

urlpatterns = [
path('', views.inicio_centro_idiomas, name='inicio_centro_idiomas'),
path('idiomas/agregar/', views.agregar_idioma, name='agregar_idioma'),
path('idiomas/', views.ver_idiomas, name='ver_idiomas'),
path('idiomas/actualizar/<int:id_idioma>/', views.actualizar_idioma, name='actualizar_idioma'),
path('idiomas/borrar/<int:id_idioma>/', views.borrar_idioma, name='borrar_idioma'),
]