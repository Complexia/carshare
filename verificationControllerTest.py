import unittest
from mp.controller import VerificationController

class MiddlewareTest(unittest.TestCase):
    __verificationController = VerificationController()

    def testVerifyUserName(self):
        validUsername = 'Tenmei'
        self.assertTrue(self.__verificationController.verifyUsername(validUsername))

    def testVerifyPassword(self):
        validPassword = 'Green3#H'
        self.assertTrue(self.__verificationController.verifyPassword(validPassword))

    def testVerifyFirstName(self):
        validFirstName = 'Noriaki'
        self.assertTrue(self.__verificationController.verifyFirstName(validFirstName))

    def testVerifyLastName(self):
        validLastName = 'Kakyoin'
        self.assertTrue(self.__verificationController.verifyLastName(validLastName))

    def testVerifyEmail(self):
        validEmail = 'cherry@email.com'
        self.assertTrue(self.__verificationController.verifyEmail(validEmail))

if __name__ == '__main__':
    unittest.main() 