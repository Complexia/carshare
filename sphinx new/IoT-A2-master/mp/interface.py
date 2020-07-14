from mp.controller import LoginController, RegistrationController, VerificationController, \
ShowAllCarsController, MainMenuController, InitialMenuController, BookingController, googleController, \
EncryptPassword, CameraController
from mp.view.console import loginFromConsole, registerFromConsole, showAllAvailableCarsConsole, \
mainMenuConsole, initialMenuConsole, bookingConsole


class Interface:
    def mainMenu(self):
        showCarsController = ShowAllCarsController()
        book = bookingConsole(self.__bookingController, self.__user)
        menuController = MainMenuController()
        menuController.setUser(self.__user)
        menuController.setBookingConsole(book)
        menu = mainMenuConsole(menuController, showCarsController)
        return menu.printMenu()
	
    def userLogin(self):
        logController = LoginController()
        verController = VerificationController()
        encryptPassword = EncryptPassword()
        log = loginFromConsole(logController, verController, encryptPassword)
        return log.login()

    def userRegister(self):
        camController = CameraController(self.__camera, self.__recogniser)
        regController = RegistrationController()
        verController = VerificationController()
        encryptPassword = EncryptPassword()
        reg = registerFromConsole(verController, regController, encryptPassword, camController)
        reg.register()

    def showAllAvailableCars(self):
        showCarsController = ShowAllCarsController()
        showCars = showAllAvailableCarsConsole(showCarsController)
        showCars.showAllAvailableCars()

    def initialMenu(self):
        camController = CameraController(self.__camera, self.__recogniser)
        logController = LoginController()
        verController = VerificationController()
        regController = RegistrationController()
        encryptPassword = EncryptPassword()
        log = loginFromConsole(logController, verController, encryptPassword)
        reg = registerFromConsole(verController,regController, encryptPassword, camController)
        menuController = InitialMenuController(log, reg)
        menuConsole = initialMenuConsole(menuController)
        self.__user = menuConsole.printMenu()
        self.__bookingController = BookingController(self.__user)
        print('Please wait while your existing bookings are updated...')
        self.__bookingController.updateBookingsStatus()
        return self.__user

    def calendarSetup(self):
        googleController.authenticateGoogleUser()
        googleController.fetchCalendar()


    def setFaceClasses(self, camera, recogniser):
        self.__camera = camera
        self.__recogniser = recogniser

interface = Interface()