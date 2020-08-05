from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/pb/get_pb_list', methods=['GET'])
def get_client_pb_get_pb_list():
    data = huawei_lte_rest_api.globals.client.pb.get_pb_list()
    return json.dumps(data)

@api.route('/client/pb/pb_count', methods=['GET'])
def get_client_pb_pb_count():
    data = huawei_lte_rest_api.globals.client.pb.pb_count()
    return json.dumps(data)

@api.route('/client/pb/group_count', methods=['GET'])
def get_client_pb_group_count():
    data = huawei_lte_rest_api.globals.client.pb.group_count()
    return json.dumps(data)

