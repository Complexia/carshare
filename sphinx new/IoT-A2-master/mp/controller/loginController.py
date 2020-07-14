from models import User
from mp.controller import ApiController, EncryptPassword

class LoginController:
	def __init__(self):
		self.__loggedInUser = None
		self.__userType = None
		self.__apiController = ApiController()

	#encrypts the password and verifies details against the DB
	def login(self, userName, hashedPassword):
		#hashedPassword = EncryptPassword.hash(self, password)

		#for user if logged in else returns false
		if self.verifyLogin(userName, hashedPassword):
			return self.__loggedInUser
		return None
		
	#checks the login details and returns a boolean result
	def verifyLogin(self, userName, hashedPassword): 
		url = "http://localhost:5000/css/api/v1.0/users?email={}&password={}".format(userName, hashedPassword)

		if len(self.__apiController.requestGet(url)['users']) > 0:
			jsonData = self.__apiController.requestGet(url)['users'][0]
		else:
			return False
			
		if jsonData['email'] == userName and jsonData['password'] == hashedPassword:
			self.__userType = jsonData['type']
			self.__loggedInUser = User(jsonData['id'], jsonData['username'], jsonData['password'], jsonData['firstName'], 
					jsonData['lastName'], jsonData['email'], jsonData['faceId'])
			return True
		
		return False

	def logout(self):
		self.__userType = None
		self.__loggedInUser = None

	def getLoggedInUser(self):
		return self.__loggedInUser

	def getLoggedInUserType(self):
		return self.__userType
	
	def setLoggedInUser(self, loggedInUser):
		self.__loggedInUser = loggedInUser
	
	def loginFace(self, faceID):
		url = "http://localhost:5000/css/api/v1.0/users?faceId={}".format(faceID)

		if len(self.__apiController.requestGet(url)['users']) > 0:
			jsonData = self.__apiController.requestGet(url)['users'][0]
			self.__loggedInUser = User(jsonData['id'], jsonData['username'], jsonData['password'], jsonData['firstName'], 
					jsonData['lastName'], jsonData['email'], jsonData['faceId'])
			return self.__loggedInUser

		else:
			return None
