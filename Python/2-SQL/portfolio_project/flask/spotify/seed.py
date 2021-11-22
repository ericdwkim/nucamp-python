"""
TODO: Populate spotify database with personal data using the SQLAlchemy ORM.
"""
import random
import string
import hashlib
import secrets
from faker import Faker
from spotify.src.models import Account, Album, Artist, Group, Song, songs_artists, songs_albums, albums_artists, groups_artists, accounts_artists
