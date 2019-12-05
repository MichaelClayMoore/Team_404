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

    def add_friend(self, user, cUser):
        """
        update users
        set friends = friends || 3
        where (id = 1) and (not friends @> ARRAY[()]);

        
        """

        #user 1 adds user2
        conn = self.connection.connectToDb()
        trans = conn.begin()
        cursor = conn.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "update users set friends = friends || (SELECT id FROM users WHERE username = '"
        query += str(user['userID']) + "') where (id = "
        query += str(cUser) + " and (not friends @> ARRAY[(SELECT id FROM users WHERE username ='" + str(user['userID']) +"')]));"

        #user2 adds user1
        query2 = "update users set friends = friends || ( "
        query2 += str(cUser) + ") where (id = (SELECT id FROM users WHERE username ='" + str(user['userID'])
        query2 += "') and (not friends @> ARRAY[" + str(cUser) +"]));"
        print('\naddfriendprop is: ', user, '\n')
        print('\ncUser is: ', query, '\n')
        try:
            cursor.execute(query)
            cursor.execute(query2)
            print("UGHHHHH")
            trans.commit()
            cursor.close()
            return True


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
