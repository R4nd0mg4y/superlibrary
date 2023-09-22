from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime
import pytz

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    author = db.Column(db.String(128))
    publication_date = db.Column(db.Date)
    cover = db.Column(db.String(256))  # Trường cover để lưu tên file hình ảnh
    content = db.Column(db.String(256))  # Trường content để lưu tên file PDF
    notes = db.relationship('Note') # Quan hệ một-nhiều với Ghi chú

# Mô hình cho Ghi chú (Notes)


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
    notes = db.relationship('Note')
