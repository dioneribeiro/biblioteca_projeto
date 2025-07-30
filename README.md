# 📚 Sistema de Biblioteca - Django

Um sistema completo de gerenciamento de biblioteca desenvolvido em Django, com interface moderna e funcionalidades avançadas para controle de livros, leitores e categorias.

## 🚀 Funcionalidades

- **Gestão de Livros**: Cadastro, edição, visualização e busca de livros
- **Controle de Leitores**: Cadastro e gerenciamento de leitores
- **Categorização**: Sistema de categorias para organização
- **Sistema de Empréstimos**: Controle de livros emprestados
- **Interface Moderna**: Design responsivo com Bootstrap 5 e glassmorphism
- **Autenticação**: Sistema de login e cadastro de usuários
- **Busca Avançada**: Pesquisa por nome, autor ou categoria

## 🛠️ Tecnologias Utilizadas

- **Backend**: Django 5.1.1
- **Database**: PostgreSQL
- **Frontend**: Bootstrap 5, Bootstrap Icons
- **Estilização**: CSS3 com glassmorphism
- **Deploy**: Heroku (configurado)

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- **Python 3.8+**
- **PostgreSQL**
- **Git**

### Instalando Python (Windows)

```bash
# Baixe e instale Python do site oficial
# https://www.python.org/downloads/
```

### Instalando PostgreSQL (Windows)

```bash
# Baixe e instale PostgreSQL do site oficial
# https://www.postgresql.org/download/windows/
```

## 🚀 Como Executar o Projeto

### 1. Clone o Repositório

```bash
git clone https://github.com/seu-usuario/biblioteca_projeto.git
cd biblioteca_projeto
```

### 2. Configure o Ambiente Virtual

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual (Windows)
venv\Scripts\activate

# Ativar ambiente virtual (Linux/Mac)
source venv/bin/activate
```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o Banco de Dados PostgreSQL

#### 4.1. Acesse o PostgreSQL

```bash
# Abra o pgAdmin ou use o terminal
psql -U postgres
```

#### 4.2. Crie o Banco de Dados

```sql
-- Conecte como superusuário
CREATE DATABASE biblioteca;
CREATE USER biblioteca WITH PASSWORD 'biblioteca';
GRANT ALL PRIVILEGES ON DATABASE biblioteca TO biblioteca;
\q
```

### 5. Configure as Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
ENVIRONMENT=development
DATABASE_URL=postgresql://biblioteca:biblioteca@127.0.0.1:5432/biblioteca
SECRET_KEY=django-insecure-e=%igdchzh@#iy81%t76m^pi**!xd9m@5!cpm0@nf&533m6^37
DEBUG=True
```

### 6. Execute as Migrações

```bash
python manage.py migrate
```

### 7. Crie um Superusuário

```bash
python manage.py createsuperuser
```

### 8. Execute o Servidor

```bash
python manage.py runserver
```

### 9. Acesse o Sistema

Abra seu navegador e acesse:
- **Sistema**: http://127.0.0.1:8000/
- **Admin**: http://127.0.0.1:8000/admin/

## 📁 Estrutura do Projeto

```
biblioteca_projeto/
├── biblioteca/              # Configurações principais do Django
│   ├── settings.py         # Configurações do projeto
│   ├── urls.py            # URLs principais
│   └── wsgi.py            # Configuração WSGI
├── livro/                  # App de gerenciamento de livros
│   ├── models.py          # Modelos de dados
│   ├── views.py           # Views e lógica de negócio
│   ├── urls.py            # URLs do app livro
│   └── templates/         # Templates HTML
├── usuarios/              # App de autenticação
│   ├── models.py          # Modelos de usuários
│   ├── views.py           # Views de autenticação
│   ├── urls.py            # URLs do app usuarios
│   └── templates/         # Templates de login/cadastro
├── templates/             # Templates base
├── static/               # Arquivos estáticos
├── requirements.txt      # Dependências Python
├── manage.py            # Script de gerenciamento Django
└── README.md           # Este arquivo
```

## 🎨 Interface Moderna

O sistema possui uma interface moderna com:

- **Design Glassmorphism**: Efeitos de vidro e transparência
- **Bootstrap 5**: Framework CSS moderno
- **Bootstrap Icons**: Ícones consistentes
- **Responsividade**: Funciona em desktop, tablet e mobile
- **Gradientes**: Backgrounds com gradientes modernos
- **Animações**: Transições suaves e hover effects

## 🔧 Configurações Importantes

### Settings.py

O arquivo `biblioteca/settings.py` está configurado para:

- **Desenvolvimento**: Usa PostgreSQL local
- **Produção**: Configurado para Heroku
- **Apps Instalados**: `livro` e `usuarios`
- **Templates**: Configurados com context processors
- **Static Files**: Configurados para produção

### Banco de Dados

- **Desenvolvimento**: PostgreSQL local
- **Produção**: PostgreSQL no Heroku
- **Migrações**: 31 migrações já aplicadas

## 🚀 Deploy no Heroku

O projeto está configurado para deploy no Heroku:

```bash
# Instale o Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

# Login no Heroku
heroku login

# Crie um app no Heroku
heroku create seu-app-name

# Configure as variáveis de ambiente
heroku config:set ENVIRONMENT=production
heroku config:set SECRET_KEY=sua-chave-secreta
heroku config:set DATABASE_URL=sua-url-do-banco

# Deploy
git push heroku main

# Execute as migrações
heroku run python manage.py migrate

# Crie um superusuário
heroku run python manage.py createsuperuser
```

## 🐛 Solução de Problemas

### Erro de Conexão com PostgreSQL

```bash
# Verifique se o PostgreSQL está rodando
# Windows: Serviços > PostgreSQL
# Linux: sudo systemctl status postgresql
```

### Erro de Migrações

```bash
# Resete as migrações se necessário
python manage.py migrate --fake-initial
```

### Erro de Dependências

```bash
# Atualize o pip
pip install --upgrade pip

# Reinstale as dependências
pip install -r requirements.txt --force-reinstall
```

### Erro de Variáveis de Ambiente

```bash
# Verifique se o arquivo .env existe
# Certifique-se de que as variáveis estão corretas
```

## 📝 Comandos Úteis

```bash
# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Coletar arquivos estáticos
python manage.py collectstatic

# Shell do Django
python manage.py shell

# Testes
python manage.py test
```

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

**Seu Nome**
- GitHub: [@dioneribeiro](https://github.com/dioneribeiro)
- LinkedIn: [Dione Ribeiro](https://linkedin.com/in/dione-ribeiro-niza-0b0814113)

## 🙏 Agradecimentos

- Django Documentation
- Bootstrap Team
- PostgreSQL Community
- Heroku Platform

---

⭐ Se este projeto te ajudou, considere dar uma estrela no repositório!
