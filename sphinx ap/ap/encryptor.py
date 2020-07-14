import hashlib

class Encryptor:
    def hash(self, string):
        sha = hashlib.sha512(string.encode('utf-8'))
        hashedString = sha.hexdigest()
        return hashedString

encryptor = Encryptor()