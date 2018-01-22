# coding=utf-8

from flask import Flask, request, jsonify
from routers.api.image import image
from routers.admin import admin

app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(image)
app.register_blueprint(admin)

@app.route('/<name>/')
def user(name):
    return 'you name is: {}'.format(name)
