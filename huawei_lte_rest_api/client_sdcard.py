from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/sd_card/dlna_setting', methods=['GET'])
def get_client_sd_card_dlna_setting():
    data = huawei_lte_rest_api.globals.client.sd_card.dlna_setting()
    return json.dumps(data)

@api.route('/client/sd_card/sdcard', methods=['GET'])
def get_client_sd_card_sdcard():
    data = huawei_lte_rest_api.globals.client.sd_card.sdcard()
    return json.dumps(data)

@api.route('/client/sd_card/sdcardsamba', methods=['GET'])
def get_client_sd_card_sdcardsamba():
    data = huawei_lte_rest_api.globals.client.sd_card.sdcardsamba()
    return json.dumps(data)

@api.route('/client/sd_card/printerlist', methods=['GET'])
def get_client_sd_card_printerlist():
    data = huawei_lte_rest_api.globals.client.sd_card.printerlist()
    return json.dumps(data)

@api.route('/client/sd_card/share_account', methods=['GET'])
def get_client_sd_card_share_account():
    data = huawei_lte_rest_api.globals.client.sd_card.share_account()
    return json.dumps(data)

