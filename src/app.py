from flask import Flask, request, Response, render_template, redirect, send_from_directory
from flask_cors import CORS
import os
import time
import random

UPLOAD_FOLDER = './uploads/'
TEMPLATE_FOLDER = './templates/'

app = Flask(__name__, template_folder=TEMPLATE_FOLDER)
app.debug = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = os.urandom(24)  # Set to a fixed value when putting into production environment
app.config['SESSION_COOKIE_NAME'] = 'session_warp'


@app.route('/', methods=["GET"])
def root():
    return render_template('index.html')


if __name__ == "__main__":
    CORS(app)
