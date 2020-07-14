import unittest
import hashlib
from mp.controller import encryptor

class encryptorTest(unittest.TestCase):

    def testhash(self):
        self.assertTrue(encryptor.hash('Gree56'))

if __name__ == '__main__':
    unittest.main()
