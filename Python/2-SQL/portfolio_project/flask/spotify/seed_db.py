"""
TODO: Populate spotify database with personal data using the SQLAlchemy ORM.
"""
# import os
# import boto3
# from dotenv import load_dotenv
import random
import string
import hashlib
import secrets
from src.models import Account, Album, Artist, Group, Song, Audio, songs_artists, songs_albums, albums_artists, groups_artists, accounts_artists, db
from src import create_app

# load_dotenv()

# access_key = os.getenv('access_key')
# print(access_key)

# access_secret = os.getenv('access_secret')
# print(access_secret)

# s3_bucket = os.getenv('bucket_name')
# print(s3_bucket)


URIs = [
    "s3://my.audio.tracks/KOGNITIF - Soul Food - 02 Soul Food.mp3",
    "s3://my.audio.tracks/KOGNITIF - Soul Food - 12 Twenty Past Four.mp3",
    "s3://my.audio.tracks/Me and You - Champange Drip & Lucii.mp3",
    "s3://my.audio.tracks/Mickman - Corollary - 02 Curio.mp3",
    "s3://my.audio.tracks/Mickman - Corollary - 03 Tolerance.mp3",
    "s3://my.audio.tracks/Octopus (Original Mix)_83859835_soundcloud.mp3",
    "s3://my.audio.tracks/Release Me- Datsik.mp3",
    "s3://my.audio.tracks/Rock My Soul - Artifakts.mp3",
    "s3://my.audio.tracks/Si Begg- Bangin'.mp3",
    "s3://my.audio.tracks/The Pixies - Where Is My Mind (Bassnectar Remix).mp3",
    "s3://my.audio.tracks/Twenty Past Four.mp3"
]


def random_passhash():
    """Get hashed and salted password of length N | 8 <= N <= 15"""
    raw = ''.join(
        random.choices(
            string.ascii_letters + string.digits + '!@#$%&',  # valid pw characters
            k=random.randint(8, 15)  # length of pw
        )
    )

    salt = secrets.token_hex(16)

    return hashlib.sha512((raw + salt).encode('utf-8')).hexdigest()


def truncate_tables():
    """Delete all rows from database tables"""
    db.session.execute(songs_artists.delete())
    db.session.execute(songs_albums.delete())
    db.session.execute(albums_artists.delete())
    db.session.execute(groups_artists.delete())
    db.session.execute(accounts_artists.delete())
    Song.query.delete()
    Album.query.delete()
    Group.query.delete()
    Account.query.delete()
    Artist.query.delete()
    Audio.query.delete()
    db.session.commit()


def main():
    """Main driver function"""
    app = create_app()
    app.app_context().push()
    truncate_tables()


if __name__ == '__main__':
    main()

"""
store the URI links in the database.
You will need to have a function that saves and returns the location of the sound file so you can store it in your table and
a function that can look up this table and go and load the data from the bucket.


# saves and returns location of audio file from s3 bucket

audioFileLocation  = None # save audio file location

def save_and_return_audio_file_location():
    # 1) store the locations into the audio table
        # sql query stmt: INSERT INTO audios (audio_URI) VALUES ([list_of_URIs?])
    # 2) return location of each audio file from audi

# looks up the audio table, grabs and loads data from s3 bucket
def lookup_and_load_data_from_bucket():
    # 1) look up audio table
    # 2) load data from bucket
"""

audioFIleLocation = None  # save audio file location


def save_return_audioFileLocation():
    for uri in URIs:
        #  INSERT INTO audios (audio_URI) VALUES (uri of URIs)
        insert_uris_query = Audio.insert().values(uri)
        db.session.execute(insert_uris_query)

        # SELECT audio_URI FROM audios;
        return_uris_query = Audio.select(Audio.audio_URI)
        db.session.execute(return_uris_query)
    # insert uris to table
    db.session.commit()
    # return values from return query ?
    return someReturningObject?
