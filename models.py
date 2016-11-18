from app import db
from sqlalchemy.dialects.postgresql import JSON

class Books(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    name = db.Column(db.String())
    author = db.Column(db.String())
    description = db.Column(db.String())
    book = db.Column(JSON)

    def __init__(self, user_id, name, author, description, book):
        self.user_id = user_id
        self.name = name
        self.author = author
        self.description = description
        self.book

        def __repre__(self):
            return '<id {}>'.format(self.id)
