from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/timerule/timerule', methods=['GET'])
def get_client_timerule_timerule():
    data = huawei_lte_rest_api.globals.client.timerule.timerule()
    return json.dumps(data)



