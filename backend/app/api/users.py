from datetime import datetime
from flask import jsonify
from app.api import bp
from app.scripts.positions import output_positions
from app.scripts.records import output_records
from app.util.get_config import get_config


@bp.route('/users', methods=['GET'])
def get_users():
    # 读取配置文件
    config = get_config()
    usersId = config['parseUsersId']
    return jsonify(usersId)


@bp.route('/positions/<int:id>', methods=['GET'])
def get_position(id):
    positions = output_positions(id)
    ret = []
    for position in positions:
        ret.append(position.position2dict())
    return jsonify({
        "time": datetime.now(),
        "id": id,
        "positions": ret
    })


@bp.route('/records/<int:id>', methods=['GET'])
def get_user_records(id):
    records = output_records(id)
    ret = []
    for record in records:
        ret.append(record.position2dict())
    return jsonify({
        "time": datetime.now(),
        "id": id,
        "dealRecords": ret
    })