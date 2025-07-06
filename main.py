import json
from requests import post
from time import sleep
import sys

# Load config
with open("config.json") as f:
    config = json.load(f)

fruit_passport = config["fruit_passport"]
power = int(config["power"])
capacity = int(config["capacity"])
deposit_ask = config["deposit_ask"]

headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 10; SM-A750F Build/QP1A.190711.020)',
    'Host': 'iran.fruitcraft.ir',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'cookie': f'FRUITPASSPORT={fruit_passport}'
}

collect_data = "edata=Gk4KXVpRXRJDSEMTfmMXSA%3D%3D"
deposit_data = "edata=Gk4KUEFQQERbUDpPAwkBAVRZRFQ4UB4aWwoEEA5GW05bAlUECgRTQ1JIBVQEUAVdFwhSQAAJCFsDF1BRBVoMBhFJ"

maining_time = int((capacity) / (power / 3600))

def collect_gold(data, headers):
    try:
        collect = post("http://iran.fruitcraft.ir/cards/collectgold", data=data, headers=headers)
        return collect
    except Exception as e:
        print("Error collecting gold:", e)

def deposit_to_bank(data, headers):
    try:
        deposit = post("http://iran.fruitcraft.ir/player/deposittobank", data=data, headers=headers)
        return deposit
    except Exception as e:
        print("Error depositing:", e)

def run():
    collect_result = collect_gold(collect_data, headers)
    if collect_result is not None and deposit_ask:
        deposit_to_bank(deposit_data, headers)

run()
