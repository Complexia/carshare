import unittest
import hashlib
from encryptPassword import EncryptPassword

class encryptPasswordTest(unittest.TestCase):

    __encryptPassword = EncryptPassword()

    def setUp(self):
        self.__testString = 'Oh, you\'re approaching me?'
        self.__expectedHash = '381ae04d31be63afba3e8f36a098bd17a56462d534b14ae88bd84a37e34ef0e6305c9d8bd253fef817213afb10c99bdcdded8ca816cd06d79dc8e15910b0b1ca'
        return super().setUp()

    def testhash(self):
        self.assertEqual(self.__encryptPassword.hash(self.__testString), self.__expectedHash)

if __name__ == '__main__':
    unittest.main()
