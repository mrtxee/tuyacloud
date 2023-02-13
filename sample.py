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
    #logger_tuya_cloud_client.setLevel(logging.ERROR)
    logger_tuya_cloud_client.addHandler(logger_file_handler)
    logger_tuya_cloud_client.info("script started")
setup_logger()

#print('your input is: ', input('Введите строку: '))
print('''TODO:
    - авторизоваться в TUYA CLOUD
    - получить список устройств в аккаунте
    - для устройства с заданным идентификатором задать прочитать его состояние и функции
    - дернуть первую функцию устройства
''');

# создаем экземпляр класса, который будет взаимодействовать с TUYA ENDPOINT
tcc = tuyacloud.TuyaCloudClientNicer(
    ACCESS_ID       = os.environ.get("ACCESS_ID"),
    ACCESS_SECRET   = os.environ.get("ACCESS_SECRET"),
    UID             = os.environ.get("UID"),
    ENDPOINT_URL    = os.environ.get("ENDPOINT_URL")
)


# homes = tcc.get_user_homes()
# rooms = tcc.get_home_rooms(home_id)['rooms']
# tcc.get_user_devices()
# tcc.get_room_devices(room['home_id'], room['room_id'])
# tcc.get_device_functions(DEVICE_UUID)
# tcc.get_device_status(DEVICE_UUID)
# tcc.exec_device_command(DEVICE_UUID, exec)



# GET LIST OF HOMES
homes = tcc.get_user_homes()
if len(homes) > 0:
    print(f"LIST OF HOMES OF {os.environ.get('UID')}:")
    print(homes)
    # GET LIST OF ROOMS FOR THE FIRST HOME
    if 'home_id' in homes[0]:
        rooms = tcc.get_home_rooms(homes[0]['home_id'])['rooms']
        # GET LIST OF DEVICES FOR THE FIST ROOM IN THE FIRST HOME
        if len(rooms) > 0:
            print(f"LIST OF ROOMS IN {homes[0]['home_id']}:")
            print(rooms)
            if 'room_id' in rooms[0]:
                devices = tcc.get_room_devices(homes[0]['home_id'], rooms[0]['room_id'])
                print(f"DEVICES IN {homes[0]['home_id']}/{rooms[0]['room_id']} ARE:")
                print(devices)
            else:
                print("NO ROOMS FOUND.")
                # GET ALL DEVICES AVAILABLE
                print("ALL DEVICES ARE:")
                devices = tcc.get_user_devices()
                print(devices)
else:
    print("NO HOMES FOUND.")

# GET CURRENT DEVICE STATE & LIST OF DEVICE FUNCTIONS AVAILABLE
devices_index = 1
if len(devices) > devices_index:
    if 'uuid' in devices[devices_index]:
        device_uuid = devices[devices_index]['uuid']
        device_status = tcc.get_device_status(device_uuid)
        print(f"DEVICE {device_uuid} STATE IS:")
        print(device_status)
        device_functions = tcc.get_device_functions(device_uuid)
        if 'success' in device_functions:
            if False == device_functions['success']:
                print(f"DEVICE {device_uuid} HAS METHODS AVAILABLE. TRY ANOTHER DEVICE.")
            else:
                print(f"DEVICE HAS FUNCTIONS RESPONSE ERROR:")
                print(device_functions)
        else:
            print(f"DEVICE {device_uuid} FUNCTIONS ARE:")
            print(device_functions)
            # execute command based on device_function
            function_index = 0
            if len(device_functions['functions']) >= function_index:
                function = device_functions['functions'][function_index]
                print(f"DEVICE FUNCTION IS:")
                print(function)
                commands = []
                if 'Boolean'==function['type']:
                    commands.append({
                        "code": function['code'],
                        "value": True
                    })
                elif 'Integer'==function['type']:
                    int_values = json.loads(function['values'])
                    commands.append({
                        "code": function['code'],
                        "value": int_values['min']+int_values['step']
                    })
                elif 'Enum'==function['type']:
                    enum_values = json.loads(function['values'])['range']
                    commands.append({
                        "code": function['code'],
                        "value": enum_values[0]
                    })
                else:
                    print(f"There is no execution method provided for function type {function['type']}")
                if len(commands) > 0:
                    print(f"APPLY TO EXECUTE FOR {device_uuid}:")
                    print(commands)
                    print("RESULT OF EXECUTION:")
                    exec_result = tcc.exec_device_command(device_uuid, {"commands": commands})
                    print(exec_result)
                else:
                    print(f'There is no commands to execute for {device_uuid}.')
            else:
                print(f'device {device_uuid} has no function with index {function_index}. Try another device.')
else:
    print(f"There is not device with index {devices_index} under your account. Add some devices or try another account.")
