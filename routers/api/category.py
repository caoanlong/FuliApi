# coding=utf-8

from flask import Blueprint, request, jsonify
import json
from ext import db
from models.categorys import Category
from models.types import Type

CATEGORY = Blueprint('category', __name__)


# 获取分类列表
@CATEGORY.route('/', methods=['GET'])
def category_list():
    categorys = [{
        'id': category.id,
        'name': category.name,
        'sort': category.sort,
        'level': category.level,
        'type_id': category.type_id,
    } for category in Category.query.join(Type, Category.type_id == Type.id).all()]
    return jsonify({'code': 0, 'msg': '成功', 'data': categorys})


# 获取分类详情
@CATEGORY.route('/info', methods=['GET'])
def category_info():
    id = request.args.get('id')
    category = Category.query.get(id)
    return jsonify({
        'code': 0, 
        'msg': '成功', 
        'data': {
            'id': category.id,
            'name': category.name,
            'sort': category.sort,
            'level': category.level
        }
    })


# 添加分类
@CATEGORY.route('/add', methods=['POST'])
def category_add():
    data = json.loads(request.data)
    if data.has_key('name'):
        name = data['name']
    else:
        return jsonify({'code': 1, 'msg': '缺少参数`name`'})
    if data.has_key('level'):
        level = data['level']
    else:
        return jsonify({'code': 1, 'msg': '缺少参数`level`'})
    if data.has_key('sort'):
        sort = data['sort']
    else:
        return jsonify({'code': 1, 'msg': '缺少参数`sort`'})
    if data.has_key('type_id'):
        type_id = data['type_id']
    else:
        return jsonify({'code': 1, 'msg': '缺少参数`type_id`'})
    category = Category(name, level, sort, type_id)
    db.session.add(category)
    db.session.commit()
    return jsonify({'code': 0, 'msg': '成功'})


# 修改分类
@CATEGORY.route('/update', methods=['POST'])
def category_update():
    data = json.loads(request.data)
    print data
    id = data['id']
    category = Category.query.get(id)
    if data.has_key('name'):
        category.name = data['name']
    if data.has_key('level'):
        category.level = data['level']
    if data.has_key('sort'):
        category.sort = data['sort']
    if data.has_key('type_id'):
        category.type_id = data['type_id']
    db.session.commit()
    return jsonify({'code': 0, 'msg': '成功'})