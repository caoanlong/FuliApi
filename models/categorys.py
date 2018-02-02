from ext import db


class Category(db.Model):
    __tablename__ = 'categorys'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    sort = db.Column(db.Integer)
    level = db.Column(db.Integer)
    type_id = db.Column(db.Integer, db.ForeignKey('types.id'))
    create_time = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, name, sort=1, level=1):
        self.name = name
        self.sort = sort
        self.level = level
