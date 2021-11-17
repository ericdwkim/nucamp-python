import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

# Song to Artist (many-many relationship helper table)


songs_artists = db.Table('songs_artists',
                         db.Column('song_id', db.Integer,
                                   db.ForeignKey('songs.song_id')),
                         db.Column('artist_id', db.Integer,
                                   db.ForeignKey('artists.artist_id'))
                         )

# Song to Album (many-many helper table)

songs_albums = db.Table('songs_albums',
                        db.Column('song_id', db.Integer,
                                  db.ForeignKey('songs.song_id')),
                        db.Column('album_id', db.Integer,
                                  db.ForeignKey('albums.album_id'))
                        )


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
    num_of_songs = db.Column(db.Integer, nullable=False)
    release_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, album_title: str, album_length: int, artwork_url: str, num_of_songs: int, release_date: datetime.datetime):
        self.album_title = album_title
        self.album_length = album_length
        self.artwork_url = artwork_url
        self.num_of_songs = num_of_songs
        self.release_date = release_date

    # TODO: serialize() ?


class Group(db.Model):
    __tablename__ = 'groups'
    group_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    group_name = db.Column(db.String(128), nullable=False)

    def __init__(self, group_name: str):
        self.group_name = group_name

        # TODO: serialize() ?


class Account(db.Model):
    __tablename__ = 'accounts'
    account_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    user_email = db.Column(db.String(255), unique=True, nullable=False)
    user_password = db.Column(db.String(255), nullable=False)

    def __init__(self, username: str, user_email: str):
        self.username = username
        self.user_email = user_email

        # TODO: serialize() ?


class Artist(db.Model):
    __tablename__ = 'artists'
    artist_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    artist_name = db.Column(db.String(128), nullable=False)
    artist_bio = db.Column(db.String(500))

    artist_songs = db.relationship(
        'Song', secondary=songs_artists, backref=db.backref('writers', lazy='dynamnic'))

    def __init__(self, artist_name: str, artist_bio: str):
        self.artist_name = artist_name
        self.artist_bio = artist_bio

        # TODO: serialize() ?
