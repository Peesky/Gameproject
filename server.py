import socket
import socket
import time
import pickle
import threading




def client(clientsocket,stock,msg):
    HEADERSIZE = 10
    while True:
        d = msg
        msg = pickle.dumps(d)
        msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
        clientsocket.send(msg)
        time.sleep(0.002)

        full_msg=b""
        new_message=True
        mesg_complet =False


        while not mesg_complet:
            msg = clientsocket.recv(32)
            if new_message:
                msglen = int(msg[:HEADERSIZE])
                new_message = False
            
            full_msg+=msg
            
            if len(full_msg)-HEADERSIZE == msglen:
                full_msg = full_msg[HEADERSIZE:]
                full_msg =  pickle.loads(full_msg)

                stock=full_msg
                mesg_complet = True
                new_message = True
                full_msg = b""

def tuplestock(nbp,stock,stock1):
    if nbp==0:
        return [stock1,stock]
    else:
        return [ stock,stock1]

def start():
    HEADERSIZE = 10
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 1243))
    s.listen(2)
    numplayer = 0
    stock=[]
    stock1=[]

    threads = []

    while True:
        print("en ecoute")
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established.")
        thread = threading.Thread(target=client, args=[clientsocket]+tuplestock(numplayer,stock,stock1))
        thread.start()
        threads.append(thread)
        numplayer+=1
            

start()  