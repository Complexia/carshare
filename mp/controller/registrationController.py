from models import User
from mp.controller import ApiController, EncryptPassword

class RegistrationController:
	def __init__(self):
		self.__apiController = ApiController()

	#receives data, hashes the password, and creates a post request on the api
	def register(self, userName, hashedPassword, firstName, lastName, email, faceID):
		

		if self.verifyRegister(userName, email):

			url = "http://localhost:5000/css/api/v1.0/users"
			data = {"email" : email, 'faceId': str(faceID), "firstName" : firstName, "id" : str(self.__id), \
			"lastName" : lastName, "password" : hashedPassword, "type": "customer", "username" : userName}

			response = self.__apiController.requestPost(url, data)
			urlGet = "http://localhost:5000/css/api/v1.0/users?email={}&password={}".format(email, hashedPassword)
			jsonData = self.__apiController.requestGet(urlGet)['users'][0] 
			loggedInUser = User(jsonData['id'], jsonData['username'], jsonData['password'], jsonData['firstName'], 
					jsonData['lastName'], jsonData['email'], jsonData['faceId'])
			return loggedInUser


	#checks if the user with these details is already registered
	def verifyRegister(self, userName, email):
		
		url = "http://localhost:5000/css/api/v1.0/users"
		jsonData = self.__apiController.requestGet(url)
		
		for x in jsonData["users"]:
			
			if x["email"] == email:
				return False
			
		self.__id = len(jsonData["users"]) + 1

		return True
		
