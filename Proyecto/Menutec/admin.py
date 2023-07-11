from django.contrib import admin
from .models import Cliente,Pedido,Plato,Menu,Categoria,EstadoMenu,EstadoPedido

class AdminCliente(admin.ModelAdmin):
    list_display=("codigouser","nombre","apellido","email")

class AdminCategoria(admin.ModelAdmin):
    list_display=("codigocate","nombre","descripcion")

class AdminEstadoMenu(admin.ModelAdmin):
    list_display=("codigoestado","nombre")

class AdminEstadoPedido(admin.ModelAdmin):
    list_display=("codigoestado","nombre")

class AdminMenu(admin.ModelAdmin):
    list_display=("codigomenu","nombremenu","precio","estado")

class AdminPlato(admin.ModelAdmin):
    list_display=("codigoplato","nombre","descripcion","categoria","precio","menu")

class AdminPedido(admin.ModelAdmin):
    list_display=("codigopedido","codcliente","codmenu","fecha","estado")

# Register your models here.
admin.site.register(Cliente,AdminCliente)
admin.site.register(Categoria,AdminCategoria)
admin.site.register(EstadoMenu, AdminEstadoMenu)
admin.site.register(EstadoPedido, AdminEstadoPedido)
admin.site.register(Menu,AdminMenu)
admin.site.register(Plato,AdminPlato)
admin.site.register(Pedido,AdminPedido)




