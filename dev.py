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

print(os.environ.get("ACCESS_ID"))

# LETS CREATE INSTANCE OF TUYA CLOUD CLIENT
tcc = tuyacloud.TuyaCloudClient(
    ACCESS_ID       = os.environ.get("ACCESS_ID"),
    ACCESS_SECRET   = os.environ.get("ACCESS_SECRET"),
    UID             = os.environ.get("UID"),
    ENDPOINT_URL    = os.environ.get("ENDPOINT_URL")

    # Grey Talon
    # ACCESS_ID       = 'n4gd3u3g3ma5733jayc5',
    # ACCESS_SECRET   = '0311ad61d889402081f19c6891ca4f67',
    # UID             = 'eu1626370410140OlW8o',
    # ENDPOINT_URL    = 'openapi.tuyaeu.com'

)



uri = 'v1.0/devices/bffe4c709473b5ce88d4pk/status'

resp = tcc.custom_request(uri)
print(resp)

'''
IR+RF
wnykq.qykarcgblvlg967t.bf77fac6b9a806178fesax
санузел
rf_curtain.0000003nzg.bf17c9530746a7ad9cwztz
справа
rf_curtain.0000003nzg.bfb9ab1cd20e249fe0vxyo
окно
rf_curtain.0000003nzg.bfb140a36bfa95b021dtyi
слева
rf_curtain.0000003nzg.bf8c58580f78d4fba87mmv
роллеты
rf_diy.0000003o5p.bf49b741a46e40cf07gdpc
'''
#resp = tcc.get_subdevices("bf77fac6b9a806178fesax")
#print(resp) get_remote_controls
#resp = tcc.get_remote_control_keys("bf77fac6b9a806178fesax","bfb09341ec37c0a126zjt3")

#uri ="v1.0/devices/bf77fac6b9a806178fesax/sub-devices"
#resp = tcc.custom_request(uri)

#/bf77fac6b9a806178fesax/bfb140a36bfa95b021dtyi/1/1676159122/power_on/1
#/bf77fac6b9a806178fesax/bf8c58580f78d4fba87mmv/ 1/1676159116/stop/3
uri = 'v2.0/infrareds/124176102462ab16d5fd/remotes/bffe4c709473b5ce88d4pk/raw/command'
post = {
    "category_id": 999,
    "remote_index": 1670108591,
    "key": "1670108550934",
    "key_id": 9
}

uri = 'v2.0/infrareds/124176102462ab16d5fd/remotes/bffe4c709473b5ce88d4pk/command'
post = {
  "categoryId": 999,
  "remoteIndex": 1670108591,
  "key": "1670108550934"
}


uri = 'v1.0/infrareds/124176102462ab16d5fd/remotes/bffe4c709473b5ce88d4pk/send-keys'
post = {
  "key": "1670108550934"
}





'''
Send Key Command
The remote control sends an infrared code to control the specified device through key commands.
POST: /v2.0/infrareds/{infrared_id}/remotes/{remote_id}/raw/command
{
  "category_id": 2,
  "remote_index": 147,
  "key": "power",
  "key_id": 1
}
'''
# post = {
#     "category_id": 999,
#     "remote_index": 1670108591,
#     "key": 1670109573919,
#     "key_id": 12
# }
# resp = tcc.custom_request(uri, 'POST', post)
# uri = 'v2.0/infrareds/124176102462ab16d5fd/remotes/bffe4c709473b5ce88d4pk/raw/command'
# resp = tcc.custom_request(uri, 'POST', post)
# resp = tcc.send_remote_control_command("124176102462ab16d5fd","bffe4c709473b5ce88d4pk", post)
#print(resp)


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