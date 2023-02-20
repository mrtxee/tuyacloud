"""
    Tuya Cloud Client Python package
    based on http-API for Tuya IoT Development Platform

    Dev. Artem Mironov
    For more info see https://github.com/mrtxee/tuyacloud

    TUYA CLOUD CLIENT USAGE EXAMPLE
"""
import src.tuyacloud as tuyacloud
import json
import os
from dotenv import load_dotenv

if os.path.exists(os.path.join(os.path.dirname(__file__), '.env')):
    load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

# LETS CREATE INSTANCE OF TUYA CLOUD CLIENT
tcc = tuyacloud.TuyaCloudClientNicer(
    ACCESS_ID       = os.environ.get("ACCESS_ID"),
    ACCESS_SECRET   = os.environ.get("ACCESS_SECRET"),
    UID             = os.environ.get("UID"),
    ENDPOINT_URL    = os.environ.get("ENDPOINT_URL")
)



resp = tcc.get_remote_controls("124176102462ab16d5fd")
#resp = tcc.get_remote_control_keys("124176102462ab16d5fd","bffe4c709473b5ce88d4pk")
print(resp)


# problematic
# bffe4c709473b5ce88d4pk    qt      Звук мультирум пульт, "remote_index": 1670108591,
# 86872105cc50e3e5df73      qt      Датчик угарного газа (CO)
# 124176102462ab16d5fd      wnykq   IR-трансмиттер

# todo: получать инструкции из категории
# bf314b2fd795bd3858tssp    wfcon   Шлюз zigbee
# bf12617223eb936930uixo    wfcon   Шлюз zigbee
# uri = 'v1.0/functions/wfcon'
# resp = tcc.custom_request(uri)
# resp = tcc.get_category_instruction('qt')

def testHomes(tcc):
    # GET LIST OF HOMES UNDER CREDENTIALS PROVIDED
    homes = tcc.get_user_homes()
    if len(homes) > 0:
        print(f"LIST OF HOMES OF {os.environ.get('UID')}:")
        print(homes)
    else:
        print("NO HOMES FOUND.")
#testHomes(tcc)

def testAuth(tcc):
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