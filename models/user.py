from .model import Model

class User(Model):
    # a user is abstract, 0 authorisation means they cannot access anything
    __authorisation = 0
    def __init__(self, id, username, password, firstName, lastName, email, faceId):
        self.__id = id
        self.__username = username
        self.__password = password
        self.__firstName = firstName
        self.__lastName = lastName
        self.__email = email
        self.__faceId = faceId

    def getAuthorisation(self):
        return self.__authorisation

    def getId(self):
        return self.__id

    def getUsername(self):
        return self.__username

    def getPassword(self):
        return self.__password

    def getFirstName(self):
        return self.__firstName

    def getCar(self):
        return self.__car

    def getFaceId(self):
        return self.__faceId

    # the schema is defined in object to make the create table function reusable
    @staticmethod
    def asSchemaDict():
        return {
            'id': 'INT PRIMARY KEY',
            'username': 'VARCHAR(100)',
            'password': 'VARCHAR(1000)',
            'firstName': 'VARCHAR(20)',
            'lastName': 'VARCHAR(20)',
            'email': 'VARCHAR(100)',
            'faceId': 'VARCHAR(1000)',
            'type': 'VARCHAR(20)'
        }

    # used to insert the field names when inserting data
    @staticmethod
    def attributesAsList():
        return ['id', 'username', 'password', 'firstName', 'lastName', 'email', 'faceId', 'type']

    # used to be able to convert the object to json
    def asDict(self):
        return {
            'id': self.__id,
            'username': self.__username,
            'password': self.__password,
            'firstName': self.__firstName,
            'lastName': self.__lastName,
            'email': self.__email,
            'faceId': self.__faceId
        }

    # used when inserting records
    def asTuple(self):
        return (self.__id, self.__username, self.__password, self.__firstName, self.__lastName, self.__email, \
            self.__faceId)
        