from ext import db


class Category(db.Model):
    __tablename__ = 'categorys'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    level = db.Column(db.Integer)
    create_time = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, name, level=1):
        self.name = name
        self.level = level
