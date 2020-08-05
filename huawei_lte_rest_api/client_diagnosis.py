from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/diagnosis/trace_route_result', methods=['GET'])
def get_client_diagnosis_trace_route_result():
    data = huawei_lte_rest_api.globals.client.diagnosis.trace_route_result()
    return json.dumps(data)

@api.route('/client/diagnosis/diagnose_ping', methods=['GET'])
def get_client_diagnosis_diagnose_ping():
    data = huawei_lte_rest_api.globals.client.diagnosis.diagnose_ping()
    return json.dumps(data)

@api.route('/client/diagnosis/diagnose_traceroute', methods=['GET'])
def get_client_diagnosis_diagnose_traceroute():
    data = huawei_lte_rest_api.globals.client.diagnosis.diagnose_traceroute()
    return json.dumps(data)

@api.route('/client/diagnosis/time_reboot', methods=['GET'])
def get_client_diagnosis_time_reboot():
    data = huawei_lte_rest_api.globals.client.diagnosis.time_reboot()
    return json.dumps(data)

