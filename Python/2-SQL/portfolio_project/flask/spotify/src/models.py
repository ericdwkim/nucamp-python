import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Song(db.Model):
    __tablename__ = 'songs'
    song_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    song_title = db.Column(db.String(128), nullable=False)
    song_writer = db.Column(db.String(128), nullable=False)
    song_producer = db.Column(db.String(128), nullable=False)
    song_length = db.Column(db.Integer, nullable=False)
    release_date = db.Column(db.DateTime, nullable=False)

    # TODO: may need to change release_date datatype
    def __init__(self, song_title: str, song_writer: str, song_producer: str, song_length: int, release_date: datetime.datetime):
        self.song_title = song_title
        self.song_writer = song_writer
        self.song_producer = song_producer
        self.song_length = song_length
        self.release_date = release_date

    # def serialize(self):
        # TODO ?


class Album(db.Model):
    __tablename__ = 'albums'
    album_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    album_title = db.Column(db.String(128), nullable=False)
    album_length = db.Column(db.Integer, nullable=False)
    artwork_url = db.Column(db.String(280), nullable=False)
    num_of_songs = db.Column(db.Integer(2), nullable=False)
    release_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, album_title: str, album_length: int, artwork_url: str, num_of_songs: int, release_date: datetime.datetime):
        self.album_title = album_title
        self.album_length = album_length
        self.artwork_url = artwork_url
        self.num_of_songs = num_of_songs
        self.release_date = release_date
