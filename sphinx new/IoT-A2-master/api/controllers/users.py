from api import db
from models import Admin, Customer, Engineer, Manager, User
from flask import jsonify

# performs request response for routes pertaining to the User resource (and subclasses)
class UserController:
    __userTypes = {
        'admin': Admin,
        'customer': Customer,
        'engineer': Engineer,
        'manager': Manager
    }

    def getUser(self, id):
        userTuple = db.getObjectById('users', id)[0]
        userType = userTuple[7]
        classType = self.__userTypes[userType]

        if userType not in self.__userTypes:
            return jsonify({'Error': 'Not found'}), 404

        user = self.__createUserFromType(userTuple, userType)

        return jsonify(user.asDict())

    def getUsers(self, params=None):
        users = []
        classType = User
        # fetch all users in the database, this does not discriminate based on type
        if not params:
            userTuples = db.getAllObjects('users')
        else:
            userType = None
            # the type param is used only to verify what user kind is requested and is not needed for object creation
            if params.get('type'):
                userType = params['type']
            for param in params:
                if param == 'type':
                    continue
                    # if there is an unexpected param the search fails
                if param not in User.attributesAsList():
                    return jsonify({'Users': []})
            if userType:
                if userType in self.__userTypes:
                    classType = self.__userTypes[userType]
            userTuples = db.getObjectsByFilter('users', list(params.keys()), list(params.values()))

        # aggregate the rows
        for i in range(len(userTuples)):
            users.append(classType(userTuples[i][0], userTuples[i][1], userTuples[i][2], userTuples[i][3], \
                userTuples[i][4], userTuples[i][5], userTuples[i][6]))

        userDicts = []

        for i in range(len(users)):
            userDict = users[i].asDict()
            userDict.update({'type': userTuples[i][7]})
            userDicts.append(userDict)

        # jsonify each user object's dict
        return jsonify(users=userDicts)

    def createUser(self, params):
        userType = None
        # cannot create a user without params
        if not params:
            return jsonify({'Error': 'Bad Request'}), 400
        # for all user types there must be 8 params - including type
        if len(params) != 8:
            return jsonify({'Error': 'Bad Request'}), 400
        # a type must be specified so the backend can create a resulting user
        if params[7] not in self.__userTypes:
            return jsonify({'Error': 'Bad Request'}), 400
        userType = params[7]
        # construct a user object from the gathered data
        user = None

        if userType in self.__userTypes:
            user = self.__userTypes[userType](params[0], params[1], params[2], params[3], params[4], params[5], params[6])
        else:
            return jsonify({'Error': 'Bad Request'}), 400

        db.insertObject('users', User.attributesAsList(), user.asTuple())
        
        # update the database with the new user and respond with a confirmation of insertion
        return jsonify({'user': user.asDict()}), 201

    def updateUser(self, id, fieldsToUpdate, params):
        # when updating there can be between 0 and 8 params
        if params and (len(params) > 8 or len(params) < 0):
            return jsonify({'Error': 'Bad Request'}), 400
        # update the user with the specified id, indicating which fields to update and what to update them to
        db.updateObject('users', id, fieldsToUpdate, params)
        # retrieve the newly updated user and create an object from it's data
        userTuple = db.getObjectById('users', id)[0]
        userType = userTuple[7]
        classType = self.__userTypes[userType]
        user = classType(userTuple[0], userTuple[1], userTuple[2], userTuple[3], userTuple[4], userTuple[5], userTuple[6])
        # jsonify the user to confirm the update
        return jsonify({'user': user.asDict()}), 201

    def deleteUser(self, id):
        db.deleteObject('users', id)
        return jsonify({'result': True})

    def __createUserFromType(self, userTuple, userType):
        classType = self.__userTypes[userType]
        return classType(userTuple[0], userTuple[1], userTuple[2], userTuple[3], userTuple[4], userTuple[5], userTuple[6])

# create a single instance of a UserController to be exported
usersController = UserController()