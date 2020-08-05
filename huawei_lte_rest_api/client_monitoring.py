from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/monitoring/converged_status', methods=['GET'])
def get_client_monitoring_converged_status():
    data = huawei_lte_rest_api.globals.client.monitoring.converged_status()
    return json.dumps(data)

@api.route('/client/monitoring/status', methods=['GET'])
def get_client_monitoring_status():
    data = huawei_lte_rest_api.globals.client.monitoring.status()
    return json.dumps(data)

@api.route('/client/monitoring/check_notifications', methods=['GET'])
def get_client_monitoring_check_notifications():
    data = huawei_lte_rest_api.globals.client.monitoring.check_notifications()
    return json.dumps(data)

@api.route('/client/monitoring/traffic_statistics', methods=['GET'])
def get_client_monitoring_traffic_statistics():
    data = huawei_lte_rest_api.globals.client.monitoring.traffic_statistics()
    return json.dumps(data)

@api.route('/client/monitoring/start_date', methods=['GET'])
def get_client_monitoring_start_date():
    data = huawei_lte_rest_api.globals.client.monitoring.start_date()
    return json.dumps(data)

@api.route('/client/monitoring/start_date_wlan', methods=['GET'])
def get_client_monitoring_start_date_wlan():
    data = huawei_lte_rest_api.globals.client.monitoring.start_date_wlan()
    return json.dumps(data)

@api.route('/client/monitoring/month_statistics', methods=['GET'])
def get_client_monitoring_month_statistics():
    data = huawei_lte_rest_api.globals.client.monitoring.month_statistics()
    return json.dumps(data)

@api.route('/client/monitoring/month_statistics_wlan', methods=['GET'])
def get_client_monitoring_month_statistics_wlan():
    data = huawei_lte_rest_api.globals.client.monitoring.month_statistics_wlan()
    return json.dumps(data)

@api.route('/client/monitoring/wifi_month_setting', methods=['GET'])
def get_client_monitoring_wifi_month_setting():
    data = huawei_lte_rest_api.globals.client.monitoring.wifi_month_setting()
    return json.dumps(data)
