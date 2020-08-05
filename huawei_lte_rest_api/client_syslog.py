from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/syslog/querylog', methods=['GET'])
def get_client_syslog_querylog():
    data = huawei_lte_rest_api.globals.client.syslog.querylog()
    return json.dumps(data)

