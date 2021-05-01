import socket
import time
import pickle
import threading

message = ["1111","111111","11111111"]

stock = []

message1 = ["2222","2222","1111"]

stock1 = []


def client(clientsocket, msg, ):
    HEADERSIZE = 10
    def envoyer():
        while True:
            d = msg
            d = pickle.dumps(d)
            d = bytes(f"{len(d):<{HEADERSIZE}}", 'utf-8')+d
            clientsocket.send(d)
            time.sleep(1)
    def recevoir():
        while True:            
            full_msg=b""
            new_message=True
            mesg_complet =False

            while not mesg_complet:
                recu = clientsocket.recv(32)
                if new_message:
                    msglen = int(recu[:HEADERSIZE])
                    new_message = False
                
                full_msg+=recu
                
                if len(full_msg)-HEADERSIZE == msglen:
                    full_msg = full_msg[HEADERSIZE:]
                    full_msg=pickle.loads(full_msg)
                    global stock
                    stock = full_msg
                    mesg_complet = True
                    new_message = True
                    full_msg = b""
                
                if len(full_msg)-HEADERSIZE > msglen:
                    full_msg = b""
                    new_message = True
    th1=threading.Thread(target=envoyer)
    th1.start()
    th2= threading.Thread(target=recevoir)
    th2.start()

def start(msg):
    HEADERSIZE = 10
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 1243))
    s.listen(2)
    
    while True:
        print("en ecoute")
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established.")
        thread = threading.Thread(target=client, args=(clientsocket,msg))
        thread.start()
        

def clientext(msg,):
    HEADERSIZE = 10
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 1243))
    def envoyer():
        while True:
            
            d = msg
            d = pickle.dumps(d)
            d = bytes(f"{len(d):<{HEADERSIZE}}", 'utf-8')+d
            s.send(d)
            time.sleep(1)
    def recevoir():
        while True:
            full_msg=b""
            new_message=True
            mesg_complet =False

            while not mesg_complet:
                msg = s.recv(32)
                if new_message:
                    msglen = int(msg[:HEADERSIZE])
                    new_message = False
                
                full_msg+=msg
                
                if len(full_msg)-HEADERSIZE == msglen:
                    full_msg = full_msg[HEADERSIZE:]
                    global stock1
                    stock1 = pickle.loads(full_msg)
                    mesg_complet = True
                    new_message = True
                    full_msg = b""
                    
                
                if len(full_msg)-HEADERSIZE > msglen:
                    full_msg = b""
                    new_message = True

    th1=threading.Thread(target=envoyer)
    th1.start()
    th2= threading.Thread(target=recevoir)
    th2.start()       
        

thr= threading.Thread(target=start, args=(message,))
thr.start()
thr2= threading.Thread(target=clientext, args=(message1,))
thr2.start()

def verify():
    global message,message1,stock,stock1
    while True:
        """if m1==c2:
            print("ok")
        else:
            print("non")
        if m2==c1:
            print("ok2")
        else:
            print("non")"""
        time.sleep(3)
        print(message,message1,stock,stock1)

thr3= threading.Thread(target=verify)
thr3.start()

message1 = ["2222","2222","1111"]