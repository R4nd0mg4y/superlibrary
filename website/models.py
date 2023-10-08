from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime
import pytz
from collections import Counter
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    author = db.Column(db.String(128))
    publication_date = db.Column(db.Date)
    cover = db.Column(db.String(256))  # Trường cover để lưu tên file hình ảnh
    content = db.Column(db.String(256))  # Trường content để lưu tên file PDF
    notes = db.relationship('Note') # Quan hệ một-nhiều với Ghi chú

    def rating_percentages(self):
        ratings = [note.rating for note in self.notes]
        total_ratings = len(ratings)
        rating_counts = Counter(ratings)
        if total_ratings == 0:
            total_ratings = 1
        rating_percentages = [rating_counts[i] / total_ratings * 100 for i in range(1, 6)]
        return rating_percentages



class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date_created = db.Column(db.DateTime, default=datetime.now(pytz.timezone('Asia/Bangkok')).replace(microsecond=0))
    rating = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))  # Khóa ngoại đến sách
    users = db.relationship('User')


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    first_name = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

