from django.shortcuts import redirect, render
from .models import Reservas
# Create your views here.
def home(request):
    reservaslistadas=Reservas.objects.all()
    return render(request,"gestionReservas.html",{"reservas":reservaslistadas})
def registrarReserva(request):
    codigo=request.POST['txtcodigo']
    nombre=request.POST['txtnombre']
    fecha=request.POST['txtfecha']
    hora=request.POST['txthora']
    personas=request.POST['txtpersonas']
    reserva=Reservas.objects.create(codigo=codigo,nombre=nombre,fecha=fecha,hora=hora,personas=personas)
    return redirect('/')
def borrarReserva(request,codigo):
    reserva=Reservas.objects.get(codigo=codigo)
    reserva.delete()
    return redirect('/')
def edicionReserva(request,codigo):
    reserva=Reservas.objects.get(codigo=codigo)
    return render(request,"edicionReserva.html",{'reserva':reserva})
def editarReserva(request):
    codigo=request.POST['txtcodigo']
    nombre=request.POST['txtnombre']
    fecha=request.POST['txtfecha']
    hora=request.POST['txthora']
    personas=request.POST['txtpersonas']
    reserva=Reservas.objects.get(codigo=codigo)
    reserva.nombre=nombre
    reserva.fecha=fecha
    reserva.hora=hora
    reserva.personas=personas
    reserva.save()
    return redirect('/')      
  
