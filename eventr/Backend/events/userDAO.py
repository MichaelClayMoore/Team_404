from databaseConnections import databaseConnections
import psycopg2, psycopg2.extras, json
from datetime import datetime

class userDAO:

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

    def addUser(self, user):
        conn = self.connection.connectToDb()
        trans = conn.begin()
        cursor = conn.connection.cursor()
        query = "INSERT into users(username,email,password) VALUES('"
        query += str(user['userinfo']['username']) + "','" + str(user['userinfo']['email']) + "', "
        query += "crypt( '" + str(user['userinfo']['password']) + "', gen_salt('md5') ) );"

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

    def removeUser(self, userId):
        conn = self.connection.connectToDb()
        trans = conn.begin()
        cursor = conn.connection.cursor()
        query = "DELETE FROM users where id = " + str(userId) + ";"
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

    def getUserByUsername(self, user):
        conn = self.connection.connectToDb()
        trans = conn.begin()
        cursor = conn.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "SELECT id\nFROM users\nWHERE username = '"
        query += str(user['userID']) + "';"
        print('\nquery is: ', query, '\n')
        try:
            cursor.execute(query)
            user = cursor.fetchone()
            print("user: ", user)
            trans.commit()
            cursor.close()
            return user if user else False


        except psycopg2.Error as error:
            trans.rollback()
            print(error.pgerror)
            return False

        finally:
            conn.close()

    def getUser(self, user):
        conn = self.connection.connectToDb()
        trans = conn.begin()
        cursor = conn.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "SELECT id\nFROM users\nWHERE username = '"
        query += str(user['username']) + "' AND password = crypt('"
        query += str(user['password']) + "',  password);"
        print('\nquery is: ', query, '\n')
        try:
            cursor.execute(query)
            user = cursor.fetchone()
            print("user: ", user)
            trans.commit()
            cursor.close()
            return user if user else False


        except psycopg2.Error as error:
            trans.rollback()
            print(error.pgerror)
            return False

        finally:
            conn.close()
