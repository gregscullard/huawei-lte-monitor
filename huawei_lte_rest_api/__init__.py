#!/usr/bin/python3

from math_bands import *
from flask import Flask, json, request
from flask_cors import CORS
import huawei_lte_rest_api.globals

globals.init()

api = Flask(__name__)
CORS(api)
#
# def get_int(value):
#     return int(float(value.split('d')[0]))
#
# def human_readable_size(size, decimal_places):
#     for unit in ['bps','Kbps','Mbps','Gbps','Tbps']:
#         if size < 1000.0:
#             if unit == 'bps':
#                 decimal_places = 0
#             break
#         size /= 1000.0
#     return f"{size:.{decimal_places}f}{unit}"
#
#
#
#
import huawei_lte_rest_api.client_bluetooth
import huawei_lte_rest_api.client_config
import huawei_lte_rest_api.client_cradle
import huawei_lte_rest_api.client_cwmp
import huawei_lte_rest_api.client_ddns
import huawei_lte_rest_api.client_device
import huawei_lte_rest_api.client_dhcp
import huawei_lte_rest_api.client_diagnosis
import huawei_lte_rest_api.client_dialup
import huawei_lte_rest_api.client_global
import huawei_lte_rest_api.client_lan
import huawei_lte_rest_api.client_language
import huawei_lte_rest_api.client_led
import huawei_lte_rest_api.client_log
import huawei_lte_rest_api.client_mlog
import huawei_lte_rest_api.client_monitoring
import huawei_lte_rest_api.client_net
import huawei_lte_rest_api.client_ntwk
import huawei_lte_rest_api.client_online_update
import huawei_lte_rest_api.client_ota
import huawei_lte_rest_api.client_pb
import huawei_lte_rest_api.client_pin
import huawei_lte_rest_api.client_redirection
import huawei_lte_rest_api.client_sdcard
import huawei_lte_rest_api.client_security
import huawei_lte_rest_api.client_sms
import huawei_lte_rest_api.client_sntp
import huawei_lte_rest_api.client_statistic
import huawei_lte_rest_api.client_syslog
import huawei_lte_rest_api.client_time
import huawei_lte_rest_api.client_timerule
import huawei_lte_rest_api.client_usb_printer
import huawei_lte_rest_api.client_usb_storage
import huawei_lte_rest_api.client_user
import huawei_lte_rest_api.client_usermanual
import huawei_lte_rest_api.client_voice
import huawei_lte_rest_api.client_vpn
import huawei_lte_rest_api.client_vsim
import huawei_lte_rest_api.client_webserver
import huawei_lte_rest_api.client_wlan

# @api.route('/signal', methods=['GET'])
# def get_signal():
#     global logged_in
#     global login_time
#     global LOGOUT_TIMEOUT
#
#     if not logged_in:
#         print("not logged in")
#         return json.dumps({"status": "Not logged in"})
#     else:
#         print("logged in - check if we need to login again")
#         logout_time = login_time + datetime.timedelta(seconds=LOGOUT_TIMEOUT)
#         if logout_time < datetime.datetime.utcnow():
#             print("timeout = re-login")
#             login()
#         else:
#             print("still in time window, no need to re-login")
#
#     signal_info = client.device.signal()
#     traffic_info = client.monitoring.traffic_statistics()
#
#     return json.dumps({
#         "cellId": signal_info['cell_id']
#         , "upFreq": signal_info['lteulfreq']
#         , "downFreq": signal_info['ltedlfreq']
#         , "rsrp": get_int(signal_info['rsrp'])
#         , "rsrq": get_int(signal_info['rsrq'])
#         , "sinr": get_int(signal_info['sinr'])
#         , "band": bands_ui_dict['b' + signal_info['band']]
#         , "downRate": human_readable_size(int(traffic_info['CurrentDownloadRate']) * 8, 2)
#         , "upRate": human_readable_size(int(traffic_info['CurrentUploadRate']) * 8, 2)
#     })
#
# def main():
#     api.run()
#
# main()
#
