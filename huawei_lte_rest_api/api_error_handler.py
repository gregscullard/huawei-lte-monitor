from huawei_lte_rest_api import api
from flask import json

@api.errorhandler(Exception)
def handle_error(e):
    errorMsg = e.args
    return json.dumps({"status": errorMsg[0]})
