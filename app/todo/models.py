from app import db


class Todo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer(), primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    is_complete = db.Column(db.Boolean(), default=False, nullable=True)

    def __init__(self, text):
        self.text = text