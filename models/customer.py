from .user import User

class Customer(User):
    def __init__(self, id, username, password, firstName, lastName, email, faceId, car=None):
        User.__init__(self, id, username, password, firstName, lastName, email, faceId)
        self.__car = car
        self.__authorisation = 4

    def bookCar(self, car):
        if not self.__car:
            self.__car = car
            return True
        return False

    def cancelBooking(self):
        if self.__car:
            self.__car = None
            return True
        return False

    def returnCar(self):
        if not self.__car:
            return False
        if not self.__car.isCarLocked():
            return False
        returnedCar = self.__car
        self.__car = None
        return True

    def lockCar(self):
        if self.__car is None:
            return False
        return self.__car.lock()

    def unlockCar(self):
        if self.__car is None:
            return False
        return self.__car.unlock()

    # used to be able to convert the object to json
    def asDict(self):
        base = super(Customer, self).asDict()
        base.update({'type': 'customer'})
        return base

    # used when inserting records
    def asTuple(self):
        base = list(super(Customer, self).asTuple())
        base.append('customer')
        return tuple(base)