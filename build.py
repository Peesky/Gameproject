import pygame
import random
import threading
import time

#CONST:
"""
adresse="IMG/equipe_B"
"""

def color():
    clt=random.randint(1,2)
    if clt==1:
        adresse="IMG/equipe_B"
    else:
        adresse="IMG/equipe_R"
    return adresse
adresse =color()




class build():
    def __init__(self,life, adresse,mousePos):
        
        self.life=life
        self.imgsize=(50,50)
        self.adresse=adresse
        
        self.x=mousePos[0]
        self.y=mousePos[1]
                 

class shooter(build):
    def __init__(self,mousePos,listeA):
        self.adresse=adresse+"/shooter.png"
        super().__init__(200,self.adresse,mousePos)
        #print("LISTE SPE",listeA)
        #self.thread=threading.Thread(target=self.shoot, args = (listeA,))
        #self.thread.start()


    
    def shoot(self,listeA):
        print("LISTE SPE",listeA)
        listeA.append(bullet(self.x+20,self.y))
        time.sleep(2)



class recolteur(build):
    def __init__(self,mousePos):
        self.adresse=adresse+"/recolteur.png"
        super().__init__(500,self.adresse,mousePos)

class barracks(build):
    def __init__(self,mousePos):
        self.adresse=adresse+"/trooper.png"
        super().__init__(350,self.adresse,mousePos)
    
    #def testlowlife(self):

        
class minerals:
    def __init__(self,x,y):
        self.adresse = "IMG/minerals.png"
        self.imgsize = (75,75)
        self.x=x
        self.y=y

class bullet():
    def __init__(self,x,y):
        self.adresse = "IMG/equipe_B/bullet.png"
        self.imgsize = (20,20)
        self.x=x
        self.y=y
        self.vel=-5
        self.ydebase=y
        self.life=3
        
        self.thread=0
        
        self.run = False   
        #self.threads=[[self.alive,(),"vide",False]]
        
        

    def alive(self):
        self.run = True
        self.y+=self.vel
        print("ok")
        self.run=False
        
             
            
        


class sprite(pygame.sprite.Sprite):
    def __init__(self,build):
        super().__init__()
        self.build=build

        self.img=pygame.transform.scale(pygame.image.load(self.build.adresse),self.build.imgsize)

        self.rect=self.img.get_rect()
        self.rect.x=self.build.x
        self.rect.y=self.build.y
    def update(self):
        self.rect=self.img.get_rect()
        self.rect.x=self.build.x
        self.rect.y=self.build.y

    