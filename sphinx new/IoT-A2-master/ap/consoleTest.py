import unittest
import console

class consoleTest(unittest.TestCase):

   # __loginController = LoginController()

    def testinvalidInput(self):
        self.assertTrue(console.invalidInput('cherr'))

if __name__ == '__main__':
    unittest.main()
