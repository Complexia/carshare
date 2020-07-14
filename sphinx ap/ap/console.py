class Console:
    def invalidInput(self):
        print('Invalid input, please re-enter')

    def loginPrompt(self):
        return input('Enter email: '), input('Enter password: ')

    def incorrectLogin(self):
        print('The details entered are incorrect. Please try again.')

    def welcomeMessage(self, firstName):
        print('Welcome', firstName, 'please select an option from below: ')

    def displayMenu(self):
        print('1.\tUnlock car')
        print('2.\tLock car')
        print('3.\tReturn car')
        print('4.\tLocate car')
        print('0.\tExit')

        return input('Enter your selection here: ')

    def unlockResponse(self, success=True):
        if (success):
            print('Car succesfully unlocked.')
        else:
            print('Car unlock failed. Perhaps it\'s already unlocked.')

    def lockResponse(self, success=True):
        if (success):
            print('Car succesfully locked.')
        else:
            print('Car lock failed. Perhaps it\'s already locked.')

    def returnResponse(self, success=True):
        if (success):
            print('Car succesfully returned. Thank you for your patronage.')
        else:
            print('Car return failed. You must first lock your car before returning it.')

    def locationMessage(self, location):
        print('Your car is currently located here {}.'.format(location))

    def logoutMessage(self, firstName):
        print('Goodbye {}! Logging you out safely.'.format(firstName))

    def noBookingWarning(self):
        print('You currently do not have a car booked! Please login to Master Pi to book a car.')

console = Console()