import unittest
from MainMenuController import mainMenuController

class mainMenuControllerTest(unittest.TestCase):

    __mainmenuController = mainMenuController()

    def testselect(self):
        self.assertIsNotNone(self.__mainmenuController.select('option'))

if __name__ == '__main__':
    unittest.main()
