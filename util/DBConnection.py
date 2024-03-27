import pyodbc
from util.DBPropertyUtil import DBPropertyUtil

class DBConnection:
    connection = None

    @staticmethod
    def getConnection():
        if DBConnection.connection is None:
            try:
                connection_string = DBPropertyUtil.getDBConn()  # Call without parentheses
                DBConnection.connection = pyodbc.connect(connection_string)
                print("Connected Successfully")
            except pyodbc.Error as e:
                print(f"Connection failed: {e}")
        else:
            print("Connection already established")

        return DBConnection.connection
