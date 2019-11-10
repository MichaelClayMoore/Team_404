##  START File !!
from flask import request, Blueprint, abort , json, jsonify
import json

event_router = Blueprint('event_router', __name__)

@event_router.route("/get_test", methods=['GET'])
def get_test():
    return "test"

@event_router.route("/save_event", methods=['POST'])
def save_event():
    print(request.get_json()['params']['event'])
    return "test"
