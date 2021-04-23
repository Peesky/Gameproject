import pygame
import random

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
    def __init__(self,mousePos):
        self.adresse=adresse+"/shooter.png"
        super().__init__(200,self.adresse,mousePos)

class recolteur(build):
    def __init__(self,mousePos):
        self.adresse=adresse+"/recolteur.png"
        super().__init__(500,self.adresse,mousePos)

class barracks(build):
    def __init__(self,mousePos):
        self.adresse=adresse+"/trooper.png"
        super().__init__(350,self.adresse,mousePos)
        
class minerals:
    def __init__(self,x,y):
        self.adresse = "IMG/minerals.png"
        self.imgsize = (75,75)

        self.x=x
        self.y=y



class sprite(pygame.sprite.Sprite):
    def __init__(self,build):
        super().__init__()
        self.build=build

        self.img=pygame.transform.scale(pygame.image.load(self.build.adresse),self.build.imgsize)

        self.rect=self.img.get_rect()
        self.rect.x=self.build.x
        self.rect.y=self.build.y
    