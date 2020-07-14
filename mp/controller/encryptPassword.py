#hash a string with sha512
import hashlib
class EncryptPassword:
	def hash(self,password):
		sha = hashlib.sha512(password.encode('utf-8'))
		hashedPassword = sha.hexdigest()
		return hashedPassword