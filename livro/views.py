from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Livros, Categoria
from django.db.models import Q


def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        livros = Livros.objects.filter(usuario=usuario)
        
        query = request.GET.get('query')
        if query:
            livros = livros.filter(
                Q(nome__icontains=query) |
                Q(autor__icontains=query) |
                Q(categoria__nome__icontains=query)
            )
            
        return render(request, 'home.html', {'livros': livros})
    else:
        return redirect('/auth/login/?status=2')
    

def ver_livro(request, id):
    if request.session.get('usuario'):
        livro = Livros.objects.get(id=id)
        if request.session.get('usuario') == livro.usuario.id:
            return render(request, 'ver_livro.html', {'livro': livro})
        else:
            return HttpResponse('Você não tem permissão para ver este livro')
    return redirect('/auth/login/?status=2')

def cadastrar_livro(request):
    if request.session.get('usuario'):
        if request.method == 'POST':
            nome = request.POST.get('nome')
            autor = request.POST.get('autor')
            co_autor = request.POST.get('co_autor', 'Nenhum')
            sinopse = request.POST.get('sinopse', 'Nenhum')
            categoria = request.POST.get('categoria')
            usuario = Usuario.objects.get(id=request.session['usuario'])
            livro = Livros(nome=nome, autor=autor, co_autor=co_autor, usuario=usuario, categoria_id=categoria, sinopse=sinopse)
            livro.save()
            return redirect('home')
        categorias = Categoria.objects.all()
        return render(request, 'cadastrar_livro.html', {'categorias': categorias})
    else:
        return redirect('/auth/login/?status=2')
    

def editar_livro(request, id):
    livro = get_object_or_404(Livros, id=id)
    if request.session.get('usuario') == livro.usuario.id:
        if request.method == 'POST':
            livro.nome = request.POST.get('nome')
            livro.autor = request.POST.get('autor')
            livro.sinopse = request.POST.get('sinopse', 'Sem informacao')
            livro.categoria = get_object_or_404(Categoria, id=request.POST.get('categoria'))
            

            livro.emprestado = 'emprestado' in request.POST
            
            livro.save()
            return redirect('home')
    
        categorias = Categoria.objects.all()
        return render(request, 'editar_livro.html', {'livro': livro, 'categorias': categorias})
    else:
        return HttpResponse('Você não tem permissão para editar este livro')


def forms(request):
    return render(request, 'form_template.html')


def listar_categorias(request):
    categorias = Categoria.objects.all()
    if not categorias:
        print("Nenhuma categoria encontrada")
    return render(request, 'listar_categorias.html', {'categorias': categorias})


def cadastrar_categoria(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')

        nova_categoria = Categoria(nome=nome, descricao=descricao)
        nova_categoria.save()
        return redirect('listar_categorias')

    return render(request, 'cadastrar_categoria.html')


def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    
    if request.method == 'POST':
        categoria.nome = request.POST.get('nome')
        categoria.descricao = request.POST.get('descricao')
        categoria.save()
        return redirect('listar_categorias')

    return render(request, 'cadastrar_categoria.html', {'categoria': categoria})