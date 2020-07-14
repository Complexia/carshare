import unittest
from mp.controller import EncryptPassword, LoginController

class LoginControllerTest(unittest.TestCase):

    __loginController = LoginController()

    def testLogin(self):
        encryptor = EncryptPassword()
        self.assertIsNotNone(self.__loginController.login('cherry@email.com', encryptor.hash('Green3#H')))

    def testLogout(self):
        self.__loginController.logout()
        self.assertIsNone(self.__loginController.getLoggedInUser())

if __name__ == '__main__':
    unittest.main() 
