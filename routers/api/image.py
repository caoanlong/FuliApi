# coding=utf-8

from flask import Blueprint, request, jsonify
import json
from ext import db
# from models.images import Image

IMAGE = Blueprint('image', __name__)


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
