import pygame
import random
import os
from player import *
import threading


pygame.init()

width = 500
height = 500
pygame.display.set_caption("MRTS")
win=pygame.display.set_mode((width,height), pygame.RESIZABLE)
backC=pygame.color.Color("#FFFFFF")



def draw(sprites):
    for i in range(len(sprites)):
        win.blit(sprites[i].img,sprites[i].rect)

for i in range(5):
    sprites.append(minerals(random.randint(0,1300),random.randint(0,200)))
    sprites.append(minerals(random.randint(0,1300),random.randint(300,700)))

player=Player()





def main():
    run = True
    clock = pygame.time.Clock()
    

    while run:
        clock.tick(60)
        win.fill(backC)
        player.update()
        
        draw(sprites)
        print(player.e)
        pygame.display.flip()
        player.move()
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        
main()
