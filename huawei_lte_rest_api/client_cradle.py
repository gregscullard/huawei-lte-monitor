from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/cradle/status_info', methods=['GET'])
def get_client_cradle_status_info():
    data = huawei_lte_rest_api.globals.client.cradle.status_info()
    return json.dumps(data)

@api.route('/client/cradle/feature_switch', methods=['GET'])
def get_client_cradle_feature_switch():
    data = huawei_lte_rest_api.globals.client.cradle.feature_switch()
    return json.dumps(data)

@api.route('/client/cradle/basic_info', methods=['GET'])
def get_client_cradle_basic_info():
    data = huawei_lte_rest_api.globals.client.cradle.basic_info()
    return json.dumps(data)

@api.route('/client/cradle/factory_mac', methods=['GET'])
def get_client_cradle_factory_mac():
    data = huawei_lte_rest_api.globals.client.cradle.factory_mac()
    return json.dumps(data)

@api.route('/client/cradle/mac_info', methods=['GET'])
def get_client_cradle_mac_info():
    data = huawei_lte_rest_api.globals.client.cradle.mac_info()
    return json.dumps(data)

