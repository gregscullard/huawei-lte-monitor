from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/device/information', methods=['GET'])
def get_client_device_information():
    data = huawei_lte_rest_api.globals.client.device.information()
    return json.dumps(data)

@api.route('/client/device/autorun_version', methods=['GET'])
def get_client_device_autorun_version():
    data = huawei_lte_rest_api.globals.clientdevice.autorun_version()
    return json.dumps(data)

@api.route('/client/device/device_feature_switch', methods=['GET'])
def get_client_device_device_feature_switch():
    data = huawei_lte_rest_api.globals.clientdevice.device_feature_switch()
    return json.dumps(data)

@api.route('/client/device/basic_information', methods=['GET'])
def get_client_device_basic_information():
    data = huawei_lte_rest_api.globals.clientdevice.basic_information()
    return json.dumps(data)

@api.route('/client/device/basicinformation', methods=['GET'])
def get_client_device_basicinformation():
    data = huawei_lte_rest_api.globals.clientdevice.basicinformation()
    return json.dumps(data)

@api.route('/client/device/usb_tethering_switch', methods=['GET'])
def get_client_device_usb_tethering_switch():
    data = huawei_lte_rest_api.globals.clientdevice.usb_tethering_switch()
    return json.dumps(data)

@api.route('/client/device/boot_time', methods=['GET'])
def get_client_device_boot_time():
    data = huawei_lte_rest_api.globals.clientdevice.boot_time()
    return json.dumps(data)

@api.route('/client/device/signal', methods=['GET'])
def get_client_device_signal():
    data = huawei_lte_rest_api.globals.clientdevice.signal()
    return json.dumps(data)

@api.route('/client/device/antenna_status', methods=['GET'])
def get_client_device_antenna_status():
    data = huawei_lte_rest_api.globals.clientdevice.antenna_status()
    return json.dumps(data)

@api.route('/client/device/antenna_type', methods=['GET'])
def get_client_device_antenna_type():
    data = huawei_lte_rest_api.globals.clientdevice.antenna_type()
    return json.dumps(data)

@api.route('/client/device/logsetting', methods=['GET'])
def get_client_device_logsetting():
    data = huawei_lte_rest_api.globals.clientdevice.logsetting()
    return json.dumps(data)
