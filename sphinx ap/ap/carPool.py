import requests, json

from models import Car

# handles car operations for agent pi
class CarPool:
    def getCar(self, id):
        response = requests.get('http://localhost:5000/css/api/v1.0/cars/{}'.format(id))
        carDict = json.loads(response.text)

        return Car(carDict['id'], carDict['make'], carDict['bodyType'], carDict['colour'], carDict['seats'], 
                carDict['location']['x'], carDict['location']['y'], carDict['costPerHour'], carDict['isLocked'])

    # should only be called on users that have booked a car
    def lockCar(self, user):
        if not user.lockCar():
            return False
        car = user.getCar()
        self.__getUpdatedFields(car)
        # update car in db - it is now locked
        requests.put('http://localhost:5000/css/api/v1.0/cars/{}'.format(car.getId()), self.__getUpdatedFields(car))
        return True

    # should only be called on users that have booked a car
    def unlockCar(self, user):
        if not user.unlockCar():
            return False
        car = user.getCar()
        # update car in db - it is now unlocked
        requests.put('http://localhost:5000/css/api/v1.0/cars/{}'.format(car.getId()), self.__getUpdatedFields(car))
        return True

    def returnCar(self, user):
        return user.returnCar()

    def __getUpdatedFields(self, car):  
        carDict = car.asDict()
        if carDict['isLocked'] == True:
            carDict['isLocked'] = 1
        else:
            carDict['isLocked'] = 0
        del carDict['id']
        return carDict

carPool = CarPool()