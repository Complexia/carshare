import cv2
import pyqrcode
import png
import os
import imutils
from pyzbar import pyzbar
import time
import re

WORKING_DIR = os.getcwd()
DEVICE_1 = 0

class QRHandler:
    def __init__(self):
        self.PREFIX = "/QRCode-"
    
    # generate a QRcode from an input string
    def QRGen(self, input_string):
        path_to_code_img = WORKING_DIR + self.PREFIX + input_string + ".png"
        the_qr_code = pyqrcode.create(input_string)
        the_qr_code.png(path_to_code_img, scale = 8)
    
    # Use web cam to read from camera input, return the input string from function QRGen 
    def QRReader(self):
        cam = cv2.VideoCapture(DEVICE_1)
        flag = True
        while flag:
            retval, frame = cam.read()
            if retval: 
                frame = imutils.resize(frame, width = 400)
                codes = pyzbar.decode(frame)
                length = len(codes)
                if length == 1:
                    print("Got one QR code.\n")
                    QRcodeData = str(codes[0][0])
                    userData = re.findall(r"'(.*?)'", QRcodeData)
                    data = userData[0]
                    flag = False
                    cam.release()
                    return data
                else: 
                    print("Alow ONE QRCode in front of camera\n")
            else:
                print("Camera read failed\n")
            time.sleep(1.0)