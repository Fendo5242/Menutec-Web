from django.urls import path
from .import views 

urlpatterns=[
    path('', views.login_view, name='login'),
    path('inicio',views.INICIO),

    path('pedidos',views.pedido, name='pedido'),
    path('buscarpedido/', views.buscar_pedido),
    path('eliminarpedido/<codigopedido>',views.eliminarpedido),
    path('marcarpedido/<codigopedido>',views.marcarpedido),

    path('platos',views.plato, name='plato'),
    path('buscarplato/', views.buscar_plato),
    path('eliminarplato/<codigoplato>',views.eliminarplato),
    path('registrarplato',views.registrarplato),
    path('editarplato/<codigoplato>',views.editarplato),

    path('categorias',views.categoria, name='categoria'),
    path('buscarcategoria/', views.buscar_categoria),
    path('eliminarcategoria/<codigocate>',views.eliminarcategoria),
    path('registrarcategoria',views.registrarcategoria),
    path('editarcategoria/<codigocate>',views.editarcategoria),


    path('menus',views.menu, name='menu'),
    path('buscarmenu/', views.buscar_menu),
    path('eliminarmenu/<codigomenu>',views.eliminarmenu),
    path('registrarmenu',views.registrarmenu),
    path('editarmenu/<codigomenu>',views.editarmenu),

]
