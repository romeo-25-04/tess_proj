from flask import render_template, request
from app import app
import os


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Photo-Reader', acHome='active')


@app.route('/process', methods=['GET', 'POST'])

def process():
    foto_dir_path = "/static/img/"
    fotoname = "upload_icon.png"
    if request.method == "POST":
        fotoname = request.form.get('foto', foto_dir_path)
        file = request.files['foto']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], fotoname))
    foto_path = foto_dir_path + fotoname
    return render_template('process.html',
                           title='Process-Photo',
                           foto_path=foto_path,
                           acProcess='active')
