#!/usr/bin/python3

from huawei_lte_api.Client import Client
from huawei_lte_api.AuthorizedConnection import AuthorizedConnection
from huawei_lte_api.exceptions import ResponseErrorLoginCsfrException
import time
from math_bands import *
from flask import Flask, json, request
from flask_cors import CORS
import datetime

api = Flask(__name__)
CORS(api)

connection = None
client = None
ip = ""
user = ""
password = ""
LOGOUT_TIMEOUT = 30  # seconds
login_time = None
logged_in = False

def get_int(value):
    return int(float(value.split('d')[0]))

def human_readable_size(size, decimal_places):
    for unit in ['bps','Kbps','Mbps','Gbps','Tbps']:
        if size < 1000.0:
            if unit == 'bps':
                decimal_places = 0
            break
        size /= 1000.0
    return f"{size:.{decimal_places}f}{unit}"

def login():
    global ip
    global user
    global password
    global connection
    global client
    global login_time
    global logged_in

    try:
        print ("logging in")
        connection = AuthorizedConnection(f'http://{ip}/', user, password)
        client = Client(connection)
        login_time = datetime.datetime.utcnow()
        logged_in = True

        print ("logging in - success")
        print (login_time)
        return json.dumps({"status": "ok"})

    except Exception as error:
        errorMsg = error.args
        if errorMsg[0] == "108003: Already login":
            print("already logged in")
            login_time = datetime.datetime.utcnow()
            logged_in = True
            return json.dumps({"status": "ok"})
        else:
            print ("logging in - error")
            print(errorMsg[0])
            logged_in = False
            return json.dumps({"status": errorMsg[0]})

@api.route('/login', methods=['POST'])
def post_login():
    global ip
    global user
    global password

    req_data = request.get_json()
    ip = req_data['ip']
    user = req_data['username']
    password = req_data['password']

    return login()

@api.route('/signal', methods=['GET'])
def get_signal():
    global logged_in
    global login_time
    global LOGOUT_TIMEOUT
    global client

    if not logged_in:
        print("not logged in")
        return json.dumps({"status": "Not logged in"})
    else:
        print("logged in - check if we need to login again")
        logout_time = login_time + datetime.timedelta(seconds=LOGOUT_TIMEOUT)
        if logout_time < datetime.datetime.utcnow():
            print("timeout = re-login")
            login()
        else:
            print("still in time window, no need to re-login")

    signal_info = client.device.signal()
    traffic_info = client.monitoring.traffic_statistics()

    return json.dumps({
        "cellId": signal_info['cell_id']
        , "upFreq": signal_info['lteulfreq']
        , "downFreq": signal_info['ltedlfreq']
        , "rsrp": get_int(signal_info['rsrp'])
        , "rsrq": get_int(signal_info['rsrq'])
        , "sinr": get_int(signal_info['sinr'])
        , "band": bands_ui_dict['b' + signal_info['band']]
        , "downRate": human_readable_size(int(traffic_info['CurrentDownloadRate']) * 8, 2)
        , "upRate": human_readable_size(int(traffic_info['CurrentUploadRate']) * 8, 2)
    })

def main():
    api.run()

main()

