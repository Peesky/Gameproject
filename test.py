import socket
import time
import pickle
import threading
threads = []

def client(clientsocket):
    listerecue=[]
    HEADERSIZE = 10
    while True:
        d = ["a","b","c","d","e","f"]
        msg = pickle.dumps(d)
        msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
        print(msg)
        clientsocket.send(msg)
        time.sleep(3)

        full_msg=b""
        new_message=True
        mesg_complet =False
        print(listerecue)


        while not mesg_complet:
            msg = clientsocket.recv(32)
            if new_message:
                msglen = int(msg[:HEADERSIZE])
                print("new msg len:",msglen)
                new_message = False
            
            full_msg+=msg
            
            if len(full_msg)-HEADERSIZE == msglen:
                full_msg = full_msg[HEADERSIZE:]
                listerecue = pickle.loads(full_msg)
                mesg_complet = True
                new_message = True
                full_msg = b""


def start():
    HEADERSIZE = 10
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 1243))
    s.listen(2)
    
    while True:
        print("en ecoute")
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established.")
        thread = threading.Thread(target=client, args=(clientsocket,))
        thread.start()
        threads.append(thread)
            

start()