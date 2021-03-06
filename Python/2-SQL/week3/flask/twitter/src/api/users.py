from flask import Blueprint, jsonify, abort, request
import sqlalchemy
from sqlalchemy.sql.functions import char_length
from ..models import Tweet, User, db, likes_table
import hashlib
import secrets
from sqlalchemy import insert


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
        # if len(request.json['username']) < 3 or len(request.json['password']) < 8:
        #     return abort(400)
        if 'username' in request.json:
            if len(request.json['username']) > 3:
                u.username = request.json['username']
            else:
                return abort(400)
        if 'password' in request.json:
            if len(request.json['password']) > 8:
                u.password = scramble(request.json['password'])
            else:
                return abort(400)
        db.session.commit()
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)


# tweets liked by a specific user


@bp.route('/<int:id>/liked_tweets', methods=['GET'])
def liked_tweets(id: int):
    lt = User.query.get_or_404(id)
    result = []
    for t in lt.liked_tweets:
        result.append(t.serialize())
    return jsonify(result)


@bp.route('/<int:id>/likes', methods=['POST'])
def like_a_tweet(id: int):
    if 'tweet_id' not in request.json:
        return abort(400)
    tweet_id = request.json['tweet_id']
    User.query.get_or_404(id)
    Tweet.query.get_or_404(tweet_id)
    try:
        stmt = insert(likes_table).values(user_id=id, tweet_id=tweet_id)
        db.session.execute(stmt)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)


@bp.route('/<int:user_id>/likes/<int:tweet_id>', methods=['DELETE'])
def unlike_a_tweet(user_id: int, tweet_id: int):
    User.query.get_or_404(user_id)
    Tweet.query.get_or_404(tweet_id)
    try:
        stmt = sqlalchemy.delete(likes_table).where(
            likes_table.c.user_id == user_id, likes_table.c.tweet_id == tweet_id)
        db.session.execute(stmt)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)
