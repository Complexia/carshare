from .model import Model

class Booking(Model):
    def __init__(self, id, startTime, endTime, user, car, active):
        self.__id = id
        self.__startTime = startTime
        self.__endTime = endTime
        self.__user = user
        self.__car = car
        if active == '1' or active == True:
            self.__active = True
        else:
            self.__active = False

    # the schema is defined in object to make the create table function reusable
    @staticmethod
    def asSchemaDict():
        return {
            'id': 'INT PRIMARY KEY',
            'startTime': 'DATETIME',
            'endTime': 'DATETIME',
            'user_id': 'INT',
            'car_id': 'INT',
            'active': 'BOOLEAN',
            'FOREIGN KEY(user_id)': 'REFERENCES users(id)',
            'FOREIGN KEY(car_id)': 'REFERENCES cars(id)'
        }

    # used to insert the field names when inserting data
    @staticmethod
    def attributesAsList():
        return ['id', 'startTime', 'endTime', 'user_id', 'car_id', 'active']

    # used to be able to convert the object to json
    def asDict(self):
        print(self.__active)
        return {
            'id': self.__id,
            'startTime': self.__startTime,
            'endTime': self.__endTime,
            'user': self.__user.asDict(),
            'car': self.__car.asDict(),
            'active': self.__active
        }

    # used when inserting records
    def asTuple(self):
        print('Active when getting insertable', self.__active)
        return (self.__id, self.__startTime, self.__endTime, self.__user.getId(), self.__car.getId(),
                '1' if self.__active == True else '0')