from django.db import models
from datetime import date
from usuarios.models import Usuario

class Leitor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.CharField(max_length=60, blank=True, null=True)
    rg = models.CharField(max_length=13, blank=True, null=True)
    cpf = models.CharField(max_length=13, blank=True, null=True)
    data_cadastro = models.DateField(default=date.today)
    livro = models.ManyToManyField('Livros', blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome
    

class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.nome
    

class Livros(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=30)
    co_autor = models.CharField(max_length=30, blank=True, null=True)
    sinopse = models.TextField(blank=True, null=True)
    data_cadastro = models.DateField(default=date.today)
    emprestado = models.BooleanField(default=False)
    leitor_emprestado = models.ForeignKey('Leitor', blank=True, null=True, on_delete=models.SET_NULL)
    data_emprestado = models.DateTimeField(blank=True, null=True)
    data_devolucao = models.DateTimeField(blank=True, null=True)
    tempo_duracao = models.DateField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    
    class Meta:
        verbose_name = 'Livro'

    def __str__(self):
        return self.nome
