import requests

from app.util.get_config import get_config
from app.model import create_record


# 获取交易记录
def get_deal_records(id):
    config = get_config()
    api = config['api']
    userDealRecordApi = api['userDealRecordApi']
    headers = config['headers']
    params = config['params']
    params['typeStr'] = str(id)
    res = requests.get(userDealRecordApi, headers=headers, params=params)
    return res.json()['data']['firmOfferHisList']


def normalize_records(list):
    ret = []
    for record in list:
        ret.append(create_record(record))
    return ret


def output_records(id):
    records = normalize_records(get_deal_records(id))
    print(records)
    return records


if __name__ == "__main__":
    output_records(97)
