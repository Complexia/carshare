import mysql.connector
from api.queryEngine import QueryEngine
from models import Admin, Booking, Car, Customer, Engineer, Manager, Report, User

class DatabaseHandler:
    def __init__(self, hostName):
        self.__conn = mysql.connector.connect(
            host=hostName,
            user='root',
            passwd='raging_mango-39'
        )
        # the query engine exists for abstraction purposes, database handler only directly uses a 'conn' object
        # query engine will perform anything requiring a 'cursor' object
        self.__queryEngine = QueryEngine(self.__conn)

    # create database if it doesn't exist and use it
    def createDB(self, dbName):
        self.__queryEngine.createDB(dbName)

    # use the query engine to create all of the tables the database will contain
    def createTables(self):
        self.__queryEngine.createTable('cars', Car.asSchemaDict())
        self.__queryEngine.createTable('users', User.asSchemaDict())
        self.__queryEngine.createTable('bookings', Booking.asSchemaDict())
        self.__queryEngine.createTable('reports', Report.asSchemaDict())

    # insert a single record into the database
    def insertObject(self, tableName, attrList, objTuple):
        self.__queryEngine.insertObject(tableName, attrList, objTuple)
        self.__conn.commit()

    # insert a list of records into the database 
    def insertObjects(self, tableName, attrList, objTupleList):
        self.__queryEngine.insertObjects(tableName, attrList, objTupleList)
        self.__conn.commit()

    # return a single resource given a provided id
    def getObjectById(self, tableName, id):
        return self.__queryEngine.getObjectById(tableName, id)

    # return all resources of a certain type
    def getAllObjects(self, tableName):
        return self.__queryEngine.getAllObjects(tableName)

    # return all resources of a certain type that meet a criteria
    def getObjectsByFilter(self, tableName, filterParams, filterValues):
        return self.__queryEngine.getObjectsByFilter(tableName, filterParams, filterValues)

    # update a resource given its id and parameters to change
    def updateObject(self, tableName, id, attrList, newParams):
        self.__queryEngine.updateObject(tableName, id, attrList, newParams)
        self.__conn.commit()

    # delete a resource
    def deleteObject(self, tableName, id):
        self.__queryEngine.deleteObject(tableName, id)
        self.__conn.commit()

    # drop a table
    def dropTable(self, tableName):
        self.__queryEngine.dropTable(tableName)

    # get all bookings containing this user_id
    def getBookingHistory(self, user_id):
        return self.__queryEngine.getBookingHistory(user_id)
    
    # close the current connection
    def shutdown(self):
        self.__conn.close()

    