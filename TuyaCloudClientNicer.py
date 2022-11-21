from .TuyaCloudClient import *

class TuyaCloudClientNicer(TuyaCloudClient):
    def __cut_metada_decorator(func): # type: ignore
        def decorate( self, *args, **kwargs ) :
            response = func( self, *args, **kwargs ) # type: ignore
            if response['success']:
                response = response['result']
            else:
                raise TuyaCloudClientResponseException("response[result] !True")
            return response
        return decorate
    
    @__cut_metada_decorator  # type: ignore
    def get_device_information(self, device_id=None):
        return super().get_device_information(device_id)
    @__cut_metada_decorator  # type: ignore
    def get_device_details(self, device_id=None):
        return super().get_device_details(device_id)
    @__cut_metada_decorator  # type: ignore
    def get_device_logs(self, device_id=None):
        return super().get_device_logs(device_id)
    @__cut_metada_decorator  # type: ignore
    def get_home_data(self, home_id=None):
        return super().get_home_data(home_id)
    @__cut_metada_decorator  # type: ignore
    def get_home_rooms(self, home_id=None):
        return super().get_home_rooms(home_id)
    @__cut_metada_decorator  # type: ignore
    def get_home_devices(self, home_id=None):
        return super().get_home_devices(home_id)
    @__cut_metada_decorator  # type: ignore
    def get_home_members(self, home_id=None):
        return super().get_home_members(home_id)
    @__cut_metada_decorator  # type: ignore
    def get_room_devices(self, home_id=None, room_id=None):
        return super().get_room_devices(home_id, room_id)
    @__cut_metada_decorator  # type: ignore
    def get_user_homes(self, user_id=None):
        return super().get_user_homes(user_id)
    @__cut_metada_decorator  # type: ignore
    def get_user_devices(self, user_id=None):
        return super().get_user_devices(user_id)
    @__cut_metada_decorator  # type: ignore
    def get_category_list(self):
        return super().get_category_list()

