import unittest
import hashlib
from encryptor import Encryptor

class encryptorTest(unittest.TestCase):
    __encryptor = Encryptor()

    def setUp(self):
        return super().setUp()

    def testhash(self):
        self.assertEqual(self.__encryptor.hash('Gree56'), 'd730f134b4dbd3878ce97dc55ee57067a543438fd1ef4702b904097b528dcb9baf3b22a4271647e8050198dfe27eef466248d20b85c0f6b9e4cb14845c3c0405')

if __name__ == '__main__':
    unittest.main()
