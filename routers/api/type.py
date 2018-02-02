# coding=utf-8

from flask import Blueprint, request, jsonify
import json
from ext import db
from models.types import Type


TYPE = Blueprint('type', __name__)


# 获取项目类别列表
@TYPE.route('/', methods=['GET'])
def type_list():
    types = [{
        'id': type.id,
        'name': type.name,
        'icon': type.icon,
        'path': type.path,
        'sort': type.sort,
        'create_time': type.create_time
    } for type in Type.query.order_by(Type.sort).all()]
    return jsonify({'code': 0, 'msg': '成功', 'data': types})


# 添加项目类别
@TYPE.route('/add', methods=['POST'])
def type_add():
    data = json.loads(request.data)
    if data.has_key('name'):
        name = data['name']
    else:
        return jsonify({'code': 1, 'msg': '缺少参数`name`'})
    if data.has_key('icon'):
        icon = data['icon']
    else:
        return jsonify({'code': 1, 'msg': '缺少参数`icon`'})
    if data.has_key('path'):
        path = data['path']
    else:
        return jsonify({'code': 1, 'msg': '缺少参数`path`'})
    if data.has_key('sort'):
        sort = data['sort']
    else:
        return jsonify({'code': 1, 'msg': '缺少参数`sort`'})
    type = Type(name, icon, path, sort)
    db.session.add(type)
    db.session.commit()
    return jsonify({'code': 0, 'msg': '成功'})


# 修改项目类别
@TYPE.route('/update', methods=['POST'])
def type_update():
    data = json.loads(request.data)
    if data.has_key('id'):
        id = data['id']
    else:
        return jsonify({'code': 1, 'msg': '缺少参数`id`'})
    type = Type.query.get(id)
    if data.has_key('name'):
        type.name = data['name']
    if data.has_key('icon'):
        type.icon = data['icon']
    if data.has_key('path'):
        type.path = data['path']
    if data.has_key('sort'):
        type.sort = data['sort']
    db.session.commit()
    return jsonify({'code': 0, 'msg': '成功'})
    

# 删除项目类别
@TYPE.route('/delete', methods=['POST'])
def type_delete():
    data = json.loads(request.data)
    if data.has_key('id'):
        id = data['id']
    else:
        return jsonify({'code': 1, 'msg': '缺少参数`id`'})
    type = Type.query.get(id)
    db.session.delete(type)
    db.session.commit()
    return jsonify({'code': 0, 'msg': '成功'})