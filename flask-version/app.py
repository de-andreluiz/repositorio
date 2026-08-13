import os
from datetime import datetime, timezone

from flask import Flask, render_template
from flask_compress import Compress

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', os.urandom(32))
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 60 * 60 * 24 * 30  # 30 dias de cache para /static
Compress(app)


@app.route('/')
def index():
    return render_template('index.html', current_year=datetime.now(timezone.utc).year)


@app.route('/robots.txt')
def robots():
    return app.send_static_file('robots.txt')


@app.route('/sitemap.xml')
def sitemap():
    return app.send_static_file('sitemap.xml')


if __name__ == '__main__':
    debug = os.getenv('FLASK_ENV') == 'development'
    app.run(debug=debug, port=int(os.getenv('PORT', 5000)))
