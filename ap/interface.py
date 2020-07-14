from .carPool import carPool
from .communicationController import CommunicationController
from .locator import locator


class Interface:
    def __init__(self):
        self.__communicationController = CommunicationController()

    def sendMessage(self, message, key):
        self.__communicationController.sendMessage(message, key)

    def userLogin(self, username, password, carId, host, port, key):
        self.__communicationController = CommunicationController(host, port)
        creds = ["1", username, password, carId]
        return self.__communicationController.sendMessage(creds, key)
        
    def userLoginFace(self, faceID, carId, host, port, key):
        self.__communicationController = CommunicationController(host, port)
        creds = ["2", faceID,  "placeHolder", carId]
        return self.__communicationController.sendMessage(creds, key)

    def getCarById(self,id):
        return carPool.getCar(id)

    def lockCar(self, user):
        return carPool.lockCar(user)

    def unlockCar(self, user):
        return carPool.unlockCar(user)

    def unlockCarEngineer(self, carId):
        return carPool.unlockCarEngineer(carId)

    def lockCarEngineer(self, carId):
        return carPool.lockCarEngineer(carId)
    
    def returnCar(self, user):
        return carPool.returnCar(user)

    def locateCar(self, car):
        return locator.getCarLocation(car)

interface = Interface()