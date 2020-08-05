from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/usb_storage/fsstatus', methods=['GET'])
def get_client_usb_storage_fsstatus():
    data = huawei_lte_rest_api.globals.client.usb_storage.fsstatus()
    return json.dumps(data)

@api.route('/client/usb_storage/usbaccount', methods=['GET'])
def get_client_usb_storage_usbaccount():
    data = huawei_lte_rest_api.globals.client.usb_storage.usbaccount()
    return json.dumps(data)

