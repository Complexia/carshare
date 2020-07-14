class registerFromConsole:
    def __init__(self, verificationController, registrationController, encryptPassword, camController):
        self.__verificationController = verificationController
        self.__registrationController = registrationController
        self.__encryptPassword = encryptPassword
        self.__camController = camController

    def register(self):
        print("Please register your account")

        
        while True:

            print("Enter Username: ")
            self.__userName = input()
            if not self.__verificationController.verifyUsername(self.__userName):
                self.__verificationController.printMessage()
            else:
                break

        while True:

            print("Enter Password: ")
            self.__password = input()
            self.__hashedPassword = self.__encryptPassword.hash(self.__password)
            if not self.__verificationController.verifyPassword(self.__password):
                self.__verificationController.printMessage()
            else:
                break

        while True:

            print("Enter First name: ")
            self.__firstName = input()
            if not self.__verificationController.verifyFirstName(self.__firstName):
                self.__verificationController.printMessage()
            else:
                break

        while True:

            print("Enter Last name: ")
            self.__lastName = input()
            if not self.__verificationController.verifyLastName(self.__lastName):
                self.__verificationController.printMessage()
            else:
                break       

        while True:

            print("Enter email: ")
            self.__email = input()
            if not self.__verificationController.verifyEmail(self.__email):
                self.__verificationController.printMessage()
            else:
                break   

        while True:
            print("Opt in for Face Recognition?")
            print("1. Yes")
            print("2. No")
            self.__faceID = None
            cho = input()
            if cho == '1':

                print("When ready, face the camera and press any key.")
                input()
                self.__faceID = self.__camController.takeAndIndex()
                

                break
            elif cho == '2':
                print("No face will be saved")
                break

                
        return self.__registrationController.register(self.__userName, self.__hashedPassword, \
            self.__firstName, self.__lastName, self.__email, self.__faceID)