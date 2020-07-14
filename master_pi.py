from mp import app, interface
from FaceAuthenticator import Camera, FaceRecogniser
def main():
    camera = Camera()
    recogniser = FaceRecogniser()
    interface.setFaceClasses(camera,recogniser)
    console = False
    if console:
        loggedInUser = interface.initialMenu()

        interface.calendarSetup()
        
        while not loggedInUser is None:
            loggedInUser = interface.mainMenu()
    else:
        app.run(port=5001)
    
main()