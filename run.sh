#!/bin/sh
pip3 install flask
export FLASK_APP=huawei_lte_rest_api
pip3 install -e .
python3 -m flask run

