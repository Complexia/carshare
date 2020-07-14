#! /usr/bin/python3
import cv2
import FaceAuthenticator

if __name__ == '__main__':
    camera = FaceAuthenticator.Camera()
    print(">>> camera is ready")

    recogniser = FaceAuthenticator.FaceRecogniser()
    print(">>> recogniser is ready")

    # test index 
    # recogniser.indexFace(recogniser.detect(camera.captureAndSaveImg()))

    # test search face
    faceIDs = recogniser.recognise(recogniser.detect(camera.captureAndSaveImg()))
    if faceIDs != False:
        print("Face matched")
        for faceID in faceIDs:
            print(faceID)
    else:
        print("No match")
