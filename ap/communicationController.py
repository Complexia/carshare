import socket, pickle, hmac, hashlib, traceback, binascii

class CommunicationController:
    def __init__(self, host='127.0.0.1', port=65432):
        
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.__socket.connect((host, port))
        except socket.error:
            pass

    def sendMessage(self, message, key):
        try:
            #signing and sending message
            data = pickle.dumps(message)
            digest =  self.signMessage(key, data)           
            header = '%s' % (digest)
            space = ' '
            self.__socket.send(header.encode() + space.encode() + data)

            #verifying and receiving message
            response = self.__socket.recv(1024)
            receivedDigest, data = response.split(b' ')
            newDigest = self.signMessage(key,data)
            if receivedDigest.decode() != newDigest:
                print("Corrupted data. Aborting...")
                return None
            else:
               response = pickle.loads(data)
            
            
            
            return response
        except Exception as e:
            print("Something went wrong clientside.")
            print(e)
            traceback.print_exc()
            return None
        
          
    def closeConnection(self):
        self.__socket.close()

    def signMessage(self, key, message):
        byte_key = key.encode()
        return hmac.new(byte_key, message, hashlib.sha1).hexdigest()