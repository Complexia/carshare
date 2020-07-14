class showAllAvailableCarsConsole:

	def __init__(self, showAllCarsController):
		self.__showAllCarsController = showAllCarsController
		self.__jsonData = self.__showAllCarsController.showAllAvailableCars()
		self.__jsonDataBook = self.__showAllCarsController.getBookingsData()

	def showAllAvailableCars(self):
		print("All cars: ")	
		for x in self.__jsonData["cars"]:
			print('Car', x['id'])
			print("Car make: ",x["make"])
			print("Body type: ",x["bodyType"])
			print("Cost per hour: ",x["costPerHour"])
			print("-------------------")
		return True

	def searchCar(self):
		model = input('Please enter a car model: ')
		bodyType = input('Please enter a car body: ')
		inc = 0
		for x in self.__jsonData["cars"]:
			if str(model).lower() in str(x["make"]).lower() or str(bodyType).lower() == str(x['bodyType']).lower():
				print('Car', x['id'])
				print("Car found.")
				print("Car make:",x["make"])
				print("Body type:",x["bodyType"])
				print("Cost per hour:",x["costPerHour"])
				print("-------------------")
				inc = 1  
		
		if inc == 0:
			print("No such car found.")
			return False
		return True




			