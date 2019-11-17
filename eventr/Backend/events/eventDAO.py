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
        query += "ST_SETSRID(ST_MAKEPOINT(" + str(event['location']['latitude']).lower() + "," + str(event['location']['longitude']).lower() + "), 4269), '" + str(event['date']).lower() + "','"
        query += str(event['creator']).lower() + "','" + str(event['style']).lower() + "','" +  str(event['description']).lower() + "'," + str(event['rsvp']).lower() + ");"

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
