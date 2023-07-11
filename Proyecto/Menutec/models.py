from django.db import models
import datetime

class Cliente(models.Model):
    codigouser=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=80)
    email = models.EmailField(max_length=40)

    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):
    codigocate=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=60)
    descripcion=models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class EstadoMenu(models.Model):
    codigoestado=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=60)
    
    def __str__(self):
        return self.nombre
    
class EstadoPedido(models.Model):
    codigoestado=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=60)
    
    def __str__(self):
        return self.nombre

class Menu(models.Model):
    codigomenu=models.AutoField(primary_key=True)
    nombremenu=models.CharField(max_length=60)
    precio=models.DecimalField(max_digits = 5, decimal_places = 2)
    estado=models.ForeignKey(EstadoMenu, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombremenu
    
class Plato(models.Model):
    codigoplato=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=60)
    descripcion=models.CharField(max_length=200)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio=models.DecimalField(max_digits = 5, decimal_places = 2)
    menu=models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    codigopedido=models.AutoField(primary_key=True)
    codcliente =models.ForeignKey(Cliente, on_delete=models.CASCADE)
    codmenu =models.ForeignKey(Menu, on_delete=models.CASCADE)
    fecha=models.DateTimeField(default=datetime.datetime.now)
    estado=models.ForeignKey(EstadoPedido, on_delete=models.CASCADE)
