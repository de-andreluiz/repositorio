# André Luiz - Portfólio Técnico

[![Python](https://img.shields.io/badge/Python-3.13+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.3-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-4.x-06B6D4?logo=tailwindcss&logoColor=white)](https://tailwindcss.com/)
[![Vercel](https://img.shields.io/badge/Deploy-Vercel-000000?logo=vercel&logoColor=white)](https://vercel.com/)

Portfólio profissional de Engenharia de Dados com backend em **Python/Flask** e frontend em **HTML5 + Tailwind CSS** (build estático via CLI).

---

## Stack Tecnológica

- **Backend:** Python, Flask
- **Frontend:** HTML5, Tailwind CSS (CLI)
- **Template Engine:** Jinja2
- **Servidor de Produção:** Gunicorn
- **Deploy:** Vercel (serverless Python)
- **Estáticos:** CSS e assets em `static/`

---

## Estrutura do Projeto

```bash
projetoPortfolio/
├── README.md
└── flask-version/
    ├── app.py
    ├── requirements.txt
    ├── package.json
    ├── vercel.json
    ├── templates/
    │   └── index.html
    └── static/
        ├── css/
        │   ├── input.css
        │   └── output.css
        └── img/
```

- `app.py`: inicialização do Flask, roteamento principal (`/`) e renderização do template.
- `templates/index.html`: estrutura principal da interface do portfólio.
- `static/css/input.css`: arquivo de entrada do Tailwind.
- `static/css/output.css`: CSS final compilado/minificado para produção.
- `vercel.json`: configuração de build e roteamento para deploy na Vercel.

---

## Rodando Localmente (Setup)

### 1) Entrar na pasta da aplicação

```bash
cd flask-version
```

### 2) Criar e ativar ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3) Instalar dependências Python

```bash
pip install -r requirements.txt
```

### 4) Instalar dependências de front-end

```bash
npm install
```

### 5) Gerar CSS estático do Tailwind

```bash
npm run build
```

### 6) Rodar o Flask

```bash
python app.py
```

Acesse em: `http://127.0.0.1:5000`

---

## Deploy

O projeto está preparado para deploy serverless na **Vercel**.

O `vercel.json` define:

- build Python com `@vercel/python` usando `app.py`
- rota catch-all (`/(.*)`) direcionada para `app.py`

Assim, toda a aplicação Flask é servida corretamente no ambiente de produção da Vercel.

---

## Segurança e Configuração

Na revisão do projeto, não foram encontrados tokens, senhas reais, chaves privadas ou credenciais sensíveis hardcoded.

Boas práticas já aplicadas:

- `SECRET_KEY` via variável de ambiente (`os.getenv`)
- `debug` controlado por ambiente (`FLASK_ENV`)
- porta configurável por variável (`PORT`)

Recomendado para execução:

- `SECRET_KEY`
- `FLASK_ENV`
- `PORT`

