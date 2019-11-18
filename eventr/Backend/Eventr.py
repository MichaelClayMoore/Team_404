##  START File !!
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_cors import CORS
from blueprints.event_router import event_router
from events.eventController import eventController

app = Flask(__name__)
CORS(app)

app.register_blueprint(event_router)

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)
