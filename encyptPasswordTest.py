import unittest
from mp.controller import EncryptPassword

class EncryptPasswordTest(unittest.TestCase):
    __encryptor = EncryptPassword()

    def testHash(self):
        data = 'Green3#H'
        expected = 'aed85f0f64c1223e1a84d125ee7c1b7cd172727d32c7fe1c902e05f6b4cee3b90359a0b8a85c2d6aeac2b4c2e2f84deeaf3d69fbe92eadf5e2855a84d49891f1'
        self.assertEqual(self.__encryptor.hash(data), expected)

if __name__ == '__main__':
    unittest.main() 