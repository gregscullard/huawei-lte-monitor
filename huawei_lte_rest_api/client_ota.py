from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/ota/status', methods=['GET'])
def get_client_ota_status():
    data = huawei_lte_rest_api.globals.client.ota.status()
    return json.dumps(data)
