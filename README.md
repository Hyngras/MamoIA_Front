# MamoIA — Sistema Web para Classificação e Relatórios de Imagens Médicas

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)]()
[![Django](https://img.shields.io/badge/Django-5.x-green.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)]()

Aplicação web desenvolvida em **Django** para upload, visualização e análise de imagens médicas (ex.: mamografia).  

> **Documentação de requisitos e histórias de usuário:** [USER_STORIES.md](projeto_mamoia/docs/USER_STORIES.md)

---

## Screenshots

| Login | Upload | Relatório |
|-------|---------|-----------|
| ![](docs/screenshots/1.png) | ![](docs/screenshots/2.png) | ![](docs/screenshots/3.png) | ![](docs/screenshots/4.png) |


---

## Sumário
- [Arquitetura](#arquitetura)
- [Funcionalidades](#funcionalidades)
- [Stack & Dependências](#stack--dependências)
- [Configuração](#configuração)
- [Como Rodar](#como-rodar)
- [Estrutura de Pastas](#estrutura-de-pastas)
- [Histórias de Usuário](#histórias-de-usuário)
- [Roadmap](#roadmap)
- [Contribuição](#contribuição)
- [Licença](#licença)

---

## Arquitetura
- **Framework:** Django (MVT)
- **Autenticação:** Usuário customizado com login por e-mail (`AUTH_USER_MODEL = "api_rest.User"`)
- **Armazenamento:** Upload de arquivos via `MEDIA_ROOT`/`MEDIA_URL`
- **Configuração:** Variáveis de ambiente com `django-environ`
- **Renderização:** Templates HTML e geração de relatórios em PDF (WeasyPrint)

---

## Funcionalidades
- Autenticação de usuários via e-mail e senha  
- Upload de imagens médicas (mamografia, tomografia, etc.)  
- Visualização de histórico de uploads  
- Geração e download de relatórios em PDF  
- Painel administrativo via Django Admin  

> Em desenvolvimento:
> - Pipeline de inferência de IA
> - Integração com modelo de classificação

---

## Stack & Dependências
- **Linguagem:** Python 3.12+
- **Framework:** Django 5.x
- **Banco de Dados:** MySQL (ou SQLite em dev)
- **Bibliotecas principais:**
  - `django-environ`
  - `Pillow`
  - `weasyprint`
  - `mysqlclient` (ou `mysql-connector-python`)
  - `whitenoise` (produção)

Arquivo completo: [`requirements.txt`](./requirements.txt)

---

## Configuração do Ambiente

1. **Crie e ative o ambiente virtual:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate     # (Linux/Mac)
   .venv\Scripts\activate        # (Windows)
````

2. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Crie o arquivo `.env` a partir do `.env.example`:**

   ```dotenv
   DEBUG=True
   SECRET_KEY=sua-chave-secreta
   ALLOWED_HOSTS=localhost,127.0.0.1

   # Banco de dados
   DB_ENGINE=sqlite
   DB_NAME=mamoia
   DB_USER=user
   DB_PASSWORD=senha
   DB_HOST=127.0.0.1
   DB_PORT=3306

   # E-mail
   EMAIL_HOST=smtp.seudominio.com
   EMAIL_PORT=587
   EMAIL_HOST_USER=usuario@seudominio.com
   EMAIL_HOST_PASSWORD=senha
   EMAIL_USE_TLS=True
   ```

> Para produção, defina `DEBUG=False` e proteja suas credenciais no servidor.

---

## Como Rodar

```bash
python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

**Acesse:**

* Aplicação: [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Painel Admin: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

**Gerar arquivos estáticos para produção:**

```bash
python manage.py collectstatic --noinput
```

---

## Estrutura de Pastas

```
.
├── Projeto_MamoIA/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── api_rest/
│   ├── admin.py
│   ├── backends.py
│   ├── context_processors.py
│   ├── models.py
│   ├── views.py
│   └── ...
├── docs/
│   ├── USER_STORIES.md
│   └── screenshots/
│       ├── IMAGEM.png
│       ├── IMAGEM.png
│       └── IMAGEM.png
├── manage.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## Histórias de Usuário

As histórias completas estão documentadas em:
📄 [docs/USER_STORIES.md](docs/USER_STORIES.md)

---

## Contribuição

1. Crie uma branch:

   ```bash
   git checkout -b feat/nome-da-feature
   ```
2. Faça commits claros:

   ```bash
   git commit -m "feat: adiciona upload de imagem"
   ```
3. Envie para o repositório:

   ```bash
   git push -u origin feat/https://github.com/Hyngras/Projeto-MAMO-IA.git
   ```

Abra um **Pull Request** no GitHub descrevendo suas alterações.

---

## Licença

Distribuído sob a licença [MIT](LICENSE).

---

**Desenvolvido por:**
👩‍💻 Hyngrid Souza & colaboradores
📘 Projeto acadêmico — *Engenharia Biomédica + ADS*

```
