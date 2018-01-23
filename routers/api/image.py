from flask import Blueprint

image = Blueprint('image', __name__)

@image.route('/')
def imageList():
    return 'imgs list'
