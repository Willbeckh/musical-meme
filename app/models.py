from app import db
from datetime import datetime
from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    profile_pic = db.Column(db.String(20))
    bio = db.Column(db.String(200))
    password_hash = db.Column(db.String(120))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    post_id = db.relationship('Post', backref='author', lazy='dynamic')
    comment_id = db.relationship('Comment', backref='author', lazy='dynamic')

    def set_password(self, password):
        """ Method to create a hashed password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        '''Verifies if a password is hashed.'''
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User: {self.username}>'


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    body = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_comment = db.relationship('Comment', backref='post', lazy='dynamic')

    def __repr__(self):
        return f'<Post: {self.title}>'


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    def __repr__(self):
        return f'<Comment: {self.comment}>'
