from huawei_lte_api.Client import Client
from huawei_lte_api.AuthorizedConnection import AuthorizedConnection
from huawei_lte_rest_api import api
from flask import Flask, json, request
import datetime
import time
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

connection = None
ip = ""
user = ""
password = ""
login_time = None
logged_in = False


def login():
    global ip
    global user
    global password
    global connection
    global login_time
    global logged_in

    try:
        print ("logging in")
        connection = AuthorizedConnection(f'http://{ip}/', user, password)
        print ("setting client")
        huawei_lte_rest_api.globals.client = Client(connection)
        login_time = datetime.datetime.utcnow()
        logged_in = True

        print ("logging in - success")
        print (login_time)
        return json.dumps({"status": "logged in"})

    except Exception as error:
        errorMsg = error.args
        if errorMsg[0] == "108003: Already login":
            print("already logged in")
            login_time = datetime.datetime.utcnow()
            logged_in = True
            return json.dumps({"status": "logged in"})
        else:
            print ("logging in - error")
            print(errorMsg[0])
            logged_in = False
            return json.dumps({"status": errorMsg[0]})


@api.route('/client/user/logout', methods=['GET'])
def get_client_user_logout():
    global connection
    if isinstance(connection, AuthorizedConnection):
        huawei_lte_rest_api.globals.client.user.logout()
        return json.dumps({"status": "logged out"})

@api.route('/client/user/login', methods=['POST'])
def post_login():
    global ip
    global user
    global password

    req_data = request.get_json()
    ip = req_data['ip']
    user = req_data['username']
    password = req_data['password']

    return login()

@api.route('/client/user/state_login', methods=['GET'])
def get_client_user_state_login():
    data = huawei_lte_rest_api.globals.client.user.state_login()
    return json.dumps(data)

@api.route('/client/user/remind', methods=['GET'])
def get_client_user_remind():
    data = huawei_lte_rest_api.globals.client.user.remind()
    return json.dumps(data)

@api.route('/client/user/password', methods=['GET'])
def get_client_user_password():
    data = huawei_lte_rest_api.globals.client.user.password()
    return json.dumps(data)

@api.route('/client/user/pwd', methods=['GET'])
def get_client_user_pwd():
    data = huawei_lte_rest_api.globals.client.user.pwd()
    return json.dumps(data)

@api.route('/client/user/authentication_login', methods=['GET'])
def get_client_user_authentication_login():
    data = huawei_lte_rest_api.globals.client.user.authentication_login()
    return json.dumps(data)

@api.route('/client/user/challenge_login', methods=['GET'])
def get_client_user_challenge_login():
    data = huawei_lte_rest_api.globals.client.user.challenge_login()
    return json.dumps(data)

@api.route('/client/user/hilink_login', methods=['GET'])
def get_client_user_hilink_login():
    data = huawei_lte_rest_api.globals.client.user.hilink_login()
    return json.dumps(data)

@api.route('/client/user/history_login', methods=['GET'])
def get_client_user_history_login():
    data = huawei_lte_rest_api.globals.client.user.history_login()
    return json.dumps(data)

@api.route('/client/user/heartbeat', methods=['GET'])
def get_client_user_heartbeat():
    data = huawei_lte_rest_api.globals.client.user.heartbeat()
    return json.dumps(data)

@api.route('/client/user/web_feature_switch', methods=['GET'])
def get_client_user_web_feature_switch():
    data = huawei_lte_rest_api.globals.client.user.web_feature_switch()
    return json.dumps(data)

@api.route('/client/user/screen_state', methods=['GET'])
def get_client_user_screen_state():
    data = huawei_lte_rest_api.globals.client.user.screen_state()
    return json.dumps(data)

@api.route('/client/user/session', methods=['GET'])
def get_client_user_session():
    data = huawei_lte_rest_api.globals.client.user.session()
    return json.dumps(data)
