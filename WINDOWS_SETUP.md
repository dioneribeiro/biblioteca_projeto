# 🪟 Guia de Configuração para Windows

Este guia é específico para usuários Windows que querem configurar o projeto Sistema de Biblioteca.

## 📋 Pré-requisitos para Windows

### 1. Instalar Python

1. **Baixe o Python**:
   - Acesse: https://www.python.org/downloads/
   - Baixe a versão mais recente (3.8+)
   - **IMPORTANTE**: Marque a opção "Add Python to PATH" durante a instalação

2. **Verifique a instalação**:
   ```cmd
   python --version
   pip --version
   ```

### 2. Instalar PostgreSQL

1. **Baixe o PostgreSQL**:
   - Acesse: https://www.postgresql.org/download/windows/
   - Baixe a versão mais recente
   - Execute o instalador

2. **Durante a instalação**:
   - Anote a senha do usuário `postgres`
   - Mantenha a porta padrão (5432)
   - Instale o pgAdmin (interface gráfica)

3. **Verifique a instalação**:
   ```cmd
   psql --version
   ```

### 3. Instalar Git

1. **Baixe o Git**:
   - Acesse: https://git-scm.com/download/win
   - Baixe e instale

2. **Verifique a instalação**:
   ```cmd
   git --version
   ```

## 🚀 Configuração do Projeto no Windows

### 1. Abra o PowerShell ou CMD

```cmd
# Navegue para a pasta onde quer clonar o projeto
cd C:\Users\seu-usuario\Documents\projetos
```

### 2. Clone o Repositório

```cmd
git clone https://github.com/seu-usuario/biblioteca_projeto.git
cd biblioteca_projeto
```

### 3. Configure o Ambiente Virtual

```cmd
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
venv\Scripts\activate

# Você verá (venv) no início da linha
```

### 4. Instale as Dependências

```cmd
pip install -r requirements.txt
```

### 5. Configure o PostgreSQL

#### 5.1. Abra o pgAdmin

1. **Inicie o pgAdmin**:
   - Menu Iniciar > pgAdmin 4
   - Ou procure por "pgAdmin" no Windows

2. **Conecte ao servidor**:
   - Clique com botão direito em "Servers"
   - "Register" > "Server"
   - Nome: `localhost`
   - Host: `localhost`
   - Port: `5432`
   - Username: `postgres`
   - Password: (senha que você definiu na instalação)

#### 5.2. Crie o Banco de Dados

1. **No pgAdmin**:
   - Expanda "Servers" > "localhost" > "Databases"
   - Clique com botão direito em "Databases"
   - "Create" > "Database"
   - Nome: `biblioteca`
   - Clique em "Save"

2. **Ou via SQL**:
   - Clique com botão direito em "PostgreSQL 15" (ou sua versão)
   - "Query Tool"
   - Execute:
   ```sql
   CREATE DATABASE biblioteca;
   CREATE USER biblioteca WITH PASSWORD 'biblioteca';
   GRANT ALL PRIVILEGES ON DATABASE biblioteca TO biblioteca;
   ```

### 6. Configure as Variáveis de Ambiente

1. **Crie o arquivo `.env`**:
   - No VS Code ou editor de sua preferência
   - Crie um arquivo chamado `.env` na raiz do projeto
   - Adicione o conteúdo:

```env
ENVIRONMENT=development
DATABASE_URL=postgresql://biblioteca:biblioteca@127.0.0.1:5432/biblioteca
SECRET_KEY=django-insecure-e=%igdchzh@#iy81%t76m^pi**!xd9m@5!cpm0@nf&533m6^37
DEBUG=True
```

### 7. Execute as Migrações

```cmd
python manage.py migrate
```

### 8. Crie um Superusuário

```cmd
python manage.py createsuperuser
# Siga as instruções na tela
```

### 9. Execute o Servidor

```cmd
python manage.py runserver
```

### 10. Acesse o Sistema

