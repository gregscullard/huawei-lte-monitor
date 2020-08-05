from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/ntwk/lan_upnp_portmapping', methods=['GET'])
def get_client_ntwk_lan_upnp_portmapping():
    data = huawei_lte_rest_api.globals.client.ntwk.lan_upnp_portmapping()
    return json.dumps(data)

@api.route('/client/ntwk/celllock', methods=['GET'])
def get_client_ntwk_celllock():
    data = huawei_lte_rest_api.globals.client.ntwk.celllock()
    return json.dumps(data)

