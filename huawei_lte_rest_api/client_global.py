from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/global/module_switch', methods=['GET'])
def get_client_global_module_switch():
    global client
    data = huawei_lte_rest_api.globals.client.global_.module_switch()
    return json.dumps(data)
