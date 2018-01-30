# coding=utf-8

from ext import db
from datetime import datetime


class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50))
    url = db.Column(db.String(100))
    desc = db.Column(db.String(100))
    read = db.Column(db.Integer)
    like = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    # category字段关联到Categorys表
    # category = db.relationship('Category', backref=db.backref('images', lazy='dynamic'))

    def __init__(self, title, url, desc, read=0, like=0, category_id, create_time=None):
        self.title = title
        self.url = url
        self.desc = desc
        self.read = read
        self.like = like
        self.category_id = category_id
        if create_time is None:
            create_time = datetime.utcnow()
        self.create_time = create_time

