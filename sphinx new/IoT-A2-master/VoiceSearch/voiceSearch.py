import os
import threading
import time
class VoiceSearch:

    def __init__(self):  
        return None

   
    def voiceQuery(self):
        os.system('python3 assistant-sdk-python/google-assistant-sdk/googlesamples/assistant/grpc/pushtotalk.py')

    def voiceAnswer(self):   
        carFile = open("carFile.txt","r") 
        car = carFile.readline()
        carFile.close()
        open("carFile", 'w').close()
        return car
  
    def voiceSearch(self):
        self.voiceQuery()
        return self.voiceAnswer()


if __name__ == '__main__':
    VoiceSearch.voiceSearch(VoiceSearch())
