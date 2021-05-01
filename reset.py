import socket
import time
import pickle
import threading

message = ["1111","111111","11111111"]

cible = []

message1 = ["lfrslsf","lsfsdfs","fssdfs",]

cible1 = []

def client(clientsocket, msg, cible):
    listerecue=[]
    HEADERSIZE = 10
    while True:
        d = msg#["a","b","c","d","e","f"]
        d = pickle.dumps(d)
        d = bytes(f"{len(d):<{HEADERSIZE}}", 'utf-8')+d
        #print(f"message a envoyer : {d}")
        clientsocket.send(d)
        time.sleep(3)

        full_msg=b""
        new_message=True
        mesg_complet =False
        #print(f"liste recue : {listerecue}")

        while not mesg_complet:
            recu = clientsocket.recv(32)
            if new_message:
                msglen = int(recu[:HEADERSIZE])
                #print("new msg len:",msglen)
                new_message = False
            
            full_msg+=recu
            
            if len(full_msg)-HEADERSIZE == msglen:
                full_msg = full_msg[HEADERSIZE:]
                #print("full msg with header", full_msg)
                cible = pickle.loads(full_msg)
                #print("listerecue : ",listerecue)
                mesg_complet = True
                new_message = True
                full_msg = b""
               
            if len(full_msg)-HEADERSIZE > msglen:
                full_msg = b""
                new_message = True


def start(msg,cible):
    HEADERSIZE = 10
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 1243))
    s.listen(2)
    
    while True:
        print("en ecoute")
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established.")
        thread = threading.Thread(target=client, args=(clientsocket,msg,cible))
        thread.start()
        
thr= threading.Thread(target=start, args=(message,cible))
thr.start()

def clientext(msg, cible):
    HEADERSIZE = 10
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 1243))
    listerecue=[]
    
    while True:
        full_msg=b""
        new_message=True
        mesg_complet =False

        while not mesg_complet:
            msg = s.recv(32)
            if new_message:
                msglen = int(msg[:HEADERSIZE])
                #print("new msg len:",msglen)
                new_message = False
            
            full_msg+=msg
            
            if len(full_msg)-HEADERSIZE == msglen:
                #print("full msg with header", full_msg)
                full_msg = full_msg[HEADERSIZE:]
                cible = pickle.loads(full_msg)
                mesg_complet = True
                new_message = True
                full_msg = b""
            
            if len(full_msg)-HEADERSIZE > msglen:
                full_msg = b""
                new_message = True
            
        time.sleep(3)
        d = msg
        d = pickle.dumps(d)
        d = bytes(f"{len(d):<{HEADERSIZE}}", 'utf-8')+d
        #print(f"message",msg)
        s.send(d)

thr2= threading.Thread(target=clientext, args=(message1,cible1))
thr2.start()

def verify(m1,m2,c1,c2):
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
        print(m1,m2,c1,c2)

thr3= threading.Thread(target=verify, args=(message,message1,cible,cible1))
thr3.start()