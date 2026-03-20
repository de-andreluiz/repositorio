import os
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', os.urandom(32))


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    debug = os.getenv('FLASK_ENV') == 'development'
    app.run(debug=debug, port=int(os.getenv('PORT', 5000)))
