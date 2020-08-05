from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/redirection/homepage', methods=['GET'])
def get_client_redirection_homepage():
    data = huawei_lte_rest_api.globals.client.redirection.homepage()
    return json.dumps(data)
