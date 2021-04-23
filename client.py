import socket
import pickle
import time

def startclient(msg,cible):
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
                new_message = False
            
            full_msg+=msg
            
            if len(full_msg)-HEADERSIZE == msglen:
                full_msg = full_msg[HEADERSIZE:]
                cible += pickle.loads(full_msg)
                print(cible)
                del cible[::-2]
                mesg_complet = True
                new_message = True
                full_msg = b""
        
        d = msg
        msg = pickle.dumps(d)
        msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
        s.send(msg)
        time.sleep(0.002)

