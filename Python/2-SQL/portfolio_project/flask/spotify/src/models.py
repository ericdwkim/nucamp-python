import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

# Song to Artist (many-many relationship helper table)


songs_artists = db.Table('songs_artists',
                         db.Column('song_id', db.Integer,
                                   db.ForeignKey('songs.song_id'), primary_key=True),
                         db.Column('artist_id', db.Integer,
                                   db.ForeignKey('artists.artist_id'), primary_key=True)
                         )

# Song to Album (many-many helper table)

songs_albums = db.Table('songs_albums',
                        db.Column('song_id', db.Integer,
                                  db.ForeignKey('songs.song_id'), primary_key=True),
                        db.Column('album_id', db.Integer,
                                  db.ForeignKey('albums.album_id'), primary_key=True)
                        )

# Album to Artist (many-many helper table)

albums_artists = db.Table('albums_artists',
                          db.Column('album_id', db.Integer,
                                    db.ForeignKey('albums.album_id'), primary_key=True),
                          db.Column('artist_id', db.Integer,
                                    db.ForeignKey('artists.artist_id'), primary_key=True)
                          )

# Group to Artist (many-many helper table)

groups_artists = db.Table('groups_artists',
                          db.Column('group_id', db.Integer,
                                    db.ForeignKey('groups.group_id'), primary_key=True),
                          db.Column('artist_id', db.Integer,
                                    db.ForeignKey('artists.artist_id'), primary_key=True)
                          )
# Account to Artist (many-many helper table)

accounts_artists = db.Table('accounts_artists',
                            db.Column('account_id', db.Integer,
                                      db.ForeignKey('accounts.account_id'), primary_key=True),
                            db.Column('artist_id', db.Integer,
                                      db.ForeignKey('artists.artist_id'), primary_key=True)
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
    def serialize(self):
        return {
            'song_id': self.song_id,
            'song_title': self.song_title,
            'song_writer': self.song_writer,
            'song_producer': self.song_producer,
            'song_length': self.song_length,
            'release_date': self.release_date
        }


class Album(db.Model):
    __tablename__ = 'albums'
    album_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    album_title = db.Column(db.String(128), nullable=False)
    album_length = db.Column(db.Integer, nullable=False)
    artwork_url = db.Column(db.String(280), nullable=False)
    num_of_songs = db.Column(db.Integer, nullable=False)
    release_date = db.Column(db.DateTime, nullable=False)

    song = db.relationship(
        'Song', secondary=songs_albums, backref=db.backref('album', lazy='select')
    )
    artist = db.relationship(
        'Artist', secondary=albums_artists, backref=db.backref('album', lazy='select'))

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

    member = db.relationship(
        'Artist', secondary=groups_artists, backref=db.backref('members', lazy='select'))

    def __init__(self, group_name: str):
        self.group_name = group_name

        # TODO: serialize() ?
    def serialize(self):
        print("this is self.group_member", self.group_member)
        return {
            'group_id': self.group_id,
            'group_name': self.group_name,
        }


class Account(db.Model):
    __tablename__ = 'accounts'
    account_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    user_email = db.Column(db.String(255), unique=True, nullable=False)
    user_password = db.Column(db.String(255), nullable=False)

    artist = db.relationship(
        'Artist', secondary=accounts_artists, backref=db.backref('account', lazy='select'))

    def __init__(self, username: str, user_email: str):
        self.username = username
        self.user_email = user_email

        # TODO: serialize() ?


class Artist(db.Model):
    __tablename__ = 'artists'
    artist_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    artist_name = db.Column(db.String(128), nullable=False)
    artist_bio = db.Column(db.String(500))

    song = db.relationship(
        'Song', secondary=songs_artists, backref=db.backref('artist', lazy='select'))

    def __init__(self, artist_name: str):
        self.artist_name = artist_name
        # self.artist_bio = artist_bio # nullable

        # TODO: serialize() ?
    def serialize(self):
        # print("this is self.artist_song", self.artist_song)
        return {
            'artist_id': self.artist_id,
            'artist_name': self.artist_name,
            'artist_bio': self.artist_bio
        }


class Audio(db.Model):
    __tablename__ = 'audios'
    audio_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    audio_url = db.Column(db.String(256), nullable=False)

    def __init__(self, audio_url: str):
        self.audio_url = audio_url
