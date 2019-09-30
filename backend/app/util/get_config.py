import json
import os
from config import base_dir


def get_config():
    f_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
    with open(os.path.join(base_dir, "config.json"), "r") as f:
        config = json.load(f)
    return config
