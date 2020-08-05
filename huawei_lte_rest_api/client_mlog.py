from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/mlog/mobile_logger', methods=['GET'])
def get_client_mlog_mobile_logger():
    data = huawei_lte_rest_api.globals.client.mlog.mobile_logger()
    return json.dumps(data)
