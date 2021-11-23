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


"""
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


    audio = Audio(uri=uri)
        session.add(audio)
    session.commit()


    for audio in tracks:
    ret_uri, status = amzn.s3.save(path, audio)
    if status:
         saved_audio = Audio(uri=ret_uri)
         session.add(saved_audio)

session.commit()
"""

# TODO: programmatically fetch (from s3) and store (to sql db) URIs for each s3 object


def ret_uri():
    # TODO: fetches uris from s3 bucket and returns uri object


def store_uri():
    # TODO: stores returned uri object to sql db table


if __name__ == '__main__':
    main()
