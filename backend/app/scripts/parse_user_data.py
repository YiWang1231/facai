from datetime import datetime
import requests
from apscheduler.schedulers.blocking import BlockingScheduler

from app.model import create_record
from app.model import create_position
from app.model import create_status
from app.util.get_config import get_config


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
            return cls._instance


class UserData(Singleton):

    def __init__(self, user_id):
        self.id = user_id

    def get_user_data(self):
        config = get_config()  # 读取配置文件
        api = config['api']  # 获得api配置
        user_data_api = api['userData']  # 获取大V用户个人信息的url
        user_deal_record_api = api['userDealRecordApi']  # 获取交易数据url
        headers = config['headers']
        params_user_data = config['params'][0]
        params_deal_record = config['params'][1]
        params_user_data['userId'] = str(self.id)
        params_deal_record['typeStr'] = str(self.id)  # 填充
        res_user_data = requests.get(user_data_api, headers=headers, params=params_user_data).json()
        res_deal_record = requests.get(user_deal_record_api, headers=headers, params=params_deal_record).json()
        user_balance = res_user_data['data']['balance']
        user_nickname = res_user_data['data']["nickName"]
        status = res_user_data['data']['ratioMap']
        positions = res_user_data['data']['futurePosition']
        records = res_deal_record['data']['firmOfferHisList']
        ret_status = []
        for item in status:
            ret_status.append(create_status(item).status2dict())
        ret_positions = []
        for item in positions:
            ret_positions.append(create_position(item).position2dict())
        ret_records = []
        for item in records:
            ret_records.append(create_record(item).record2dict())
        user_dict = {
            'time': datetime.now(),
            'id': self.id,
            'nickName': user_nickname,
            'balance': user_balance,
            'status': ret_status,
            'positions': ret_positions,
            'records': ret_records
        }
        print(user_dict)
        return user_dict

    def auto_output(self):
        scheduler = BlockingScheduler()
        scheduler.add_job(func=self.get_user_data, trigger='interval', seconds=20, next_run_time=datetime.now(), id='user_data_task')
        try:
            scheduler.start()
        except:
            pass


if __name__ == "__main__":
    user = UserData(97)
    user.auto_output()