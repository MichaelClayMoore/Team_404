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
