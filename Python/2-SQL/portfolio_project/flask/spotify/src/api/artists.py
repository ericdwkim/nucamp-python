from flask import Blueprint, jsonify, abort, request
from ..models import Artist, db

bp = Blueprint('artists', __name__, url_prefix='/artists')


@bp.route('', methods=['GET'])
