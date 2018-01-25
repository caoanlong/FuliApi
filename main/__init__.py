# coding=utf-8

from flask import Flask, request, jsonify
from routers.api.image import image
from ext import db

app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(image, url_prefix='/api/image')
db.__init__(app)

with app.app_context():
    db.drop_all()
    db.create_all()


@app.route('/')
def user():
    return 'you name is: index'
