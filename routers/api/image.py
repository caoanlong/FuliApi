# coding=utf-8

from flask import Blueprint, request, jsonify
import json
from main import db
# from models.images import Image
from models.categorys import Category

IMAGE = Blueprint('image', __name__)

def category2dict(category):
    return {
        'id': category.id,
        'name': category.name,
        'level': category.level
    }

# 获取图片列表
@IMAGE.route('/', methods=['GET'])
def image_list():
    images = Image.query.all()
    return jsonify(images)


# 添加图片
@IMAGE.route('/add', methods=['POST'])
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
@IMAGE.route('/category', methods=['GET'])
def category_list():
    categorys = [{
        'id': category.id,
        'name': category.name,
        'level': category.level
    } for category in Category.query.all()]
    return jsonify({'code': 0, 'msg': '成功', 'data': categorys})


# 获取图片分类详情
@IMAGE.route('/category/info', methods=['GET'])
def category_info():
    id = request.args.get('id')
    category = Category.query.get(id)
    print dir(category)
    return jsonify({'code': 0, 'msg': '成功', 'data': category})


# 添加图片分类
@IMAGE.route('/category/add', methods=['POST'])
def category_add():
    data = json.loads(request.data)
    name = data['name']
    category = Category(name=name)
    db.session.add(category)
    db.session.commit()
    return jsonify({'code': 0, 'msg': '成功'})


# 修改图片分类
@IMAGE.route('/category/update', methods=['POST'])
def category_update():
    data = json.loads(request.data)
    id = data['id']
    name = data['name']
    level = data['level']
    if not (id and name and level):
        return jsonify({'code': 1, 'msg': '缺少参数'})
    category = Category.query.filter_by(id=id).first()
    category.name = name
    category.level = level
    db.session.commit()
    return jsonify({'code': 0, 'msg': '成功'})
