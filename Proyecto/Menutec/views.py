from django.http import HttpResponse
from django.shortcuts import render, redirect 
from .models import Pedido, Plato, Menu, Categoria, EstadoMenu, EstadoPedido
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'inicio.html')  # Reemplaza 'nombre_de_la_pagina' con el nombre de la página a la que deseas redirigir
        else:
            pass
    return render(request, 'login.html')

def INICIO(request):
    return render(request,'inicio.html')

#--------------------------Pedidos-------------------------------

def pedido(request):
    pedidos = Pedido.objects.all()
    estados = EstadoPedido.objects.all()
    context = {"pedidos":pedidos,"estados": estados}
    return render(request, 'pedidos.html', context)

def buscar_pedido(request):
    if request.method == 'GET':
        fecha = request.GET.get('txtfecha')        
        pedidos = Pedido.objects.filter(fecha__icontains=fecha)
        return render(request, 'pedidos.html', {'pedidos': pedidos})
    
def marcarpedido(request, codigopedido):
    pedido = get_object_or_404(Pedido, codigopedido=codigopedido)
    nuevo_estado = EstadoPedido.objects.get(nombre='Atendido')
    pedido.estado = nuevo_estado
    pedido.save()
    return redirect("/pedidos")

def eliminarpedido(request, codigopedido):
    pedido=Pedido.objects.get(codigopedido=codigopedido)
    pedido.delete()
    PedidosListado = Pedido.objects.order_by('codigopedido')
    return render(request, 'pedidos.html', {"pedidos":PedidosListado})

#--------------------------Platos-------------------------------
def plato(request):
    platos = Plato.objects.all()
    categorias = Categoria.objects.all()
    menus = Menu.objects.all()
    context = {"platos":platos,"categorias": categorias, "menus": menus}
    return render(request,'platos.html',context)

def buscar_plato(request):
    if request.method == 'GET':
        nombre = request.GET.get('txtnombre')
        platos = Plato.objects.filter(nombre__icontains=nombre)
        return render(request, 'platos.html', {'platos': platos})

def registrarplato(request):
    nombre = request.POST["txtnombreplato"]
    descripcion = request.POST["txtdescripcion"]
    categoria = request.POST["txtCategoria"]
    precio = request.POST["txtprecio"]
    menu = request.POST["txtMenu"]

    categoria_fk = Categoria.objects.get(codigocate = categoria)
    menu_fk = Menu.objects.get(codigomenu = menu)
    
    plato=Plato.objects.create(nombre=nombre,descripcion=descripcion,categoria=categoria_fk, precio=precio,menu=menu_fk)
    plato.save()
    PlatosListado = Plato.objects.order_by('codigoplato')
    return render(request, 'platos.html', {"platos":PlatosListado})

def eliminarplato(request, codigoplato):
    plato=Plato.objects.get(codigoplato=codigoplato)
    plato.delete()
    PlatosListado = Plato.objects.order_by('codigoplato')
    return render(request, 'platos.html', {"platos":PlatosListado})

def editarplato(request, codigoplato):
    nombre = request.POST["txtnombreplato"]
    descripcion = request.POST["txtdescripcion"]
    categoria = request.POST["txtCategoria"]
    precio = request.POST["txtprecio"]
    menu = request.POST["txtMenu"]

    plato = Plato.objects.get(codigoplato = codigoplato)
    plato.nombre = nombre
    plato.descripcion = descripcion
    plato.precio = precio
    categoria_fk = Categoria.objects.get(codigocate = categoria)
    plato.categoria = categoria_fk
    menu_fk = Menu.objects.get(codigomenu = menu)
    plato.menu = menu_fk
    plato.save()
    return redirect("/platos")

#--------------------------Categorias-------------------------------
def categoria(request):
    categorias = Categoria.objects.all()
    context = {"categorias": categorias}
    return render(request,'categorias.html',context)

def buscar_categoria(request):
    if request.method == 'GET':
        nombre = request.GET.get('txtnombre')
        categorias = Categoria.objects.filter(nombre__icontains=nombre)
        return render(request, 'categorias.html', {'categorias': categorias})

def registrarcategoria(request):
    nombre = request.POST["txtnombrecategoria"]
    descripcion = request.POST["txtdescripcion"]

    categoria=Categoria.objects.create(nombre=nombre,descripcion=descripcion)
    categoria.save()
    CategoriasListado = Categoria.objects.order_by('codigocate')
    return render(request, 'categorias.html', {"categorias":CategoriasListado})

def eliminarcategoria(request, codigocate):
    categoria=Categoria.objects.get(codigocate=codigocate)
    categoria.delete()
    CategoriasListado = Categoria.objects.order_by('codigocate')
    return render(request, 'categorias.html', {"categorias":CategoriasListado})

def editarcategoria(request, codigocate):
    nombre = request.POST["txtnombrecategoria"]
    descripcion = request.POST["txtdescripcion"]

    categoria = Categoria.objects.get(codigocate=codigocate)
    categoria.nombre = nombre
    categoria.descripcion = descripcion
    categoria.save()
    return redirect("/categorias")

#--------------------------Menus-------------------------------

def menu(request):
    menus = Menu.objects.all()
    estados = EstadoMenu.objects.all()
    context = {"menus": menus, "estados":estados}
    return render(request,'menus.html',context)

def buscar_menu(request):
    if request.method == 'GET':
        nombre = request.GET.get('txtnombre')
        menus = Menu.objects.filter(nombremenu__icontains=nombre)
        return render(request, 'menus.html', {'menus': menus})

def registrarmenu(request):
    nombremenu = request.POST["txtnombremenu"]
    precio = request.POST["txtprecio"]
    estado = request.POST["txtestado"]

    estado_fk = EstadoMenu.objects.get(codigoestado = estado)

    menu=Menu.objects.create(nombremenu=nombremenu,precio=precio, estado=estado_fk)
    menu.save()
    MenusListado = Menu.objects.order_by('codigomenu')
    return render(request, 'menus.html', {"menus":MenusListado})

def eliminarmenu(request, codigomenu):
    menu=Menu.objects.get(codigomenu=codigomenu)
    menu.delete()
    MenusListado = Menu.objects.order_by('codigomenu')
    return render(request, 'menus.html', {"menus":MenusListado})

def editarmenu(request, codigomenu):
    nombremenu = request.POST["txtnombremenu"]
    precio = request.POST["txtprecio"]
    estado = request.POST["txtestado"]

    menu = Menu.objects.get(codigomenu=codigomenu)
    menu.nombremenu = nombremenu
    menu.precio = precio
    estadomenu_fk = EstadoMenu.objects.get(codigoestado = estado)
    menu.estado = estadomenu_fk
    menu.save()
    return redirect("/menus")