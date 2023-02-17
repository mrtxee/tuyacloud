# Tuya Cloud Client
Tuya Cloud Client Python package based on http-API for [Tuya IoT Development Platform](https://developer.tuya.com/en/docs/iot). TuyaCloudClient provides full fuctionality for remote manipulation with Tuya IoT platform based smart devices.

# Overview
Tuya Cloud Client implies quick client functionality for an easy interaction with Tuya services. Most suitable for building software with Tuya API integrated services.

Major fuctionality of Tuya Cloud Client package is based on two classes: **TuyaCloudClient & TuyaCloudClientNicer**. TuyaCloudClientNicer is an extension over TuyaCloudClient. It provides just the same methods, but brings  more significant data in responses, cleaned from meta. Usage of TuyaCloudClientNicer class is preferable for the most cases. 

## Functionality
Intuitive functional interface of a service object
 - get_user_homes()
 - get_user_devices()
 - get_device_information(device_id:uuid)
 - get_device_details(device_id:uuid)
 - get_device_functions(device_id:uuid)
 - get_device_specifications(device_id:uuid)
 - get_device_status(device_id:uuid)
 - get_device_logs(device_id:uuid)
 - get_home_data(home_id:int)
 - get_home_rooms(home_id:int)
 - get_home_devices(home_id:int)
 - get_home_members(home_id:int)
 - get_room_devices(home_id:int, room_id:int)
 - get_category_list()
 - get_category_instruction(category:str)
 - exec_device_command(device_id:uuid, commands:JSON)

## Installation

    python3 -m pip install tuyacloud

## Getting started
OOP based package

### Initiation of an object
    tcc = tuyacloud.TuyaCloudClientNicer(
        ACCESS_ID       = 'XXXXXXXXXXXXXX',
        ACCESS_SECRET   = 'XXXXXXXXXXXXXX',
        UID             = 'XXXXXXXXXXXXXX',
        ENDPOINT_URL    = 'XXXXXXXXXXXXXX'
    )

Credentials **ACCESS_ID, ACCESS_SECRET, UID** could be claimed at [iot.tuya.com](https://iot.tuya.com). **ENDPOINT_URL** is to be chosen by user from 

#### List of tuya endpoints:
    Availability zone	Endpoint
    America	            openapi.tuyaus.com
    China	            openapi.tuyacn.com
    Europe	            openapi.tuyaeu.com
    India	            openapi.tuyain.com
    Eastern America	    openapi-ueaz.tuyaus.com
    Western Europe	    openapi-weaz.tuyaeu.com

### Getting data from tuya endpoint, example
Call methods

    homes = tcc.get_user_homes()
    print(homes)
    
Get response

    [
        {
            "geo_name": "Hong-Kong, Main str. 2716",
            "home_id": 1490003,
            "lat": 00.460004060004,
            "lon": 00.219918549988,
            "name": "Bachelor Condo",
            "role": "OWNER"
        },
        ...
    ]
### Execute command over device, example
Call methods

    device_uuid = "3217xxxxxxxxxxx"
    commands = []
    commands.append({
        "code": "switch_led_1",
        "value": True
    })
    exec_result = tcc.exec_device_command(device_uuid, {"commands": commands})
    print(exec_result)

Get response

    {
        "result": True,
        "success": True,
        "t": 1676636545787,
        "tid": "bcc21939aebd11ed838e2a0aa76353ad"
    }

### Use built-in logger functionality, example
You may capture logs by setting logger with id **tuyacloud.TuyaCloudClient** like so

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

## Links
For more info see [github.com/mrtxee/tuyacloud](https://github.com/mrtxee/tuyacloud)