Abra seu navegador e acesse:
- **Sistema**: http://127.0.0.1:8000/
- **Admin**: http://127.0.0.1:8000/admin/

## 🔧 Solução de Problemas Comuns no Windows

### Erro: "python não é reconhecido"

```cmd
# Verifique se Python está no PATH
echo %PATH%

# Se não estiver, adicione manualmente:
# C:\Users\seu-usuario\AppData\Local\Programs\Python\Python39\
# C:\Users\seu-usuario\AppData\Local\Programs\Python\Python39\Scripts\
```

### Erro: "psql não é reconhecido"

```cmd
# Adicione PostgreSQL ao PATH:
# C:\Program Files\PostgreSQL\15\bin
# (ajuste o número da versão conforme sua instalação)
```

### Erro de Conexão com PostgreSQL

1. **Verifique se o serviço está rodando**:
   - Pressione `Win + R`
   - Digite `services.msc`
   - Procure por "postgresql-x64-15" (ou sua versão)
   - Verifique se está "Running"

2. **Se não estiver rodando**:
   - Clique com botão direito no serviço
   - "Start"

### Erro: "pip não é reconhecido"

```cmd
# Reinstale o Python marcando "Add to PATH"
# Ou adicione manualmente ao PATH
```

### Erro de Permissão

```cmd
# Execute o PowerShell como Administrador
# Ou o CMD como Administrador
```

### Erro de Ambiente Virtual

```cmd
# Se o comando activate não funcionar:
venv\Scripts\activate.bat

# Ou use:
.\venv\Scripts\activate
```

## 📁 Estrutura de Pastas no Windows

```
C:\Users\seu-usuario\Documents\projetos\biblioteca_projeto\
├── biblioteca\
├── livro\
├── usuarios\
├── templates\
├── static\
├── venv\                    # Ambiente virtual
├── requirements.txt
├── manage.py
├── .env                     # Variáveis de ambiente
└── README.md
```

## 🎯 Comandos Úteis no Windows

```cmd
# Ativar ambiente virtual
venv\Scripts\activate

# Desativar ambiente virtual
deactivate

# Verificar versão do Python
python --version

# Verificar versão do pip
pip --version

# Listar pacotes instalados
pip list

# Atualizar pip
python -m pip install --upgrade pip

# Instalar dependências
pip install -r requirements.txt

# Executar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Executar servidor
python manage.py runserver

# Parar servidor
Ctrl + C
```

## 🔍 Verificações Importantes

### 1. Verificar Instalações

```cmd
python --version
pip --version
git --version
psql --version
```

### 2. Verificar Ambiente Virtual

```cmd
# Deve mostrar o caminho do venv
where python
```

### 3. Verificar Conexão com PostgreSQL

```cmd
psql -U postgres -h localhost
# Digite sua senha quando solicitado
# Digite \q para sair
```

### 4. Verificar Arquivo .env

```cmd
# Verifique se o arquivo existe
dir .env

# Verifique o conteúdo
type .env
```

## 🚀 Próximos Passos

Após configurar o projeto:

1. **Explore o Sistema**:
   - Acesse http://127.0.0.1:8000/
   - Crie uma conta ou faça login
   - Explore as funcionalidades

2. **Personalize**:
   - Edite os templates em `livro/templates/`
   - Modifique os estilos em `templates/base.html`
   - Adicione novas funcionalidades

3. **Deploy**:
   - Configure para Heroku ou outro serviço
   - Siga as instruções no README principal

## 📞 Suporte

Se encontrar problemas:

1. **Verifique os logs**:
   - Erros no terminal onde executou `runserver`
   - Logs do PostgreSQL no pgAdmin

2. **Recursos úteis**:
   - Documentação do Django: https://docs.djangoproject.com/
   - Stack Overflow: https://stackoverflow.com/
   - Comunidade Python: https://python.org.br/

---

🎉 **Parabéns!** Seu sistema de biblioteca está rodando no Windows! 