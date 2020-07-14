class loginFromConsole:
	def __init__(self, loginController, verificationController, encryptPassword):
		self.__loginController = loginController
		self.__verificationController = verificationController
		self.__encryptPassword = encryptPassword

	def login(self):
		loggedInUser = None
		while (loggedInUser is None):
			while True:
				print("Enter email: ")
				self.__userName = input()
				if self.__verificationController.verifyEmail(self.__userName):
					break
				else:
					self.__verificationController.printMessage()
			
			print("Enter Password: ")
			self.__password = self.__encryptPassword.hash(input())

			#once the format entered was verified correct, the login details are verified with db
			#loginFromConsole.login() --> loginController.login() --> loginController.veryfyLogin()
			loggedInUser = self.__loginController.login(self.__userName,self.__password)

			if (loggedInUser == None):
				print('Sorry, your details aren\'t correct. Please re-enter them.')

		return loggedInUser

	def getLoginController(self):
		return self.__loginController

	def getVerificationController(self):
		return self.__verificationController

