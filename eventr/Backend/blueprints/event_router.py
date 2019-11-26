##  START File !!
from flask import request, Blueprint, abort , json, jsonify
from events.eventController import eventController
from users.userController import userController
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

@event_router.route("/delete_event", methods=['POST'])
def delete_event():
    event = request.get_json()['params']['eventId']
    return event_controller.removeEvent( event )

@event_router.route("/get_events", methods=['GET'])
def get_events():
    return json.dumps( event_controller.getEvents() )

@event_router.route("/search_event", methods=['POST'])
def search_event():
    searchProp = request.get_json()['params']['searchProp']
    event_controller.search_event( searchProp )

    return event_controller.search_event( searchProp )

@event_router.route("/save_user", methods=['POST'])
def save_user():
    event = request.get_json()['params']['signupProp']
    # print(event)
    return user_controller.save_user( user )