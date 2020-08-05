from huawei_lte_rest_api import api
from flask import Flask, json, request
import huawei_lte_rest_api.globals
import huawei_lte_rest_api.api_error_handler

@api.route('/client/voice/featureswitch', methods=['GET'])
def get_client_voice_featureswitch():
    data = huawei_lte_rest_api.globals.client.voice.featureswitch()
    return json.dumps(data)

@api.route('/client/voice/sipaccount', methods=['GET'])
def get_client_voice_sipaccount():
    data = huawei_lte_rest_api.globals.client.voice.sipaccount()
    return json.dumps(data)

@api.route('/client/voice/sipadvance', methods=['GET'])
def get_client_voice_sipadvance():
    data = huawei_lte_rest_api.globals.client.voice.sipadvance()
    return json.dumps(data)

@api.route('/client/voice/sipserver', methods=['GET'])
def get_client_voice_sipserver():
    data = huawei_lte_rest_api.globals.client.voice.sipserver()
    return json.dumps(data)

@api.route('/client/voice/speeddial', methods=['GET'])
def get_client_voice_speeddial():
    data = huawei_lte_rest_api.globals.client.voice.speeddial()
    return json.dumps(data)

@api.route('/client/voice/functioncode', methods=['GET'])
def get_client_voice_functioncode():
    data = huawei_lte_rest_api.globals.client.voice.functioncode()
    return json.dumps(data)

@api.route('/client/voice/voiceadvance', methods=['GET'])
def get_client_voice_voiceadvance():
    data = huawei_lte_rest_api.globals.client.voice.voiceadvance()
    return json.dumps(data)

@api.route('/client/voice/codec', methods=['GET'])
def get_client_voice_codec():
    data = huawei_lte_rest_api.globals.client.voice.codec()
    return json.dumps(data)

@api.route('/client/voice/voicebusy', methods=['GET'])
def get_client_voice_voicebusy():
    data = huawei_lte_rest_api.globals.client.voice.voicebusy()
    return json.dumps(data)
