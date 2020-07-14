import unittest


from middleware import Middleware


class middlewareTest(unittest.TestCase):

    _middleware = Middleware()

    def __validateRegister(self):
       
        self.assertIsNotNone(self. _middleware.__validateRegister('Ridoy','5622#','Mehei','hasan','cherry@email.com'))

   
if __name__ == '__main__':
    unittest.main() 
