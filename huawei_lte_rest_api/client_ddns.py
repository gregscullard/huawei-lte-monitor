from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/d_dns/get_ddns_list', methods=['GET'])
def get_client_d_dns_get_ddns_list():
    data = huawei_lte_rest_api.globals.client.d_dns.get_ddns_list()
    return json.dumps(data)

@api.route('/client/d_dns/get_status', methods=['GET'])
def get_client_d_dns_get_status():
    data = huawei_lte_rest_api.globals.client.d_dns.get_status()
    return json.dumps(data)
