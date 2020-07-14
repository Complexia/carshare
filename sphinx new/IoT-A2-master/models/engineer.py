from .user import User

class Engineer(User):
    __reportedCars = []
    def __init__(self, id, username, password, firstName, lastName, email, faceId, reportedCars=None):
        User.__init__(self, id, username, password, firstName, lastName, email, faceId)
        # if there are existing reported cars assigned to the engineer, initialise them
        self.__reportedCars.append(reportedCars)
        self.__authorisation = 3

    def addReportedCar(self, reportedCar):
        self.__reportedCars.append(reportedCar)

    def generateQRCode(self):
        return None

     # used to be able to convert the object to json
    def asDict(self):
        base = super(Engineer, self).asDict()
        base.update({'type': 'engineer'})
        return base

    # used when inserting records
    def asTuple(self):
        base = list(super(Engineer, self).asTuple())
        base.append('engineer')
        return tuple(base)