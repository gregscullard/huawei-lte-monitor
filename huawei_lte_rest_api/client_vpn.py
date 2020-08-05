from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/vpn/feature_switch', methods=['GET'])
def get_client_vpn_feature_switch():
    data = huawei_lte_rest_api.globals.client.vpn.feature_switch()
    return json.dumps(data)

@api.route('/client/vpn/br_list', methods=['GET'])
def get_client_vpn_br_list():
    data = huawei_lte_rest_api.globals.client.vpn.br_list()
    return json.dumps(data)

@api.route('/client/vpn/ipsec_settings', methods=['GET'])
def get_client_vpn_ipsec_settings():
    data = huawei_lte_rest_api.globals.client.vpn.ipsec_settings()
    return json.dumps(data)

@api.route('/client/vpn/l2tp_settings', methods=['GET'])
def get_client_vpn_l2tp_settings():
    data = huawei_lte_rest_api.globals.client.vpn.l2tp_settings()
    return json.dumps(data)

@api.route('/client/vpn/pptp_settings', methods=['GET'])
def get_client_vpn_pptp_settings():
    data = huawei_lte_rest_api.globals.client.vpn.pptp_settings()
    return json.dumps(data)

@api.route('/client/vpn/status', methods=['GET'])
def get_client_vpn_status():
    data = huawei_lte_rest_api.globals.client.vpn.status()
    return json.dumps(data)

