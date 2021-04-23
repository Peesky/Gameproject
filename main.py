import pygame
import random
import os
from player import *
import threading
from client import *
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







def main():
    run = True
    otherbuilds=[]
    othersprites=[]
    thread = threading.Thread(target =startclient , args=(player.builds,otherbuilds))
    thread.start()


    clock = pygame.time.Clock()
    

    while run:
        clock.tick(60)
        win.fill(backC)
        
        equivalent(player.builds, player.sprites)
        equivalent(otherbuilds, othersprites)
        



        player.update()
        draw(player.sprites)
        #draw(sprites1)
        

        pygame.display.flip()
        player.move()
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        
main()
