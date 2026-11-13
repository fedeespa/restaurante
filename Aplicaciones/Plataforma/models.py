from django.db import models

# Create your models here.
class Reservas(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=50)
    fecha=models.DateField()
    hora=models.IntegerField()
    personas=models.IntegerField()
    def __str__(self):
        return self.codigo+" "+self.nombre+" "+str(self.fecha)+" "+str(self.hora)+" "+str(self.personas)
