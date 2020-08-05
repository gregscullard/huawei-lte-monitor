from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/time/timeout', methods=['GET'])
def get_client_time_timeout():
    data = huawei_lte_rest_api.globals.client.time.timeout()
    return json.dumps(data)
