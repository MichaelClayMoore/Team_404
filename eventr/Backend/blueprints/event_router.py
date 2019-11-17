##  START File !!
from flask import request, Blueprint, abort , json, jsonify
from events.eventController import eventController
from events.friendsController import friendController
import json

event_controller = eventController()
friends_controller = friendController()
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

@event_router.route("/savefriend_event", methods=['POST'])
def save_friend():
    friend = request.get_json()['params']['friend']
    print('added User')
    return friends_controller.save_friend( friend )

@event_router.route("/addfriend_event", methods=['POST'])
def addfriend_event():
    addFriendProp = request.get_json()['params']['name']
    #print(request.get_json()['params']['name'])
    
    friends_controller.search_friends( addFriendProp )
    return "Success"

@event_router.route("/search_event", methods=['POST'])
def search_event():
    searchProp = request.get_json()['params']['searchProp']
    
    event_controller.search_event( searchProp )

    return "Success"
