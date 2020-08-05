from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/config_device_information/config', methods=['GET'])
def get_client_config_device_information_config():
    data = huawei_lte_rest_api.globals.client.config_device_information.config()
    return json.dumps(data)

@api.route('/client/config_dialup/config', methods=['GET'])
def get_client_config_dialup_config():
    data = huawei_lte_rest_api.globals.client.config_dialup.config()
    return json.dumps(data)

@api.route('/client/config_dialup/connectmode', methods=['GET'])
def get_client_config_dialup_connectmode():
    data = huawei_lte_rest_api.globals.client.config_dialup.connectmode()
    return json.dumps(data)

@api.route('/client/config_dialup/profileswitch', methods=['GET'])
def get_client_config_dialup_profileswitch():
    data = huawei_lte_rest_api.globals.client.config_dialup.profileswitch()
    return json.dumps(data)

@api.route('/client/config_dialup/lmt_auto_mode_disconnect', methods=['GET'])
def get_client_config_dialup_lmt_auto_mode_disconnect():
    data = huawei_lte_rest_api.globals.client.config_dialup.lmt_auto_mode_disconnect()
    return json.dumps(data)

@api.route('/client/config_global/languagelist', methods=['GET'])
def get_client_config_global_languagelist():
    data = huawei_lte_rest_api.globals.client.config_global.languagelist()
    return json.dumps(data)

@api.route('/client/config_global/config', methods=['GET'])
def get_client_config_global_config():
    data = huawei_lte_rest_api.globals.client.config_global.config()
    return json.dumps(data)

@api.route('/client/config_global/net_type', methods=['GET'])
def get_client_config_global_net_type():
    data = huawei_lte_rest_api.globals.client.config_global.net_type()
    return json.dumps(data)

@api.route('/client/config_lan/config', methods=['GET'])
def get_client_config_lan_config():
    data = huawei_lte_rest_api.globals.client.config_lan.config()
    return json.dumps(data)

@api.route('/client/config_network/config', methods=['GET'])
def get_client_config_network_config():
    data = huawei_lte_rest_api.globals.client.config_network.config()
    return json.dumps(data)

@api.route('/client/config_network/net_mode', methods=['GET'])
def get_client_config_network_net_mode():
    data = huawei_lte_rest_api.globals.client.config_network.net_mode()
    return json.dumps(data)

@api.route('/client/config_network/networkmode', methods=['GET'])
def get_client_config_network_networkmode():
    data = huawei_lte_rest_api.globals.client.config_network.networkmode()
    return json.dumps(data)

@api.route('/client/config_network/networkband_null', methods=['GET'])
def get_client_config_network_networkband_null():
    data = huawei_lte_rest_api.globals.client.config_network.networkband_null()
    return json.dumps(data)

@api.route('/client/config_pc_assistant/config', methods=['GET'])
def get_client_config_pc_assistant_config():
    data = huawei_lte_rest_api.globals.client.config_pc_assistant.config()
    return json.dumps(data)

@api.route('/client/config_pc_assistant/updateautorun', methods=['GET'])
def get_client_config_pc_assistant_updateautorun():
    data = huawei_lte_rest_api.globals.client.config_pc_assistant.updateautorun()
    return json.dumps(data)

@api.route('/client/config_pincode/config', methods=['GET'])
def get_client_config_pincode_config():
    data = huawei_lte_rest_api.globals.client.config_pincode.config()
    return json.dumps(data)

@api.route('/client/config_sms/config', methods=['GET'])
def get_client_config_sms_config():
    data = huawei_lte_rest_api.globals.client.config_sms.config()
    return json.dumps(data)

@api.route('/client/config_voice/config', methods=['GET'])
def get_client_config_voice_config():
    data = huawei_lte_rest_api.globals.client.config_voice.config()
    return json.dumps(data)

@api.route('/client/config_web_ui_cfg/config', methods=['GET'])
def get_client_config_web_ui_cfg_config():
    data = huawei_lte_rest_api.globals.client.config_web_ui_cfg.config()
    return json.dumps(data)

@api.route('/client/config_wifi/configure', methods=['GET'])
def get_client_config_wifi_configure():
    data = huawei_lte_rest_api.globals.client.config_wifi.configure()
    return json.dumps(data)

@api.route('/client/config_wifi/country_channel', methods=['GET'])
def get_client_config_wifi_country_channel():
    data = huawei_lte_rest_api.globals.client.config_wifi.country_channel()
    return json.dumps(data)

@api.route('/client/config_wifi/channel_auto_match_hardware', methods=['GET'])
def get_client_config_wifi_channel_auto_match_hardware():
    data = huawei_lte_rest_api.globals.client.config_wifi.channel_auto_match_hardware()
    return json.dumps(data)

@api.route('/client/config_device/config', methods=['GET'])
def get_client_config_device_config():
    data = huawei_lte_rest_api.globals.client.config_device.config()
    return json.dumps(data)

@api.route('/client/config_fast_boot/config', methods=['GET'])
def get_client_config_fast_boot_config():
    data = huawei_lte_rest_api.globals.client.config_fast_boot.config()
    return json.dumps(data)

@api.route('/client/config_firewall/config', methods=['GET'])
def get_client_config_firewall_config():
    data = huawei_lte_rest_api.globals.client.config_firewall.config()
    return json.dumps(data)

@api.route('/client/config_ipv6/config', methods=['GET'])
def get_client_config_ipv6_config():
    data = huawei_lte_rest_api.globals.client.config_ipv6.config()
    return json.dumps(data)

@api.route('/client/config_ota/config', methods=['GET'])
def get_client_config_ota_config():
    data = huawei_lte_rest_api.globals.client.config_ota.config()
    return json.dumps(data)

@api.route('/client/config_pb/config', methods=['GET'])
def get_client_config_pb_config():
    data = huawei_lte_rest_api.globals.client.config_pb.config()
    return json.dumps(data)

@api.route('/client/config_sntp/config', methods=['GET'])
def get_client_config_sntp_config():
    data = huawei_lte_rest_api.globals.client.config_sntp.config()
    return json.dumps(data)

@api.route('/client/config_stk/config', methods=['GET'])
def get_client_config_stk_config():
    data = huawei_lte_rest_api.globals.client.config_stk.config()
    return json.dumps(data)

@api.route('/client/config_update/config', methods=['GET'])
def get_client_config_update_config():
    data = huawei_lte_rest_api.globals.client.config_update.config()
    return json.dumps(data)

@api.route('/client/config_u_pnp/config', methods=['GET'])
def get_client_config_u_pnp_config():
    data = huawei_lte_rest_api.globals.client.config_u_pnp.config()
    return json.dumps(data)

@api.route('/client/config_ussd/prepaidussd', methods=['GET'])
def get_client_config_ussd_prepaidussd():
    data = huawei_lte_rest_api.globals.client.config_ussd.prepaidussd()
    return json.dumps(data)

@api.route('/client/config_ussd/postpaidussd', methods=['GET'])
def get_client_config_ussd_postpaidussd():
    data = huawei_lte_rest_api.globals.client.config_ussd.postpaidussd()
    return json.dumps(data)

@api.route('/client/config_web_sd/config', methods=['GET'])
def get_client_config_web_sd_config():
    data = huawei_lte_rest_api.globals.client.config_web_sd.config()
    return json.dumps(data)
