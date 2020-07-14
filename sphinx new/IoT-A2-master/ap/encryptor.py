#hash a string with sha512
import hashlib
class Encryptor:
    def hash(password):
        sha = hashlib.sha512(password.encode('utf-8'))
        hashedPassword = sha.hexdigest()
        return hashedPassword