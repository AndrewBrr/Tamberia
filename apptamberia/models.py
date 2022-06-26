from django.db import models


class Productos(models.Model):
    
    nombre = models.CharField(max_length=20)
    calidad = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    precio = models.IntegerField()

    def __str__(self):
            return self.nombre+" "+str(self.calidad)+" "+str(self.tipo)+" "+str(self.precio)


class Clientes(models.Model):
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre+" "+str(self.apellido)+" "+str(self.email)+" "+str(self.telefono)    


class Pedidos(models.Model):
    
    cliente = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.IntegerField()
    pedido = models.CharField(max_length=100)
    

    def __str__(self):
        return self.cliente+" "+str(self.direccion)+"// "+str(self.email)+"// "+str(self.telefono)+"// "+str(self.pedido)