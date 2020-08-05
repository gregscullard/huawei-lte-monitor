from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/dial_up/mobile_dataswitch', methods=['GET'])
def get_client_dial_up_mobile_dataswitch():
    data = huawei_lte_rest_api.globals.client.dial_up.mobile_dataswitch()
    return json.dumps(data)

@api.route('/client/dial_up/connection', methods=['GET'])
def get_client_dial_up_connection():
    data = huawei_lte_rest_api.globals.client.dial_up.connection()
    return json.dumps(data)

@api.route('/client/dial_up/dialup_feature_switch', methods=['GET'])
def get_client_dial_up_dialup_feature_switch():
    data = huawei_lte_rest_api.globals.client.dial_up.dialup_feature_switch()
    return json.dumps(data)

@api.route('/client/dial_up/profiles', methods=['GET'])
def get_client_dial_up_profiles():
    data = huawei_lte_rest_api.globals.client.dial_up.profiles()
    return json.dumps(data)

@api.route('/client/dial_up/auto_apn', methods=['GET'])
def get_client_dial_up_auto_apn():
    data = huawei_lte_rest_api.globals.client.dial_up.auto_apn()
    return json.dumps(data)

