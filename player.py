import pygame
from build import *
import threading
import time

#CONST
sprites=[]



class Player:
    def __init__(self,):
        self.argent=500
        
        self.mousePos=pygame.mouse.get_pos()
        self.mouseSTATE=pygame.mouse.get_pressed()

        self.menu=False

        self.a=False
        self.z=False
        self.e=False

        self.Ba=False
        self.Bz=False
        self.Be=False

        
        self.th1=threading.Thread(target=None)
        self.th2=threading.Thread(target=None)
        self.th3=threading.Thread(target=None)
        
    def add(self,build, var):
        var=True
        sprites.append(build)
        time.sleep(0.3)
        var=False








    def menu(self):
        pass

    def addshooter(self):
        if self.z:
            if self.mouseSTATE[0]:
                if self.Bz == False:
                    self.argent-=100
                    self.th1=threading.Thread(self.add(shooter(self.mousePos),self.Bz))
                    self.th1.start()
                    
    def addtrooper(self):
        if self.e:
            if self.mouseSTATE[0]:
                sprites.append(barracks(self.mousePos))
                self.argent-=150
                

    def addrecolteur(self):
        if self.a:
            if self.mouseSTATE[0]:
                sprites.append(recolteur(self.mousePos))
                self.argent-=300

    

    def update(self):
        self.mousePos=pygame.mouse.get_pos()
        self.mouseSTATE=pygame.mouse.get_pressed()
        self.addrecolteur()
        self.addshooter()
        self.addtrooper()
    
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            if self.argent>300:
                self.addrecolteur()

        if keys[pygame.K_z]:
            if self.argent>=100:
                self.z=True

        if keys[pygame.K_e]:
            if self.argent>150:
                self.e=True

        if keys[pygame.K_r]:
            self.menu()
            
    
    

        