from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/dhcp/settings', methods=['GET'])
def get_client_dhcp_settings():
    data = huawei_lte_rest_api.globals.client.dhcp.settings()
    return json.dumps(data)

@api.route('/client/dhcp/feature_switch', methods=['GET'])
def get_client_dhcp_feature_switch():
    data = huawei_lte_rest_api.globals.client.dhcp.feature_switch()
    return json.dumps(data)

@api.route('/client/dhcp/dhcp_host_info', methods=['GET'])
def get_client_dhcp_dhcp_host_info():
    data = huawei_lte_rest_api.globals.client.dhcp.dhcp_host_info()
    return json.dumps(data)

@api.route('/client/dhcp/static_addr_info', methods=['GET'])
def get_client_dhcp_static_addr_info():
    data = huawei_lte_rest_api.globals.client.dhcp.static_addr_info()
    return json.dumps(data)
