import json


def get_config():
    with open("/Users/wangyi/Projects/facai/backend/config.json", "r") as f:
        config = json.load(f)
    return config