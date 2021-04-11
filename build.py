import pygame
import random

#CONST:
adresse="IMG/equipe_B"


def color():
    clt=random.randint(1,2)
    if clt==1:
        adresse="IMG/equipe_B"
    else:
        adresse="IMG/equipe_R"


class build(pygame.sprite.Sprite):
    def __init__(self,life, adresse,mousePos):
        super().__init__()
        self.life=life
        
        self.img=pygame.transform.scale(pygame.image.load(adresse),(50,50))
        
        self.x=mousePos[0]
        self.y=mousePos[1]
        
        self.rect=self.img.get_rect()
        self.rect.x=self.x
        self.rect.y=self.y

         

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
        self.img=pygame.transform.scale(pygame.image.load("IMG/minerals.png"),(75,75))
        self.x=x
        self.y=y
        self.rect=self.img.get_rect()
        self.rect.x=self.x
        self.rect.y=self.y





"""
tourner une image sur son centre
def rot_center(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image
    """