class InitialMenuController:

	def __init__(self, loginFromConsole, registerFromConsole):
		self.__loginFromConsole = loginFromConsole
		self.__registerFromConsole = registerFromConsole

	def select(self, option):
		if int(option) == 1:
			return self.__loginFromConsole.login()
		elif int(option) == 2:
			return self.__registerFromConsole.register()
