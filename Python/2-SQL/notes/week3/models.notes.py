import datetime
from flask_sqlalchemy import SQLAlchemy

# creating a db adapter using SQLAlchemy
db = SQLAlchemy()

# Reference:
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
# https://docs.sqlalchemy.org/en/14/core/metadata.html#sqlalchemy.schema.Column
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#many-to-many-relationships


# creates User as a subclass of SQLAlchemy's db.Model class

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    # back reference (part 1)
    tweets = db.relationship('Tweet', backref='user', cascade="all,delete")

# creates Like model; a many-to-many relationship w/ User and Tweet


likes_table = db.Table(
    'likes',
    db.Column(
        'user_id', db.Integer,
        db.ForeignKey('users.id'),
        primary_key=True
    ),

    db.Column(
        'tweet_id', db.Integer,
        db.ForeignKey('tweets.id'),
        primary_key=True
    ),

    db.Column(
        'created_at', db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )
)


# creates Tweet model

class Tweet(db.Model):
    __tablename__ = 'tweets'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(280), nullable=False)
    created_at = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )

    # equivalent to adding the fk column; creates the relationship b/w User and Tweet models
    # and thus the tweets table and the users table
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # back reference (part 2)
    likes = db.relationship(
        'User', secondary=likes_table,
        lazy='subquery',
        backref=db.backref('liked_tweets', lazy=True)
    )
