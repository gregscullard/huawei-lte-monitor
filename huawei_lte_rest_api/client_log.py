from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/log/loginfo', methods=['GET'])
def get_client_log_loginfo():
    data = huawei_lte_rest_api.globals.client.log.loginfo()
    return json.dumps(data)
