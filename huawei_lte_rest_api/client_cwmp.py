from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/cwmp/basic_info', methods=['GET'])
def get_client_cwmp_basic_info():
    data = huawei_lte_rest_api.globals.client.cwmp.basic_info()
    return json.dumps(data)

