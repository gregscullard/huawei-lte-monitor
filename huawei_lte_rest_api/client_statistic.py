from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/statistic/feature_roam_statistic', methods=['GET'])
def get_client_statistic_feature_roam_statistic():
    data = huawei_lte_rest_api.globals.client.statistic.feature_roam_statistic()
    return json.dumps(data)

