from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/usb_printer/printerlist', methods=['GET'])
def get_client_usb_printer_printerlist():
    data = huawei_lte_rest_api.globals.client.usb_printer.printerlist()
    return json.dumps(data)
