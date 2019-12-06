##  START File !!
from flask import request, Blueprint, abort , json, jsonify
from events.eventController import eventController
from events.userController import userController
import json

event_controller = eventController()
user_controller = userController()

event_router = Blueprint('event_router', __name__)

@event_router.route("/get_test", methods=['GET'])
def get_test():
    return event_controller.test()

@event_router.route("/join_event", methods=['POST'])
def join_event():
    event = request.get_json()['params']['event']
    return event_controller.join_event(event)

@event_router.route("/getName", methods=['POST'])
def getName():
    id = request.get_json()['params']['id']
    return event_controller.getName(id)


@event_router.route("/get_A_List", methods=['POST'])
def getAttendList():
    event = request.get_json()['params']['event']
    return event_controller.get_A_List(event)

@event_router.route("/submit_comment", methods=['POST'])
def submit_comment():
    comment = request.get_json()['params']['comment']
    return event_controller.submit_comment(comment)

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

@event_router.route("/addfriend_event", methods=['POST'])
def addfriend_event():
    print("made it inside of event_router.py ")
    user = request.get_json()['params']['name']
    cUser= request.get_json()['params']['cUser']
    return user_controller.add_friend( user, cUser )

@event_router.route("/search_event", methods=['POST'])
def search_event():
    searchProp = request.get_json()['params']['searchProp']
    event_controller.search_event( searchProp )

    return event_controller.search_event( searchProp )

@event_router.route("/search_my_friends", methods=['POST'])
def search_my_friends():
    friendProp = request.get_json()['params']['friendProp']
    return user_controller.search_friends( friendProp )

@event_router.route("/save_user", methods=['POST'])
def save_user():
    user = request.get_json()['params']['signupProp']
    return user_controller.save_user( user )

@event_router.route("/validate_user", methods=['POST'])
def validate_user():
    user = request.get_json()['params']['loginProp']
    return user_controller.validate_user( user )
#@event_router.route("/_user", methods=['POST'])
#def signup_user():
 #   event = request.get_json()['params']['signupProp']
    # print(event)
  #  return user_controller.save_user( user )
