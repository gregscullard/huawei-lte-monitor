from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/wlan/wifi_feature_switch', methods=['GET'])
def get_client_wifi_wifi_feature_switch():
    data = huawei_lte_rest_api.globals.client.wifi.wifi_feature_switch()
    return json.dumps(data)

@api.route('/client/wlan/station_information', methods=['GET'])
def get_client_wifi_station_information():
    data = huawei_lte_rest_api.globals.client.wifi.station_information()
    return json.dumps(data)

@api.route('/client/wlan/basic_settings', methods=['GET'])
def get_client_wifi_basic_settings():
    data = huawei_lte_rest_api.globals.client.wifi.basic_settings()
    return json.dumps(data)

@api.route('/client/wlan/security_settings', methods=['GET'])
def get_client_wifi_wifi_security_settings():
    data = huawei_lte_rest_api.globals.client.wifi.security_settings()
    return json.dumps(data)

@api.route('/client/wlan/multi_security_settings', methods=['GET'])
def get_client_wifi_multi_security_settings():
    data = huawei_lte_rest_api.globals.client.wifi.multi_security_settings()
    return json.dumps(data)

@api.route('/client/wlan/multi_security_settings_ex', methods=['GET'])
def get_client_wifi_multi_security_settings_ex():
    data = huawei_lte_rest_api.globals.client.wifi.multi_security_settings_ex()
    return json.dumps(data)

@api.route('/client/wlan/multi_basic_settings', methods=['GET'])
def get_client_wifi_multi_basic_settings():
    data = huawei_lte_rest_api.globals.client.wifi.multi_basic_settings()
    return json.dumps(data)

@api.route('/client/wlan/host_list', methods=['GET'])
def get_client_wifi_wifi_host_list():
    data = huawei_lte_rest_api.globals.client.wifi.host_list()
    return json.dumps(data)

@api.route('/client/wlan/handover_setting', methods=['GET'])
def get_client_wifi_handover_setting():
    data = huawei_lte_rest_api.globals.client.wifi.handover_setting()
    return json.dumps(data)

@api.route('/client/wlan/multi_switch_settings', methods=['GET'])
def get_client_wifi_multi_switch_settings():
    data = huawei_lte_rest_api.globals.client.wifi.multi_switch_settings()
    return json.dumps(data)

@api.route('/client/wlan/multi_macfilter_settings', methods=['GET'])
def get_client_wifi_multi_macfilter_settings():
    data = huawei_lte_rest_api.globals.client.wifi.multi_macfilter_settings()
    return json.dumps(data)

@api.route('/client/wlan/multi_macfilter_settings_ex', methods=['GET'])
def get_client_wifi_multi_macfilter_settings_ex():
    data = huawei_lte_rest_api.globals.client.wifi.multi_macfilter_settings_ex()
    return json.dumps(data)

@api.route('/client/wlan/mac_filter', methods=['GET'])
def get_client_wifi_mac_filter():
    data = huawei_lte_rest_api.globals.client.wifi.mac_filter()
    return json.dumps(data)

@api.route('/client/wlan/oled_showpassword', methods=['GET'])
def get_client_wifi_oled_showpassword():
    data = huawei_lte_rest_api.globals.client.wifi.oled_showpassword()
    return json.dumps(data)

@api.route('/client/wlan/wps', methods=['GET'])
def get_client_wifi_wps():
    data = huawei_lte_rest_api.globals.client.wifi.wps()
    return json.dumps(data)

@api.route('/client/wlan/wps_appin', methods=['GET'])
def get_client_wifi_wps_appin():
    data = huawei_lte_rest_api.globals.client.wifi.wps_appin()
    return json.dumps(data)

@api.route('/client/wlan/wps_pbc', methods=['GET'])
def get_client_wifi_wps_pbc():
    data = huawei_lte_rest_api.globals.client.wifi.wps_pbc()
    return json.dumps(data)

@api.route('/client/wps_switch', methods=['GET'])
def get_client_wifi_wps_switch():
    data = huawei_lte_rest_api.globals.client.wifi.wps_switch()
    return json.dumps(data)

@api.route('/client/wlan/status_switch_settings', methods=['GET'])
def get_client_wifi_status_switch_settings():
    data = huawei_lte_rest_api.globals.client.wifi.status_switch_settings()
    return json.dumps(data)

@api.route('/client/wlan/wifiprofile', methods=['GET'])
def get_client_wifi_wifiprofile():
    data = huawei_lte_rest_api.globals.client.wifi.wifiprofile()
    return json.dumps(data)

@api.route('/client/wlan/wififrequence', methods=['GET'])
def get_client_wifi_wififrequence():
    data = huawei_lte_rest_api.globals.client.wifi.wififrequence()
    return json.dumps(data)

@api.route('/client/wlan/wifiscanresult', methods=['GET'])
def get_client_wifi_wifiscanresult():
    data = huawei_lte_rest_api.globals.client.wifi.wifiscanresult()
    return json.dumps(data)
