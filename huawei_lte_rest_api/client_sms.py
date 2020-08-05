from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/sms/get_cbsnewslist', methods=['GET'])
def get_client_sms_get_cbsnewslist():
    data = huawei_lte_rest_api.globals.client.sms.get_cbsnewslist()
    return json.dumps(data)

@api.route('/client/sms/sms_count', methods=['GET'])
def get_client_sms_sms_count():
    data = huawei_lte_rest_api.globals.client.sms.sms_count()
    return json.dumps(data)

@api.route('/client/sms/send_status', methods=['GET'])
def get_client_sms_send_status():
    data = huawei_lte_rest_api.globals.client.sms.send_status()
    return json.dumps(data)

@api.route('/client/sms/get_sms_list', methods=['GET'])
def get_client_sms_get_sms_list():
    data = huawei_lte_rest_api.globals.client.sms.get_sms_list()
    return json.dumps(data)

@api.route('/client/sms/config', methods=['GET'])
def get_client_sms_config():
    data = huawei_lte_rest_api.globals.client.sms.config()
    return json.dumps(data)

@api.route('/client/sms/sms_count_contact', methods=['GET'])
def get_client_sms_sms_count_contact():
    data = huawei_lte_rest_api.globals.client.sms.sms_count_contact()
    return json.dumps(data)

@api.route('/client/sms/get_sms_list_pdu', methods=['GET'])
def get_client_sms_get_sms_list_pdu():
    data = huawei_lte_rest_api.globals.client.sms.get_sms_list_pdu()
    return json.dumps(data)
