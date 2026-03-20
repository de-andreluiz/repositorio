EDEAS CLONE - VERSAO FLASK
==========================

ESTRUTURA DE PASTAS:
flask-version/
├── app.py              # Aplicação Flask principal
├── requirements.txt    # Dependências Python
├── templates/
│   └── index.html     # Template HTML completo
└── README.txt         # Este arquivo


COMO RODAR:
-----------

1. Instalar dependências:
   pip install -r requirements.txt

2. Rodar o servidor:
   python app.py

3. Acessar no navegador:
   http://localhost:5000


PERSONALIZAÇÕES:
----------------

1. CORES: Edite as cores no bloco <script> do Tailwind config no index.html
   - primary: cor principal (verde por padrão)
   - background: cor de fundo
   - card: cor dos cards

2. TEXTOS: Edite diretamente no index.html
   - Titulos, descrições, serviços, etc.

3. CONTATO: 
   - Altere o número de WhatsApp nas URLs (wa.me/5585999999999)
   - Altere email e endereço

4. FORMULÁRIO:
   - Configure o envio de email no app.py
   - Integre com banco de dados se necessário


PARA ADICIONAR BANCO DE DADOS:
------------------------------

pip install flask-sqlalchemy

Exemplo no app.py:
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    subject = db.Column(db.String(50))
    message = db.Column(db.Text)


PARA ENVIAR EMAIL:
------------------

pip install flask-mail

Exemplo no app.py:
from flask_mail import Mail, Message

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'seu@email.com'
app.config['MAIL_PASSWORD'] = 'sua-senha'

mail = Mail(app)
