"""
TODO: Populate spotify database with personal data using the SQLAlchemy ORM.
"""
import os
import boto3
from dotenv import load_dotenv
import random
import string
import hashlib
import secrets
import urllib
from src.models import Account, Album, Artist, Group, Song, Audio, songs_artists, songs_albums, albums_artists, groups_artists, accounts_artists, db
from src import create_app

# Load environmental variables
load_dotenv()
access_key = os.getenv('access_key')
access_secret = os.getenv('access_secret')
s3_bucket = os.getenv('bucket_name')


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


# def random_passhash():
#     # Get hashed and salted password of length N | 8 <= N <= 15
#     raw = ''.join(
#         random.choices(
#             string.ascii_letters + string.digits + '!@#$%&',  # valid pw characters
#             k=random.randint(8, 15)  # length of pw
#         )
#     )

#     salt = secrets.token_hex(16)

#     return hashlib.sha512((raw + salt).encode('utf-8')).hexdigest()


# def truncate_tables():
#     # Delete all rows from database tables
#     db.session.execute(songs_artists.delete())
#     db.session.execute(songs_albums.delete())
#     db.session.execute(albums_artists.delete())
#     db.session.execute(groups_artists.delete())
#     db.session.execute(accounts_artists.delete())
#     Song.query.delete()
#     Album.query.delete()
#     Group.query.delete()
#     Account.query.delete()
#     Artist.query.delete()
#     Audio.query.delete()
#     db.session.commit()


def main():
    # Main driver function
    # app = create_app()
    # app.app_context().push()
    # truncate_tables()

    # Connect to S3 service
    s3 = boto3.client(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=access_secret
    )

    # TODO: object url requires configuring permissions for each individual s3 object;
    # programmatically access each s3 object; see SAMPLE ACL:

    """
    https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#sample-acl
    https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html
    https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-arn-format.html
    https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-policy-language-overview.html
    
    """

    # TODO: return fetched URL objects?
    # fetch s3 object URLs; NOTE: req's permissions to play
    # print((k['Key'])) # NOTE: returns audio file

    prefix = "https://s3.us-east-2.amazonaws.com/my.audio.tracks/"
    for k in s3.list_objects(Bucket=s3_bucket)['Contents']:
        print(prefix + urllib.parse.quote(k['Key'], safe="~()*!.'"))


# def store_uri():
#     # TODO: stores returned uri objects to sql db table
#     audio = Audio(audio_URI=URIs)
#     db.session.add(audio)
#     db.session.commit()


# store_uri()

if __name__ == '__main__':
    main()
