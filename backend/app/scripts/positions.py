import requests

from app.model import create_position
from app.util.get_config import get_config


# 获取仓位信息
def get_positions(id):
    config = get_config()  # 读取配置文件
    api = config['api']  # 获得api配置
    userDataApi = api['userData']  # 获取大V用户个人信息的url
    eos_url = userDataApi + str(id)  # 拼接爬取的url
    headers = config['headers']  # 获取headers
    res = requests.get(eos_url, headers=headers)  # 获取请求response
    positions = res.json()['data']["futurePosition"]  # 抓取返回的positions列表
    return positions


# 标准化仓位信息
def normalize_positons(list):
    ret = []
    for position in list:
        ret.append(create_position(position))
    return ret


# 最终输出函数
def output_positions(id):
    # 结构化后的仓位
    positions = normalize_positons(get_positions(id))
    print(positions)
    return positions





