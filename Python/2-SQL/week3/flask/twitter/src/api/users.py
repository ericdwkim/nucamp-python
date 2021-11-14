from flask import Blueprint, jsonify, abort, request
from sqlalchemy.sql.functions import char_length
from ..models import Tweet, User, db
import hashlib
import secrets


def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()


bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('', methods=['GET'])
def index():
    users = User.query.all()
    result = []
    for u in users:
        result.append(u.serialize())
    return jsonify(result)


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    u = User.query.get_or_404(id)
    return jsonify(u.serialize())


@bp.route('', methods=['POST'])
def create():
    # req body must contain username, password
    if 'username' not in request.json or 'password' not in request.json:
        return abort(400)
    # username < 3 chars; password < 8 chars
    if len(request.json['username']) < 3 or len(request.json['password']) < 8:
        return abort(400)
    # cosntruct User
    u = User(
        username=request.json['username'],
        password=scramble(request.json['password'])
    )

    db.session.add(u)
    db.session.commit()
    return jsonify(u.serialize())


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    u = User.query.get_or_404(id)
    try:
        db.session.delete(u)  # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)


@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id: int):
    u = User.query.get_or_404(id)
    try:
        # prevents edge case where user could create() then update()
        if len(request.json['username']) < 3 or len(request.json['password']) < 8:
            return abort(400)
        if 'username' in request.json:
            u.username = request.json['username']
        if 'password' in request.json:
            u.password = scramble(request.json['password'])
        db.session.commit()
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)


# docker exec -it pg_container psql -U postgres -d twitter -c
# 'SELECT l.user_id, u.username FROM likes l JOIN users u
# ON l.user_id = u.id WHERE l.tweet_id = 50;'
@bp.route('/<int:id>/liked_tweets', methods=['GET'])
def liking_users(id: int):
    liked_tweets = User.query.get_or_404(id)
    result = []
    for tweet in liked_tweets.tweets:
        result.append(tweet.serialize())
    return jsonify(result)

# @bp.route('/<int:id>/liked_tweets', methods=['GET'])
# def liked_tweets(id: int):
#     liked_tweets = User.query.get_or_404(id)
