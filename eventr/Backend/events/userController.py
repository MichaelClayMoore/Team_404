import json
from .userDAO import userDAO

class userController():
    def __init__(self):
        self.userDAO = userDAO()

    def test(self):
        return self.userDAO.testConnection()

    def save_user(self, user):
        try:
            addUserToDatabase = self.userDAO.addUser(user)
            if addUserToDatabase:
                user['id'] = addUserToDatabase
                return json.dumps( user )
            else:
                return json.dumps(False)
        except:
            print("returning error")
            return json.dumps(False)

    def validate_user( self, user ):
        valid = self.userDAO.getUser( user )
        return json.dumps(valid)

    def add_friend( self, user, cUser ):
        
        found = self.userDAO.add_friend( user, cUser )
        return json.dumps( found )

    def convertId2Name(self, id):
        username = self.userDAO.getUsername( id )
        
        return username

    def search_friends(self, friendProp):
        friends = self.userDAO.getFriends( friendProp )
        searchedFriends = []    
        for friend in friends:
            for fr in friend:
                username = self.userDAO.getUsername( fr )
                print('\nfriend within search_friend is: ', fr)
                print("username within search_friends:", username)  

                searchedFriends.append( username )
    
        
        print('\nsearchedFriends within search_friend is: ', searchedFriends)     
        return json.dumps(searchedFriends)

    def nothing( self ):
        return True