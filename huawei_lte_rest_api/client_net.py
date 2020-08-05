from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/net/current_plmn', methods=['GET'])
def get_client_net_current_plmn():
    data = huawei_lte_rest_api.globals.client.net.current_plmn()
    return json.dumps(data)

@api.route('/client/net/net_mode', methods=['GET'])
def get_client_net_net_mode():
    data = huawei_lte_rest_api.globals.client.net.net_mode()
    return json.dumps(data)

@api.route('/client/net/network', methods=['GET'])
def get_client_net_network():
    data = huawei_lte_rest_api.globals.client.net.network()
    return json.dumps(data)

@api.route('/client/net/register', methods=['GET'])
def get_client_net_register():
    data = huawei_lte_rest_api.globals.client.net.register()
    return json.dumps(data)

@api.route('/client/net/net_mode_list', methods=['GET'])
def get_client_net_net_mode_list():
    data = huawei_lte_rest_api.globals.client.net.net_mode_list()
    return json.dumps(data)

@api.route('/client/net/plmn_list', methods=['GET'])
def get_client_net_plmn_list():
    data = huawei_lte_rest_api.globals.client.net.plmn_list()
    return json.dumps(data)

@api.route('/client/net/net_feature_switch', methods=['GET'])
def get_client_net_net_feature_switch():
    data = huawei_lte_rest_api.globals.client.net.net_feature_switch()
    return json.dumps(data)

@api.route('/client/net/cell_info', methods=['GET'])
def get_client_net_cell_info():
    data = huawei_lte_rest_api.globals.client.net.cell_info()
    return json.dumps(data)

@api.route('/client/net/csps_state', methods=['GET'])
def get_client_net_csps_state():
    data = huawei_lte_rest_api.globals.client.net.csps_state()
    return json.dumps(data)
