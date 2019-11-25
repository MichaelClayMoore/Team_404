import json
from .userDAO import userDAO

class userController:
    def __init__(self):
        self.userDAO = userDAO();

    def test(self):
        return self.userDAO.testConnection()

    def save_event(self, user):
        try:
            event['location']['latitude'] = latlong['latitude']
            event['location']['longitude'] = latlong['longitude']
            addEventToDatabase = self.eventDAO.addEvent(event);
            if addEventToDatabase:
                event['id'] = addEventToDatabase
            return json.dumps(event)
            return json.dumps(False)
        except:
            return json.dumps(False)