import json

class eventController:
    def __init__(self):
        self.events = []

    def test(self):
        return "test"

    def save_event(self, event ):
        try:
            self.events.append(event)
            return "Success"
        except:
            return "Failed"

    def return_events(self):
        return json.dumps( self.events )

    def search_event(self):
        return "this works"