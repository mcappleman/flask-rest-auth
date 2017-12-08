"""Imports"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import Result

app = Flask(__name__)
app.config.from_object(os.environ['app_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFCATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def hello():
    """Return Hello World"""
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    """Return Hello World"""
    return "Hello {}!".format(name)


if __name__ == '__main__':
    app.run()
