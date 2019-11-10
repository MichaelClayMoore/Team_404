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
