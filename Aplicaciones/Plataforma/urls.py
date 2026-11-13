from django.urls import path
from . import views
urlpatterns=[
    path('',views.home),
    path('registrarReserva/',views.registrarReserva),
    path('edicionReserva/<codigo>',views.edicionReserva),
    path('borrarReserva/<codigo>',views.borrarReserva),
    path('editarReserva/',views.editarReserva),
]
