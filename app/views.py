from flask import render_template, request
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Photo-Reader', acHome='active')


@app.route('/process')
def process():
    return render_template('process.html', title='Process-Photo', acProcess='active')
