"""Imports"""
import os
from flask import Flask

APP = Flask(__name__)
APP.config.from_object(os.environ['APP_SETTINGS'])

@APP.route('/')
def hello():
    """Return Hello World"""
    return "Hello World!"

@APP.route('/<name>')
def hello_name(name):
    """Return Hello World"""
    return "Hello {}!".format(name)

if __name__ == '__main__':
    APP.run()
