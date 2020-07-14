from .model import Model

class Report(Model):
    def __init__(self, id, car, description, open):
        self.__id = id
        self.__car = car
        self.__description = description
        if open == '1' or open == True or open == 'true' or open == 1:
            self.__open = True
        else:
            self.__open = False

    # the schema is defined in object to make the create table function reusable
    @staticmethod
    def asSchemaDict():
        return {
            'id': 'INT PRIMARY KEY',
            'carId': 'INT',
            'description': 'VARCHAR(1000)',
            'open': 'BOOLEAN',
            'FOREIGN KEY(carId)': 'REFERENCES cars(id)'
        }
    
    # used to insert the field names when inserting data
    @staticmethod
    def attributesAsList():
        return ['id', 'carId', 'description', 'open']
    
    # used to be able to convert the object to json
    def asDict(self):
        return {
            'id': self.__id,
            'car': self.__car.asDict(),
            'description': self.__description,
            'open': self.__open
        }

    # used when inserting records
    def asTuple(self):
        return (self.__id, self.__car.getId(), self.__description, self.__open)
        