from databaseConnections import databaseConnections
import psycopg2, psycopg2.extras, json
from datetime import datetime

class eventDAO:

    def __init__(self):
        try:
            self.connection = databaseConnections.databaseConnection()
        except psycopg2.Error as error:
            try:
                print(error.pgerror)
                print("Couldn't connect to the database")
            finally:
                error = None
                del error

    def testConnection(self):
        if self.connection:
            return json.dumps(True)
        else:
            return json.dumps(False)

    def addEvent(self, event):
        conn = self.connection.connectToDb()
        trans = conn.begin()
        cursor = conn.connection.cursor()
        query = "INSERT into events(name, address1, address2, city, state, zip, latitude, longitude, geom, date, host, style, description, rsvp) VALUES('"
        query += str(event['name']) + "','" + str(event['location']['address1']).lower() + "', '"
        query += str(event['location']['address2']).lower() + "', '" + str(event['location']['city']).lower() + "','"
        query += str(event['location']['state']) + "','" + str(event['location']['zip']).lower() + "', "
        query += str(event['location']['latitude']).lower() + ", " + str(event['location']['longitude']).lower() + ","
        query += "ST_SETSRID(ST_MAKEPOINT(" + str(event['location']['latitude']).lower() + "," + str(event['location']['longitude']).lower() + "), 4269), "
        query += "to_date('" + str(event['date']).lower() + "','YYYY-MM-DD'), "
        query += str(event['creator']).lower() + ",'" + str(event['style']).lower() + "','" +  str(event['description']).lower() + "'," + str(event['rsvp']).lower() + ");"

        print('\nquery is: ', query, '\n')
        try:
            cursor.execute(query)
            trans.commit()
            query = "SELECT MAX(id) from events;"

            try:
                cursor.execute(query)
                row = cursor.fetchone()
                return row[0] if row else None

            except psycopg2.Error as error:
                trans.rollback()
                print(error.pgerror)
                return False

            trans.commit()
            cursor.close()

        except psycopg2.Error as error:
            trans.rollback()
            print(error.pgerror)
            return False

        finally:
            conn.close()

    def joinEvent(self, event):
        conn = self.connection.connectToDb()
        trans = conn.begin()
        cursor = conn.connection.cursor()
        """
        This Will get append ints to the list 

            update events
            set attendees[cardinality(attendees)] = userID
            where id = eventID;

        #superior version:
            update events
            set attendees = attendees || 7
            where (id = 3) and (not attendees @> ARRAY[7]);
        """
        print(event)
        print( type(event))
        query = "UPDATE events set attendees = attendees || " + str(event['user']) + " WHERE (id = " +str(event['eventId'])+ ") and (not attendees @> ARRAY[ " +str(event['user']) +"]);"
        
        try:
            cursor.execute(query)
            trans.commit()
            cursor.close()
            return True
        except psycopg2.Error as error:
            trans.rollback()
            print(error.pgerror)
            return False
        finally:
            conn.close()

    def removeEvent(self, eventId):
        conn = self.connection.connectToDb()
        trans = conn.begin()
        cursor = conn.connection.cursor()
        query = "DELETE FROM events where id = " + str(eventId) + ";"
        print('\nquery is: ', query, '\n')
        try:
            cursor.execute(query)
            trans.commit()
            cursor.close()
            return True


        except psycopg2.Error as error:
            trans.rollback()
            print(error.pgerror)
            return False

        finally:
            conn.close()

    def getEvents(self):
        conn = self.connection.connectToDb()
        trans = conn.begin()
        cursor = conn.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "SELECT name, address1, address2, city, state, zip, latitude, longitude, date, host, style, description, rsvp, attendees, id from events;"
        print('\nquery is: ', query, '\n')
        try:
            cursor.execute(query)
            eventsGiven = cursor.fetchall()
            print("events: ", eventsGiven)
            events = []
            for event in eventsGiven:
                temp = {'name':event[0], 'location': {'address1':event[1], 'address2':event[2], 'city':event[3], 'state':event[4], 'zip':event[5], 'latitude':event[6], 'longitude':event[7]}, 'date': event[8], 'creator':event[9], 'style':event[10], 'description': event[11], 'rsvp':event[12],'attendees':event[13], 'id':event[14]};
                events.append(temp)
            print(eventsGiven)
            print(events)
            trans.commit()
            cursor.close()
            return events


        except psycopg2.Error as error:
            trans.rollback()
            print(error.pgerror)
            return []

        finally:
            conn.close()
