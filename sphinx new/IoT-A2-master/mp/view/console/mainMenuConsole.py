from mp.view.console import showAllAvailableCarsConsole
class mainMenuConsole:

	__option = None
	def __init__(self, mainMenuController, showAllCarsController):
		self.__showAllCarsController = showAllCarsController
		self.__mainMenuController = mainMenuController
		self.__mainMenuController.setShowCarsConsole(showAllAvailableCarsConsole(showAllCarsController))


	def printMenu(self):
		

		while True:
			try:
				print("-------------------")
				print("Main menu properties: ")
				print("1. View history of previously booked cars")
				print("2. Show all available cars")
				print("3. Search a car")
				print("4. Book a car")
				print("5. View current bookings")
				print("6. Cancel a booking")
				print("7. Logout")
				print("8. Go back")
				print("Select an option: ")

				r = range(1,9)
				self.__option = input()
				if int(self.__option) in r:

					break
				else:
					print("Invalid input")


			except ValueError:
				print("Invalid input")
			

		return self.__mainMenuController.select(self.__option)
	