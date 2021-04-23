import pygame
from build import *
import threading
import time
from client import *



class Player:
    def __init__(self,):
        


        self.id=0
        self.argent=500
        self.sprites=[]
        self.builds=[]
        
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
        self.builds.append(build)
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
                    self.z=False
                    
    def addtrooper(self):
        if self.e:
            if self.mouseSTATE[0]:
                self.argent-=150
                if self.Be == False:
                    self.argent-=100
                    self.th1=threading.Thread(self.add(barracks(self.mousePos),self.Be))
                    print("ok")
                    self.th1.start()
                    self.e=False
                
    def addrecolteur(self):
        if self.a:
            if self.mouseSTATE[0]:
                self.argent-=300
                if self.Ba == False:
                    self.th1=threading.Thread(self.add(recolteur(self.mousePos),self.Ba))
                    self.th1.start()
                    self.a=False
                

    

    def update(self):
        self.mousePos=pygame.mouse.get_pos()
        self.mouseSTATE=pygame.mouse.get_pressed()
        self.addrecolteur()
        self.addshooter()
        self.addtrooper()
    
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            if self.argent>=300 and not self.z and not self.e:
                self.a=True

        if keys[pygame.K_z] and not self.a and not self.e:
            if self.argent>=100:
                self.z=True

        if keys[pygame.K_e] and not self.z and not self.a:
            if self.argent>=150:
                self.e=True

        if keys[pygame.K_r]:
            self.menu()
            
    
    

        