import cv2
import boto3
import time
import os
import numpy as np
import json

WORKING_DIR = os.getcwd()
PATH_to_frontalface_default = WORKING_DIR + "/FaceAuthenticator/haarcascade_frontalface_default.xml"
FACE_CASCADE = cv2.CascadeClassifier(PATH_to_frontalface_default)
REJECT_LEVEL = 1.3
REJECT_WEIGHTS = 5
DEVICE_1 = 0

"""
Take a frame of image using local camera
"""
class Camera:
    def __init__(self):
        print("Camera initialized")
        
    def captureAndSaveImg(self):
        self.lens = cv2.VideoCapture(DEVICE_1)
        ts = time.time()
        retval, frame = self.lens.read()
        self.lens.release()
        if retval:
            return frame
        else:
            print("Camera reading failed")
            return None
class FaceRecogniser:
    def __init__(self):
        self.haarcascade_frontface = FACE_CASCADE

    #  Detect if there is one face in the image, 
    def detect(self, frame):
        grayImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.haarcascade_frontface.detectMultiScale(grayImg, REJECT_LEVEL, REJECT_WEIGHTS)

        if (len(faces) == 1):
            print(">>> One face detected")
            return frame
        elif (len(faces) == 0):
            print(">>> No face detected")
            return False
        else:
            print(str(len(faces)) + " face(s) detected")
            return False

    # Index the input face and associate that facial signature with userID
    def indexFace(self, frame):
        is_success, img_buf_arr = cv2.imencode(".png", frame)
        if is_success:
            byte_img = img_buf_arr.tobytes()
            reko = boto3.client('rekognition', region_name = 'ap-southeast-2')
            response = reko.index_faces(
                CollectionId = 'rmit-user-collection',
                Image = {
                    'Bytes': byte_img
                },
                MaxFaces = 1
            )
            faceID = response['FaceRecords'][0]['Face']['FaceId']
            confidence = response['FaceRecords'][0]['Face']['Confidence']
            print(">>> Face indexed." + "\nFace ID is: " + faceID + "\nConfidence level: " + str(confidence))
            return faceID
        else:
            print(">>> image converting failed")
            return False

    # Recognise input face against collection 
    def recognise(self, frame):
        faceIDs = []
        is_success, img_buf_arr = cv2.imencode(".png", frame)
        if is_success:
            byte_img = img_buf_arr.tobytes()
            reko = boto3.client('rekognition', region_name = 'ap-southeast-2')
            response = reko.search_faces_by_image(
                CollectionId='rmit-user-collection',
                Image={
                    'Bytes': byte_img
                },
                MaxFaces=1
            )
            if len(response['FaceMatches']) >= 1:
                print(">>> Face(s) matched")
                for face in response['FaceMatches']:
                    faceIDs.append(face['Face']['FaceId'])
                print(faceIDs)
                print(">>> number of matched face(s): " + str(len(faceIDs)))
                return faceIDs
            else:
                print(">>>No faces found")
                return False
        else:
            print(">>> image converting failed")
            return False