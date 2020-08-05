from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/pin/status', methods=['GET'])
def get_client_pin_status():
    data = huawei_lte_rest_api.globals.client.pin.status()
    return json.dumps(data)

@api.route('/client/pin/simlock', methods=['GET'])
def get_client_pin_simlock():
    data = huawei_lte_rest_api.globals.client.pin.simlock()
    return json.dumps(data)

@api.route('/client/pin/save_pin', methods=['GET'])
def get_client_pin_save_pin():
    data = huawei_lte_rest_api.globals.client.pin.save_pin()
    return json.dumps(data)
