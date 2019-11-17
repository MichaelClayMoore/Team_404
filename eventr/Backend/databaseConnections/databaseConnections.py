from sqlalchemy import create_engine
import yaml, os


settingsFile = 'settings.yaml'

class databaseConnection:

    def __init__(self):
        with open(settingsFile, 'r') as (configStream):
            data = yaml.load(configStream)['postgres']
        connectionString = 'postgresql+psycopg2://' + data['user'] + ':' + data['password'] + '@' + data['host'] + ':' + str(data['port']) + '/' + data['db']
        self.engine = create_engine(connectionString)

    def connectToDb(self):
        connection = self.engine.connect()
        return connection


instance = None

def __new__(cls):
    if not databaseConnection.instance:
        databaseConnection.instance = databaseConnection.__databaseConnection()
    return databaseConnection.instance
