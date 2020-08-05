from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/online_update/check_new_version', methods=['GET'])
def get_client_online_update_check_new_version():
    data = huawei_lte_rest_api.globals.client.online_update.check_new_version()
    return json.dumps(data)

@api.route('/client/online_update/status', methods=['GET'])
def get_client_online_update_status():
    data = huawei_lte_rest_api.globals.client.online_update.status()
    return json.dumps(data)

@api.route('/client/online_update/url_list', methods=['GET'])
def get_client_online_update_url_list():
    data = huawei_lte_rest_api.globals.client.online_update.url_list()
    return json.dumps(data)

@api.route('/client/online_update/ack_newversion', methods=['GET'])
def get_client_online_update_ack_newversion():
    data = huawei_lte_rest_api.globals.client.online_update.ack_newversion()
    return json.dumps(data)

@api.route('/client/online_update/cancel_downloading', methods=['GET'])
def get_client_online_update_cancel_downloading():
    data = huawei_lte_rest_api.globals.client.online_update.cancel_downloading()
    return json.dumps(data)

@api.route('/client/online_update/upgrade_messagebox', methods=['GET'])
def get_client_online_update_upgrade_messagebox():
    data = huawei_lte_rest_api.globals.client.online_update.upgrade_messagebox()
    return json.dumps(data)

@api.route('/client/online_update/configuration', methods=['GET'])
def get_client_online_update_configuration():
    data = huawei_lte_rest_api.globals.client.online_update.configuration()
    return json.dumps(data)

@api.route('/client/online_update/autoupdate_config', methods=['GET'])
def get_client_online_update_autoupdate_config():
    data = huawei_lte_rest_api.globals.client.online_update.autoupdate_config()
    return json.dumps(data)

@api.route('/client/online_update/redirect_cancel', methods=['GET'])
def get_client_online_update_redirect_cancel():
    data = huawei_lte_rest_api.globals.client.online_update.redirect_cancel()
    return json.dumps(data)
