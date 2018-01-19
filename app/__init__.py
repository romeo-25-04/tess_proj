from flask import Flask

UPLOAD_FOLDER = '/static/img/process/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from app import views
