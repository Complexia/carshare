from .model import Model

class Car(Model):
    def __init__(self, id, make, bodyType, colour, seats, xCoordinate, yCoordinate, costPerHour, isLocked):
        self.__id = id
        self.__make = make
        self.__bodyType = bodyType
        self.__colour = colour
        self.__seats = seats
        self.__location = {'x': xCoordinate,'y': yCoordinate}
        self.__costPerHour = costPerHour
        if isLocked == '1' or isLocked == True or isLocked == 'true' or isLocked == 1:
            self.__isLocked = True
        else:
            self.__isLocked = False

    def getId(self):
        return self.__id

    def getMake(self):
        return self.__make

    def getBodyType(self):
        return self.__bodyType

    def getColour(self):
        return self.__colour

    def getSeats(self):
        return self.__seats
        
    def getLocation(self):
        return self.__location

    def isCarLocked(self):
        return self.__isLocked

    # the schema is defined in object to make the create table function reusable
    @staticmethod
    def asSchemaDict():
        return {
            'id': 'INT PRIMARY KEY',
            'make': 'VARCHAR(100)',
            'bodyType': 'VARCHAR(100)',
            'colour': 'VARCHAR(20)',
            'seats': 'INT',
            'xCoordinate': 'REAL',
            'yCoordinate': 'REAL',
            'costPerHour': 'REAL',
            'isLocked': 'BOOLEAN'
        }

    # used to insert the field names when inserting data
    @staticmethod
    def attributesAsList():
        return ['id', 'make', 'bodyType', 'colour', 'seats', 'xCoordinate', 'yCoordinate', 'costPerHour', 'isLocked']

    # used to be able to convert the object to json
    def asDict(self):
        return {
            'id': self.__id,
            'make': self.__make,
            'bodyType': self.__bodyType,
            'colour': self.__colour,
            'seats': self.__seats,
            'location': self.__location,
            'costPerHour': self.__costPerHour,
            'isLocked': self.__isLocked
        }

    # used when inserting records
    def asTuple(self):
        return (self.__id, self.__make, self.__bodyType, self.__colour, self.__seats, self.__location['x'], self.__location['y'], 
                self.__costPerHour, '1' if self.__isLocked == True else '0')

    def lock(self):
        if self.__isLocked:
            return False
        self.__isLocked = True
        return True

    def unlock(self):
        if not self.__isLocked:
            return False
        self.__isLocked = False
        return True