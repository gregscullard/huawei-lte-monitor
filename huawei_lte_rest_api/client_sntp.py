from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/s_ntp/get_settings', methods=['GET'])
def get_client_s_ntp_get_settings():
    data = huawei_lte_rest_api.globals.client.s_ntp.get_settings()
    return json.dumps(data)

@api.route('/client/s_ntp/sntpswitch', methods=['GET'])
def get_client_s_ntp_sntpswitch():
    data = huawei_lte_rest_api.globals.client.s_ntp.sntpswitch()
    return json.dumps(data)

@api.route('/client/s_ntp/serverinfo', methods=['GET'])
def get_client_s_ntp_serverinfo():
    data = huawei_lte_rest_api.globals.client.s_ntp.serverinfo()
    return json.dumps(data)

@api.route('/client/s_ntp/timeinfo', methods=['GET'])
def get_client_s_ntp_timeinfo():
    data = huawei_lte_rest_api.globals.client.s_ntp.timeinfo()
    return json.dumps(data)

