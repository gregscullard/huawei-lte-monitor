from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/v_sim/operateswitch_vsim', methods=['GET'])
def get_client_v_sim_operateswitch_vsim():
    data = huawei_lte_rest_api.globals.client.v_sim.operateswitch_vsim()
    return json.dumps(data)
