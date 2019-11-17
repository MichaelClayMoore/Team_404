import json
from Utility.geocodeUtility import geocodeUtility

class eventController:
    def __init__(self):
        self.events = []
        self.geoCoder = geocodeUtility();

    def test(self):
        return "test"

    def save_event(self, event ):
        try:
            latlong = self.geocode_location(event['location'])
            event['location']['latitude'] = latlong['latitude']
            event['location']['longitude'] = latlong['longitude']
            self.events.append(event);
            return "Success"
        except:
            return "Failed"

    def return_events(self):
        return json.dumps( self.events )
        
    def geocode_location(self, location):
        latlong = self.geoCoder.getLatLong(location)
        return latlong



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
            return searchedEvents
        else:
            print("found no matching events")
            
