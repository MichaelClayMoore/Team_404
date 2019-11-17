##  START File !!
from flask import request, Blueprint, abort , json, jsonify
from events.eventController import eventController
import json

event_controller = eventController()
event_router = Blueprint('event_router', __name__)

@event_router.route("/get_test", methods=['GET'])
def get_test():
    return event_controller.test()

@event_router.route("/save_event", methods=['POST'])
def save_event():
    event = request.get_json()['params']['event']
    # print(event)
    return event_controller.save_event( event )

@event_router.route("/get_events", methods=['GET'])
def get_events():
    return event_controller.return_events()
    print(request.get_json()['params']['event'])
    return "Success"

<<<<<<< HEAD
@event_router.route("/addfriend_event", methods=['POST'])
def addfriend_event():
    print(request.get_json()['name'])
=======
@event_router.route("/search_event", methods=['POST'])
def search_event():
    searchProp = request.get_json()['params']['searchProp']
    
    event_controller.search_event( searchProp )

>>>>>>> ab07f88b96b8a10e057c38d5ee92b18d1fc849d7
    return "Success"
