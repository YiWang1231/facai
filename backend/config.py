import os

from dotenv import load_dotenv

base_dir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(base_dir, '.env'))

DOMIAN_NAME = 'root:123456@localhost'
PORT = '3306'


class Config(object):
    SQL_ALCHEMY_DATABASE_URI = (
            'mysql+pymysql://' + DOMIAN_NAME + ':' + PORT + "/coin?charset=utf8"
    )
