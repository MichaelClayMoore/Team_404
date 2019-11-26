import json
from .userDAO import userDAO

class userController:
    def __init__(self):
        self.userDAO = userDAO();

    def test(self):
        return self.userDAO.testConnection()

    def save_user(self, user):
        try
            addUserToDatabase = self.userDAO.addUser(user);
            if addUserToDatabase:
                user['id'] = addUserToDatabase
            return json.dumps(user)
            return json.dumps(False)
        except:
            return json.dumps(False)