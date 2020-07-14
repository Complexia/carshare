from .user import User

class Manager(User):
    def __init__(self, id, username, password, firstName, lastName, email, faceId):
        User.__init__(self, id, username, password, firstName, lastName, email, faceId)
        self.__authorisation = 2

    # used to be able to convert the object to json
    def asDict(self):
        base = super(Manager, self).asDict()
        base.update({'type': 'manager'})
        return base

    # used when inserting records
    def asTuple(self):
        base = list(super(Manager, self).asTuple())
        base.append('manager')
        return tuple(base)