class CameraController:

    def __init__(self, camera, recogniser):
        self.__camera = camera
        self.__recogniser = recogniser

    def takeAndIndex(self):
        frame = self.__camera.captureAndSaveImg()
        if frame is not None:
            frame = self.__recogniser.detect(frame)
            if frame is not False:
                faceID = self.__recogniser.recognise(frame)
                if faceID is False:
                    faceID = self.__recogniser.indexFace(frame)
                    if faceID is not False:
                        return faceID
                else:
                    print("Duplicate face found. No face will be saved")
        return None