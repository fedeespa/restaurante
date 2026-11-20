from django.urls import path
from . import views
urlpatterns=[
    path('',views.login),
    path('registrarReserva/',views.registrarReserva),
    path('edicionReserva/<codigo>',views.edicionReserva),
    path('borrarReserva/<codigo>',views.borrarReserva),
    path('editarReserva/',views.editarReserva),
    path('loguearse/',views.chequearUsuarios),
    path('inicio/',views.home),
    path('registrarse/',views.registrarse),
    path('registro/',views.registro)
]
