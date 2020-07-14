from .user import User

class Admin(User):
    def __init__(self, id, username, password, firstName, lastName, email, faceId):
        super(Admin, self).__init__(id, username, password, firstName, lastName, email, faceId)
        # additional authentication 
        self.__authorisation = 1

    # used to be able to convert the object to json
    def asDict(self):
        base = super(Admin, self).asDict()
        base.update({'type': 'admin'})
        return base

    # used when inserting records
    def asTuple(self):
        base = list(super(Admin, self).asTuple())
        base.append('admin')
        return tuple(base)
    