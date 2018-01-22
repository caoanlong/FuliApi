# coding=utf-8

from flask import Flask, request, jsonify

app = Flask(__name__)
app.config.from_object('config')


@app.route('/user/<name>/')
def user(name):
    return 'you name is: {}'.format(name)
