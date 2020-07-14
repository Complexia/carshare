import os
import time
#from assistant-sdk-python.google-assistant-sdk.googlesamples.assistant.grpc import pushtotalk
class VoiceSearch:

    def __init__(self):  
        return None

   
    def voiceQuery(self):
        os.system('python3 mp/VoiceSearch/assistant-sdk-python/google-assistant-sdk/googlesamples/assistant/grpc/pushtotalk.py')
        #pushtotalk.main()

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
