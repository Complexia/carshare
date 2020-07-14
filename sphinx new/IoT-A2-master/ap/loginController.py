import json, requests
from .encryptor import encryptor
from models import User

class LoginController:
    def login(self, username, password):
        hashedPassword = encryptor.hash(password)
        url = 'http://localhost:5000/css/api/v1.0/users?username={}&password={}'.format(username, hashedPassword)

        response = requests.get(url)
        jsonData = json.loads(response.text)

        if (not self.__verifyLogin(jsonData, username, hashedPassword)):
            return None

        userDict = jsonData['users'][0]

        return User(userDict['id'], userDict['username'], userDict['password'], userDict['firstName'], userDict['lastName'], 
                userDict['email'])
    
    def __verifyLogin(self, jsonData, username, password):
        if not jsonData['users']:
            return False
        if len(jsonData['users']) <= 0:
            return False

        userDict = jsonData['users'][0]

        if not(userDict['username'] and userDict['password']):
            return False

        if userDict['username'] != username or userDict['password'] != password:
            return False
        
        return True

loginController = LoginController()