from .carPool import carPool
from .communicationController import CommunicationController
from .locator import locator
from .loginController import loginController

class Interface:
    def __init__(self):
        self.__communicationController = CommunicationController()

    def sendMessage(self, message, key):
        self.__communicationController.sendMessage(message, key)

    def userLogin(self, username, password, host, port, key):
        self.__communicationController = CommunicationController(host, port)
        #return loginController.login(username, password)
        creds = [username, password]
        
        
        return self.__communicationController.sendMessage(creds, key)
        

    def getCarById(self,id):
        return carPool.getCar(id)

    def lockCar(self, user):
        return carPool.lockCar(user)

    def unlockCar(self, user):
        return carPool.unlockCar(user)
    
    def returnCar(self, user):
        return carPool.returnCar(user)

    def locateCar(self, car):
        return locator.getCarLocation(car)

interface = Interface()