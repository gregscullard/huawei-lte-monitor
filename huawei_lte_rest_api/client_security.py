from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/security/bridgemode', methods=['GET'])
def get_client_security_bridgemode():
    data = huawei_lte_rest_api.globals.client.security.bridgemode()
    return json.dumps(data)

@api.route('/client/security/get_firewall_switch', methods=['GET'])
def get_client_security_get_firewall_switch():
    data = huawei_lte_rest_api.globals.client.security.get_firewall_switch()
    return json.dumps(data)

@api.route('/client/security/mac_filter', methods=['GET'])
def get_client_security_mac_filter():
    data = huawei_lte_rest_api.globals.client.security.mac_filter()
    return json.dumps(data)

@api.route('/client/security/lan_ip_filter', methods=['GET'])
def get_client_security_lan_ip_filter():
    data = huawei_lte_rest_api.globals.client.security.lan_ip_filter()
    return json.dumps(data)

@api.route('/client/security/virtual_servers', methods=['GET'])
def get_client_security_virtual_servers():
    data = huawei_lte_rest_api.globals.client.security.virtual_servers()
    return json.dumps(data)

@api.route('/client/security/url_filter', methods=['GET'])
def get_client_security_url_filter():
    data = huawei_lte_rest_api.globals.client.security.url_filter()
    return json.dumps(data)

@api.route('/client/security/upnp', methods=['GET'])
def get_client_security_upnp():
    data = huawei_lte_rest_api.globals.client.security.upnp()
    return json.dumps(data)

@api.route('/client/security/dmz', methods=['GET'])
def get_client_security_dmz():
    data = huawei_lte_rest_api.globals.client.security.dmz()
    return json.dumps(data)

@api.route('/client/security/sip', methods=['GET'])
def get_client_security_sip():
    data = huawei_lte_rest_api.globals.client.security.sip()
    return json.dumps(data)

@api.route('/client/security/feature_switch', methods=['GET'])
def get_client_security_feature_switch():
    data = huawei_lte_rest_api.globals.client.security.feature_switch()
    return json.dumps(data)

@api.route('/client/security/nat', methods=['GET'])
def get_client_security_nat():
    data = huawei_lte_rest_api.globals.client.security.nat()
    return json.dumps(data)

@api.route('/client/security/special_applications', methods=['GET'])
def get_client_security_special_applications():
    data = huawei_lte_rest_api.globals.client.security.special_applications()
    return json.dumps(data)

@api.route('/client/security/white_lan_ip_filter', methods=['GET'])
def get_client_security_white_lan_ip_filter():
    data = huawei_lte_rest_api.globals.client.security.white_lan_ip_filter()
    return json.dumps(data)

@api.route('/client/security/white_url_filter', methods=['GET'])
def get_client_security_white_url_filter():
    data = huawei_lte_rest_api.globals.client.security.white_url_filter()
    return json.dumps(data)

@api.route('/client/security/acls', methods=['GET'])
def get_client_security_acls():
    data = huawei_lte_rest_api.globals.client.security.acls()
    return json.dumps(data)
