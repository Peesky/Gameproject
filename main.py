import pygame
import random
import os
from player import *
import threading
import pickle


pygame.init()

width = 500
height = 500
pygame.display.set_caption("MRTS")
win=pygame.display.set_mode((width,height), pygame.RESIZABLE)
backC=pygame.color.Color("#FFFFFF")

player=Player()


def equivalent(builds,sprites):
    nbb = len(builds)
    nbs = len(sprites)
    dif = nbb-nbs
    compteur = 0 
    for i in range(dif):
        sprites.append(sprite(builds[-(dif-compteur)]))
        compteur+=1
    for i in range(len(sprites)):
        sprites[i].build=builds[i]
    



def draw(sprites):
    for i in range(len(sprites)):
        win.blit(sprites[i].img,sprites[i].rect)

for i in range(5):
    player.builds.append(minerals(random.randint(0,1300),random.randint(300,650)))



def client(clientsocket, ):
    HEADERSIZE = 10
    def envoyer():
        while True:
            global player
            d = player.builds
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
                    global player
                    player.otherbuilds = full_msg
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
        

def clientext():
    HEADERSIZE = 10
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 1243))
    def envoyer():
        while True:
            global player
            d=player.builds
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
                    global player
                    player.otherbuilds = pickle.loads(full_msg)
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
        

def verify():
    global player
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
        print(player.builds,player.otherbuilds)

thr3= threading.Thread(target=verify)
thr3.start()


def menu():
    i=input("host?")
    if i=="y":
        thr= threading.Thread(target=start)
        thr.start()
    else:
        thr2= threading.Thread(target=clientext)
        thr2.start()



def main():
    menu()
    run = True

    clock = pygame.time.Clock()
    red=(255,0,0)
    blue=(0,0,255)
    while run:
        clock.tick(60)
        win.fill(backC)
        pygame.draw.rect(win,red,player.rect)
        pygame.draw.rect(win,blue,player.otherrect)

        equivalent(player.builds, player.sprites)
        equivalent(player.otherbuilds, player.othersprites)
        



        player.update()
        draw(player.sprites)
        draw(player.othersprites)
        #draw(sprites1)
        

        pygame.display.flip()
        player.move()
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        
main()
