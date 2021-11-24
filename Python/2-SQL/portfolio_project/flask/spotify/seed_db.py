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


def main():
    # Main driver function
    app = create_app()
    app.app_context().push()
    # truncate_tables()

    # Connect to S3 service
    s3 = boto3.client(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=access_secret
    )

    def toList(s):
        list_resp = list(s.split(" "))
        return list_resp

    def store_urls(list_url):
        # iterate through each url element in list_url
        # store each url element into audios table, creating new audio records w/ respective urls
        for url in list_url:
            audio = Audio(url)
            db.session.add(audio)
        db.session.commit()

        """
        NOTE: print((k['Key'])) # returns audio file
        NOTE: print(list_url_objs) # returns urls in list data structure

        """

    prefix = "https://s3.us-east-2.amazonaws.com/my.audio.tracks/"
    for k in s3.list_objects(Bucket=s3_bucket)['Contents']:
        list_url_obj = toList(
            prefix + urllib.parse.quote(k['Key'], safe="~()*!.'"))
        store_urls(list_url_obj)

    # TODO: object url requires configuring permissions for each individual s3 object;
    # programmatically access each s3 object; see SAMPLE ACL:


if __name__ == '__main__':
    main()
