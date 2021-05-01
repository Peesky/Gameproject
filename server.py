import socket
import socket
import time
import pickle
import threading




def client(clientsocket,stock,msg):
    HEADERSIZE = 10
    while True:
        print(f"stock, msg : {stock, msg}")
        message = msg
        if len(msg)>0:
            message = pickle.dumps(message)
            message = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+message
            clientsocket.send(message)
        time.sleep(0.002)

        full_msg=b""
        new_message=True
        mesg_complet =False


        while not mesg_complet:
            msg = clientsocket.recv(32)
            print(f"message recu : {msg}")
            if new_message:
                msglen = int(msg[:HEADERSIZE])
                new_message = False
            
            full_msg+=msg
            
            if len(full_msg)-HEADERSIZE == msglen:
                full_msg = full_msg[HEADERSIZE:]
                full_msg =  pickle.loads(full_msg)
                print(f"full msg recu decrypte{full_msg}")
                stock=full_msg
                print("oki")
                mesg_complet = True
                new_message = True
                full_msg = b""

def tuplestock(nbp,stock,stock1):
    if nbp==0:
        return [stock1,stock]
    else:
        return [ stock,stock1]

def printstock(b,a):
    while True:
        print(f"stock a,b : {a,b}")

def start():
    HEADERSIZE = 10
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 1243))
    s.listen(2)
    numplayer = 0
    stock=[]
    stock1=[]

    threads = []
    thr=threading.Thread(target=printstock, args = (stock1,stock))
    #thr.start()

    while True:
        print("en ecoute")
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established.")
        thread = threading.Thread(target=client, args=[clientsocket]+tuplestock(numplayer,stock,stock1))
        thread.start()
        threads.append(thread)
        numplayer+=1
        
            

start()  