# coding=utf-8

import json
from flask import Flask, request, jsonify
from flask.json import JSONEncoder
from ext import db
from models.member import Member
from routers.api.image import IMAGE

class MyJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, list):
            return super(MyJSONEncoder, self).default(obj)
        return obj.__dict__

APP = Flask(__name__)
APP.config.from_object('config')
APP.json_encoder = MyJSONEncoder

APP.register_blueprint(IMAGE, url_prefix='/api/image')
db.__init__(APP)

with APP.app_context():
    db.drop_all()
    db.create_all()

@APP.route('/member', methods=['GET'])
def member_get_list():
    memberlist = [{
        'id': member.id,
        'name': member.name
    } for member in Member.query.all()]
    return jsonify({
        'code': 0,
        'msg': '成功',
        'data': memberlist
    })

@APP.route('/member/add', methods=['POST'])
def member_add():
    if not request.data:
        return jsonify({
            'code': 1,
            'msg': '无参数'
        })
    else:
        data = json.loads(request.data)
        if data.has_key('name'):
            name = data['name']
            member = Member(name=name.encode('utf-8'))
            db.session.add(member)
            db.session.commit()
            return jsonify({
                'code': 0,
                'msg': '成功',
            })
        else:
            return jsonify({
                'code': 2,
                'msg': '缺少参数：name'
            })
