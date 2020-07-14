class initialMenuConsole:

	def __init__(self, initialMenuController):
		self.__option = None
		self.__initialMenuController = initialMenuController

	def printMenu(self):

		while True:

			try:

				print("Car share app")
				print("1. Log in")
				print("2. Register")
				print("Select your choice: ")

				self.__option = input()
				r = range(1,3)
				if int(self.__option) in r:
					break
				else:
					print("Invalid input")

			except ValueError:
				print("Invalid input")

			

		return self.__initialMenuController.select(self.__option)