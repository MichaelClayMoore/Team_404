import json
from Utility.geocodeUtility import geocodeUtility
from .eventDAO import eventDAO

class friendController:
    def __init__(self):
        self.friends = []
        self.geoCoder = geocodeUtility();
        self.eventDAO = eventDAO();
        print(self.test()); 
        print('This is a test of friends controller');

    def test(self):
        return self.eventDAO.testConnection();

    def save_friend(self, friend ):
        try:
            self.friends.append(friend);
            return "Success"
        except:
            return "Failed"

    def return_friends(self):
        return json.dumps( self.friends )

    def geocode_location(self, location):
        latlong = self.geoCoder.getLatLong(location)
        return latlong



    def search_friends(self, searchProp):
        searchedFriends = [] #this is a list that will contain all of the matching users

        #searching through each of the friends in the fake database
        for friend in self.friends:   
            if friend.get('userID2') == searchProp.get('userID'):     #name matching
                searchedFriends.append(friend) 

        if searchedFriends:      #if searchedEvents conatins events return the list, else return no results found
            print("returning found friends")
            for friend2 in searchedFriends:
                print(friend2)
            return searchedFriends
        else:
            print("found no matching friends")
                
                

            
