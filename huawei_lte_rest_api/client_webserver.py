from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/webserver/publickey', methods=['GET'])
def get_client_webserver_publickey():
    data = huawei_lte_rest_api.globals.client.webserver.publickey()
    return json.dumps(data)

@api.route('/client/webserver/token', methods=['GET'])
def get_client_webserver_token():
    data = huawei_lte_rest_api.globals.client.webserver.token()
    return json.dumps(data)

@api.route('/client/webserver/white_list_switch', methods=['GET'])
def get_client_webserver_white_list_switch():
    data = huawei_lte_rest_api.globals.client.webserver.white_list_switch()
    return json.dumps(data)
