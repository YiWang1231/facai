from flask import jsonify
from app.api import bp


@bp.route('/ping', methods=['GET'])
def ping():
    return jsonify('Pong!')


@bp.route('/pong', methods=['GET'])
def pong():
    return jsonify('Ping!')
