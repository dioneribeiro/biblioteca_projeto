from django.shortcuts import redirect, render
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Livros, Categoria
from django.shortcuts import get_object_or_404


def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        livro = Livros.objects.filter(usuario = usuario)
        
        return render(request, 'home.html', {'livros': livro})
    else:
        return redirect('/auth/login/?status=2')
    
def ver_livro(request, id):
    if request.session.get('usuario'):
        livro = Livros.objects.get(id = id)
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
            categoria = request.POST.get('categoria')
            usuario = Usuario.objects.get(id=request.session['usuario'])
            livro = Livros(nome=nome, autor=autor, usuario=usuario, categoria_id=categoria)
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
            livro.categoria_id = request.POST.get('categoria')
            livro.save()
            return redirect('home')
        categorias = Categoria.objects.all()
        return render(request, 'editar_livro.html', {'livro': livro, 'categorias': categorias})
    else:
        return HttpResponse('Você não tem permissão para editar este livro')