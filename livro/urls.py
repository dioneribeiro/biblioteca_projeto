from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('listar_categorias/', views.listar_categorias, name='listar_categorias'),
    path('ver_livro/<int:id>/', views.ver_livro, name='ver_livro'),
    path('listar_leitores/', views.listar_leitores, name='listar_leitores'),
    path('cadastrar_livro/', views.cadastrar_livro, name='cadastrar_livro'),
    path('editar_livro/<int:id>/', views.editar_livro, name='editar_livro'),
    path('cadastrar_categoria/', views.cadastrar_categoria, name='cadastrar_categoria'),
    path('editar_categoria/<int:id>/', views.editar_categoria, name='editar_categoria'),
    path('cadastrar_leitor/', views.cadastrar_leitor, name='cadastrar_leitor'),
    path('editar_leitor/<int:id>/', views.editar_leitor, name='editar_leitor'),
]