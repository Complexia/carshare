import re
class VerificationController:
	def verifyUsername(self, userName):		
		LENGTH = re.compile(r'.{4,20}')
		NO_SPECIAL_CHARS = re.compile(r'[^!@#$%^&*]')  
		ALL_PATTERNS = (LENGTH, NO_SPECIAL_CHARS)
		if all(pattern.search(userName) for pattern in ALL_PATTERNS):
			return True
		else:
			self.__errorMessage = "Username invalid Must be at least 4 chars long and contain no \
			special characters."
			return False
		
	def verifyPassword(self, password):
		LENGTH = re.compile(r'.{8,}')  
		UPPERCASE = re.compile(r'[A-Z]')
		LOWERCASE = re.compile(r'[a-z]')
		DIGIT = re.compile(r'[0-9]')
		SPECIAL_CHARS = re.compile(r'[[!@#$%^&*]')
		ALL_PATTERNS = (LENGTH, UPPERCASE, LOWERCASE, DIGIT, SPECIAL_CHARS)
		if all(pattern.search(password) for pattern in ALL_PATTERNS):
			return True
		else:
			self.__errorMessage = "The password must contain one lower case, \
			one upper case, one digit, and one special character."
			return False


	def verifyFirstName(self, firstName):
		LENGTH = re.compile(r'.{1,20}')
		NO_SPECIAL_CHARS = re.compile(r'[^!@#$%^&*]') 
		NO_DIGISTS = firstName.isalpha() 
		ALL_PATTERNS = (LENGTH, NO_SPECIAL_CHARS)
		if NO_DIGISTS and all(pattern.search(firstName) for pattern in ALL_PATTERNS):
			return True
		else:
			self.__errorMessage = "First name invalid."
			return False

	def verifyLastName(self, lastName):
		LENGTH = re.compile(r'.{2,20}')
		NO_SPECIAL_CHARS = re.compile(r'[^!@#$%^&*]') 
		NO_DIGISTS = lastName.isalpha() 
		ALL_PATTERNS = (LENGTH, NO_SPECIAL_CHARS)
		if NO_DIGISTS and all(pattern.search(lastName) for pattern in ALL_PATTERNS):
			return True
		else:
			self.__errorMessage = "Last name invalid."
			return False

	def verifyEmail(self, email):
		pattern = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
		if re.search(pattern,email):
			return True
		else:
			self.__errorMessage = "The email format is invalid."
			return False

	def printMessage(self):
		print(self.__errorMessage)
