# coding=utf-8

from flask import Blueprint, request, jsonify
import json
from ext import db
from models.images import Image
from models.categorys import Category

image = Blueprint('image', __name__)


# 获取图片列表
@image.route('/', methods=['GET'])
def image_list():
    print '-' * 20
    images = Image.query.all()
    return jsonify(images)


# 添加图片
@image.route('/add', methods=['POST'])
def image_add():
    data = json.loads(request.data)
    title = data.title
    url = data.url
    desc = data.desc
    category_id = data.category_id
    image_new = Image(title, url, desc, category_id)
    db.session.add(image_new)
    db.session.commit()
    return jsonify({'code': 0, 'msg': '成功'})


# 获取图片分类列表
@image.route('/category', methods=['GET'])
def category_list():
    category = Category.query.all()
    return jsonify(category)


# 添加图片分类
@image.route('/category/add', methods=['POST'])
def category_add():
    data = json.loads(request.data)
    name = data['name']
    category_new = Category(name)
    db.session.add(category_new)
    db.session.commit()
    return jsonify({'code': 0, 'msg': '成功'})
