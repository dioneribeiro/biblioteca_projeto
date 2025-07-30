# ⚡ Início Rápido - Sistema de Biblioteca

Este guia permite configurar o projeto em **5 minutos** para desenvolvedores experientes.

## 🚀 Setup Expresso

### 1. Clone e Configure
```bash
git clone https://github.com/seu-usuario/biblioteca_projeto.git
cd biblioteca_projeto
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

### 2. Banco de Dados
```sql
-- No pgAdmin ou psql
CREATE DATABASE biblioteca;
CREATE USER biblioteca WITH PASSWORD 'biblioteca';
GRANT ALL PRIVILEGES ON DATABASE biblioteca TO biblioteca;
```

### 3. Variáveis de Ambiente
Crie `.env` na raiz:
```env
ENVIRONMENT=development
DATABASE_URL=postgresql://biblioteca:biblioteca@127.0.0.1:5432/biblioteca
SECRET_KEY=django-insecure-e=%igdchzh@#iy81%t76m^pi**!xd9m@5!cpm0@nf&533m6^37
DEBUG=True
```

### 4. Execute
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### 5. Acesse
- **Sistema**: http://127.0.0.1:8000/
- **Admin**: http://127.0.0.1:8000/admin/

## 🎯 Comandos Essenciais

```bash
# Desenvolvimento
python manage.py runserver

# Migrações
python manage.py makemigrations
python manage.py migrate

# Superusuário
python manage.py createsuperuser

# Shell Django
python manage.py shell

# Testes
python manage.py test
```

## 📁 Estrutura Rápida

```
biblioteca_projeto/
├── biblioteca/     # Configurações Django
├── livro/          # App de livros
├── usuarios/       # App de autenticação
├── templates/      # Templates base
├── static/         # Arquivos estáticos
├── requirements.txt
├── manage.py
└── .env           # Variáveis de ambiente
```

## 🔧 Troubleshooting Rápido

### Erro de Conexão PostgreSQL
```bash
# Verifique se está rodando
services.msc  # Windows
# Procure por "postgresql" e inicie
```

### Erro de Dependências
```bash
pip install -r requirements.txt --force-reinstall
```

### Erro de Migrações
```bash
python manage.py migrate --fake-initial
```

## 🎨 Funcionalidades Principais

- ✅ **Gestão de Livros**: CRUD completo
- ✅ **Sistema de Leitores**: Cadastro e controle
- ✅ **Categorias**: Organização por categorias
- ✅ **Empréstimos**: Controle de livros emprestados
- ✅ **Busca**: Pesquisa avançada
- ✅ **Interface Moderna**: Bootstrap 5 + Glassmorphism
- ✅ **Autenticação**: Login e cadastro
- ✅ **Responsivo**: Desktop, tablet e mobile

## 📱 URLs Principais

- `/` - Página inicial (lista de livros)
- `/cadastrar_livro/` - Cadastrar novo livro
- `/listar_categorias/` - Gerenciar categorias
- `/listar_leitores/` - Gerenciar leitores
- `/login/` - Autenticação
- `/cadastro/` - Criar conta
- `/admin/` - Painel administrativo

## 🎯 Próximos Passos

1. **Explore o sistema** - Teste todas as funcionalidades
2. **Personalize** - Modifique templates e estilos
3. **Adicione features** - Implemente novas funcionalidades
4. **Deploy** - Configure para produção

---

⚡ **Pronto!** Seu sistema está rodando em menos de 5 minutos! 