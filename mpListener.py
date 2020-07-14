import selectors, socket, types, pickle, sys, hmac, hashlib, traceback
from mp.controller import LoginController, ApiController
sel = selectors.DefaultSelector()

#accepts incoming socket
def acceptConnection(sock):
    conn, addr = sock.accept()  #accepting incoming connection
    print('accepted connection from', addr) 
    #stops the connected socket from blocking other processes
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
    #setting up monitoring for when the socket is ready to either read or write
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)


def serviceConnection(key, mask, signature):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  #reading
        #data is being received
        if recv_data:
            data.outb += recv_data
            

            receivedDigest, pickled_data = data.outb.split(b' ')
            newDigest = signMessage(signature,pickled_data)
            
            if receivedDigest.decode() != newDigest:
                print("Corrupted data. Aborting...")
                dataString = ["1", "blank", "blank","blank"]
                
            else:

               dataString = pickle.loads(pickled_data) 
               

            apiCon = ApiController()
            loginController = LoginController()
            
            #select login method
            if dataString[0] == '1':

                data.inb = loginController.login(dataString[1],dataString[2]) #user
                
            elif dataString[0] == '2':
                
                data.inb = loginController.loginFace(dataString[1][0])
                
            #check if the user actually booked the car/use data here 
            if data.inb:
                dataBook = apiCon.requestGet("http://localhost:5000/css/api/v1.0/bookings")
                inc = 0
                for x in dataBook["bookings"]:
                    if x["car"]["id"] == dataString[3] and x["user"]["id"] == data.inb.getId() \
                    and x["active"] == 1:
                        inc = 1
                if inc == 0:
                    data.inb = None


        #if socket closed, close connection and stop monitoring the socket
        else:
            print('closing connection to', data.addr)
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE: #This is true after receiving some data from client socket
        if data.outb:
            
            data.inb = pickle.dumps(data.inb)

            digest =  signMessage(signature, data.inb)
            header = '%s' % (digest)
            
            space = ' '
            sent = sock.send(header.encode() + space.encode() + data.inb)  # Sending response to client            
            data.outb[sent:]
            data.outb = False
            
            
#listens and determines whether to accept a new con or act on existing one
def eventLoop(signature):
    while True:
        events = sel.select(timeout=None)
        try:
            for key, mask in events:
                #if there is no data, socket is not yet connected the con is accepted
                if key.data is None:
                    acceptConnection(key.fileobj)
                #if there is data, socket is already connected, and needs to be actioned
                else:
                    try:
                        serviceConnection(key, mask, signature)
                    except:
                        print("Something went wront serverside")
                        traceback.print_exc()

        except ConnectionResetError:
            print("Client crashed")


def signMessage(signature, message):
        byte_key = signature.encode()
        return hmac.new(byte_key, message, hashlib.sha1).hexdigest()


def startServer(host='', port=65432, signature='sharedKey0'):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen()
    print('listening on', (host, port))
    #setting blocking to false prevents the socket to stall other processes
    sock.setblocking(False)
    #registers the socket for monitoring. When data is sent, the socket will receive it
    sel.register(sock, selectors.EVENT_READ, data=None)
    eventLoop(signature.strip())

def main():
    try:
        startServer(sys.argv[1], int(sys.argv[2]), sys.argv[3])
    except IndexError:
        startServer()
        print("No arguments passed. Running default...")
main()