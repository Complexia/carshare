import datetime, sys
from ap import console, interface
from models import Car, User
from FaceAuthenticator import Camera, FaceRecogniser

loggedInUser = None
# each agent corresponds to a single car - change the passed in id to run for different cars
thisCar = interface.getCarById(2)

def login(host='127.0.0.1', port=65432, key='sharedKey0'):

    loggedInUser = None
    thisCar = interface.getCarById(2)
    selection = console.loginMethodPrompt()
    if selection == '1':
        #as soon as user presses key, camera is initialized, taking a pic
        console.faceAuthenticatePrompt()
        camera = Camera()
        frame = camera.captureAndSaveImg()
        if frame is not None: 
            
            faceRec = FaceRecogniser()
            if faceRec.detect(frame) is not False:
                print("Face found")
                faceID = faceRec.recognise(frame)
                
                if faceID is not False:
                    loggedInUser = interface.userLoginFace(faceID, thisCar.getId(), host, port, key)
                    if loggedInUser:
                        loggedInUser.bookCar(thisCar) 
                        return loggedInUser
                    else:
                        print("Face not found. Login with email and password.")
                        selection = '2'
                else:
                    print("Face not found. Login with email and password.")
                    selection = '2'
                    
            else:
                print("Face not found. Login with email and password.")
                selection = '2'

    if selection == '2':

        while not loggedInUser:

            username, password = console.loginPrompt()
            loggedInUser = interface.userLogin(username, password, thisCar.getId(), host, port, key)
            if not loggedInUser:
                console.incorrectLogin()
        loggedInUser.bookCar(thisCar)        
        return loggedInUser  
    elif selection != '1' and selection != '2':
        console.invalidInput()

def menu(loggedInUser):

    userChoice = ''

    console.welcomeMessage(loggedInUser.getFirstName(), thisCar.getMake())

    while userChoice != '0':
        if (not loggedInUser.getCar()):
            console.noBookingWarning()
        userChoice = console.displayMenu()

        if userChoice == '1':
            if interface.unlockCar(loggedInUser):
                console.unlockResponse()
            else:
                console.unlockResponse(False)
        elif userChoice == '2':
            if interface.lockCar(loggedInUser):
                console.lockResponse()
            else:
                console.lockResponse(False)
        elif userChoice == '3':
            if interface.returnCar(loggedInUser):
                console.returnResponse()
            else:
                console.returnResponse(False)
        elif userChoice == '4':
            console.locationMessage(interface.locateCar(loggedInUser.getCar()))
        elif userChoice == '0':
            console.logoutMessage(loggedInUser.getFirstName())
        else:
           console.invalidInput()

def main():
    try:
        loggedInUser = login(sys.argv[1], int(sys.argv[2]), sys.argv[3].strip())
    except IndexError:
        console.printArgsError()
        loggedInUser = login()
        
    menu(loggedInUser)

main()