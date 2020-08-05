from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/led/nightmode', methods=['GET'])
def get_client_led_nightmode():
    data = huawei_lte_rest_api.globals.client.led.nightmode()
    return json.dumps(data)

