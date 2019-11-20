import json
from Utility.geocodeUtility import geocodeUtility
from .eventDAO import eventDAO

class eventController:
    def __init__(self):
        self.events = []
        self.geoCoder = geocodeUtility();
        self.eventDAO = eventDAO();

    def test(self):
        return self.eventDAO.testConnection();

    def save_event(self, event ):
        self.events.append(event)       #need this so that way my search events still works with the local event list (beacuse I dont have DB fully set up the try doesn't go through)
        try:
            latlong = self.geocode_location(event['location'])
            if latlong:
                event['location']['latitude'] = latlong['latitude']
                event['location']['longitude'] = latlong['longitude']
                addEventToDatabase = self.eventDAO.addEvent(event);
                if addEventToDatabase:
                    event['id'] = addEventToDatabase
                    self.events.append(event);
                return json.dumps(event)
            else:
                return json.dumps(False)
        except:
            return json.dumps(False)

    def removeEvent( self, eventId ):
        return json.dumps( self.eventDAO.removeEvent(eventId) );

    def return_events(self):
        return json.dumps( self.events )

    def geocode_location(self, location):
        latlong = self.geoCoder.getLatLong(location)
        return latlong

    def getEvents(self):
        self.events = self.eventDAO.getEvents();
        for event in self.events:
            event['date'] = event['date'].strftime("%m-%d-%Y")
        return json.dumps( self.events )

    def search_event(self, searchProp):
        searchedEvents = []

        #searching through each of the events
        for event in self.events:
            if searchProp.get('name') == "" or event.get('name') == searchProp.get('name'):     #name matching
                if searchProp.get('creator') == "" or event.get('creator') == searchProp.get('creator'):    #creator matching
                    if not len(searchProp.get('style')) == 0:     #checking if there is a style of event array to search with
                        for style in searchProp.get('style'):
                            if style == event.get('style'):
                                searchedEvents.append(event)
                    else:    #the style list is empty
                        searchedEvents.append(event)

        if searchedEvents:      #if searchedEvents conatins events return the list, else return no results found
            print("returning found events")
            for event2 in searchedEvents:
                print(event2)

            return json.dumps(searchedEvents)
        else:
            print("found no matching events")
