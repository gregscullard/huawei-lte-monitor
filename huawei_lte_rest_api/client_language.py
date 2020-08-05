from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/language/current_language', methods=['GET'])
def get_client_language_current_language():
    data = huawei_lte_rest_api.globals.client.language.current_language()
    return json.dumps(data)
