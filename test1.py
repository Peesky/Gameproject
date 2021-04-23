import socket
import pickle
import time

def startclient():
    HEADERSIZE = 10
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 1243))
    listerecue=[]
    while True:
        full_msg=b""
        new_message=True
        mesg_complet =False
        print(listerecue)


        while not mesg_complet:
            msg = s.recv(32)
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
        
        d = ["a","b","c","d","e","f"]
        msg = pickle.dumps(d)
        msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
        print(msg)
        s.send(msg)
        time.sleep(3)

startclient()