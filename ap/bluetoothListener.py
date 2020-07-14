import bluetooth

from .interface import Interface
from .console import Console
class BluetoothListener:

    def __init__(self):
        self.__interface = Interface()
        self.__console = Console()
        self.__carId = 2


    def listen(self):

        while True:
            result = bluetooth.lookup_name('f0:5c:77:be:dc:c6', timeout=20)
            if result:
                action = 1
                self.__console.engineerBluetoothResponse(action)
                self.__interface.unlockCarEngineer(self.__carId)
                self.__console.unlockResponse()
                break

        while True:
            result = bluetooth.lookup_name('f0:5c:77:be:dc:c6', timeout=20)
            if result == None:
                action = 0
                self.__console.engineerBluetoothResponse(action)
                self.__interface.lockCarEngineer(self.__carId)
                self.__console.lockResponse()

if __name__ == '__main__':
    BluetoothListener.listen(BluetoothListener())