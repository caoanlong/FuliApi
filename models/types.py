from ext import db

class Type(db.Model):
    __tablename__ = 'types'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    icon = db.Column(db.String(50))
    path = db.Column(db.String(50))
    sort = db.Column(db.Integer)
    create_time = db.Column(db.TIMESTAMP, default=db.func.current_timestamp(), nullable=False)

    def __init__(self, name, icon, path, sort=1):
        self.name = name
        self.icon = icon
        self.path = path
        self.sort = sort
