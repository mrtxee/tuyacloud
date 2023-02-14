import tuyacloud

import json
import logging
import inspect
from logging.handlers import RotatingFileHandler
import os
from dotenv import load_dotenv

if os.path.exists(os.path.join(os.path.dirname(__file__), '.env')):
    load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

# SETUP DEFAULT LOGGER IF YOU WHANT TO SEE HOW tuyacloud WORKS
def setup_logger():
    logger_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger_file_handler = logging.handlers.RotatingFileHandler('tuyacloud.log', maxBytes=51200, backupCount=2)
    logger_file_handler.setLevel(logging.DEBUG)
    logger_file_handler.setFormatter(logger_formatter)
    logger_tuya_cloud_client = logging.getLogger('tuyacloud.TuyaCloudClient')
    logger_tuya_cloud_client.setLevel(logging.DEBUG)
    logger_tuya_cloud_client.addHandler(logger_file_handler)
    logger_tuya_cloud_client.info("script started")
setup_logger()


# создаем экземпляр класса, который будет взаимодействовать с TUYA ENDPOINT
tcc = tuyacloud.TuyaCloudClient(
    ACCESS_ID       = os.environ.get("ACCESS_ID"),
    ACCESS_SECRET   = os.environ.get("ACCESS_SECRET"),
    UID             = os.environ.get("UID"),
    ENDPOINT_URL    = os.environ.get("ENDPOINT_URL")
)

print(os.environ.get("ENDPOINT_URL"))

#user_id = os.environ.get("UID")
#uri = 'v1.0/users/%s/homes' % user_id

# Project Code: p16664581051628jfm7c

# 797uu1@bk.ru
# Access ID:		8rvfccfcvcyxcv53peat
# Access Secret:	04e1df9e25d44a9c8629194b8d828b48
# UID:			eu1676274642418TJPHe


username = "797uu1@bk.ru"
#1. A third-party system server authorizes an account to access the Tuya IoT Development Platform and determines the type of the authorized account.
uri = 'v1.0/industry/auth/admin'
post = {
    "username": username,
}
# resp = tcc.custom_request(uri, 'POST', post)
# print(resp)

#2. The third-party system sends authorized account and country code to the Tuya IoT Development Platform, and requests a ticket.
uri = 'v1.0/industry/auth/ticket'
post = {
    "username": username,
}
resp = tcc.custom_request(uri, 'POST', post)
print(resp)
print(resp['result'])

#3. Grant project space permissions to the account.
#3 lighting.console.tuyacn.com?ticket=aFlcFxRSmYnMdzcM
#POST /v1.0/illumination/account/permission/add
uri = 'v1.0/illumination/account/permission/add'
post = {
    "tuyaUid": os.environ.get("UID"),
    "projectId": "p16664581051628jfm7c",
    "roomIdList": ["21078434","21078435"]
}
# resp = tcc.custom_request(uri, 'POST', post)
# print(resp)