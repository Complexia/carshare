import socket
import threading
from requests import get


def start_server(host='', port=1060):
   global sock_server
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   s.bind((host, port))
   s.listen(1)
   while True:
      sock_server, sockname = s.accept()
      break


def receiveMessage(sock):
   message = sock.recv(32)
   return message


def stopAlarm():
   pass


def startAlarm():
   pass


class OrderWaiter(threading.Thread):
   def __init__(self, **kwargs):
      super(OrderWaiter, self).__init__(**kwargs)

   def run(self):
      global sock_server
      while True:
         try:
            message = receiveMessage(sock_server)
         except Exception:
            pass
         else:
            if message != '':
               if message == 'stop alarm':
                  stopAlarm()
               elif message == 'start alarm':
                  startAlarm()
               sock_server.close()
               break

if __name__ == '__main__':
   sock_server = None
   start_server() # pass the host and the port as parameters
   OrderWaiter().start() #start the thread which will wait for the order