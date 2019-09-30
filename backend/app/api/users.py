from flask import jsonify

from app.api import bp
from app.scripts.parse_user_data import UserData
from app.util.get_config import get_config

config = get_config()


@bp.route('/users', methods=['GET'])
def get_users():
    users = config['users']
    ret = []
    for user in users:
        user_id = user['id']
        print(user_id)
        user_data = UserData(user_id)
        ret.append(user_data.get_user_data())
    return jsonify(ret)
