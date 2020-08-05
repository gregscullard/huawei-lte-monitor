from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/usermanual_public_sys_resources/config', methods=['GET'])
def get_client_usermanual_public_sys_resources_config():
    data = huawei_lte_rest_api.globals.client.usermanual_public_sys_resources.config()
    return json.dumps(data)

