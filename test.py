import pygame
import random
pygame.init()

width = 500
height = 500
pygame.display.set_caption("MRTS")
win=pygame.display.set_mode((width,height), pygame.RESIZABLE)
backC=pygame.color.Color("#FFFFFF")


sprites=[]

class minerals:
    def __init__(self,x,y):
        self.img=pygame.transform.scale(pygame.image.load("IMG/minerals.png"),(75,75))
        self.x=x
        self.y=y
        self.rect=self.img.get_rect()
        self.rect.x=self.x
        self.rect.y=self.y

def move():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        print("a")
        addshooter()

    if keys[pygame.K_RIGHT]:
        print("z")
    if keys[pygame.K_e]:
        print("e")

    if keys[pygame.K_r]:
        print("r")
              
def addshooter():
    sprites.append(minerals(100,100))

        
        

def draw(sprites):
    for i in range(len(sprites)):
        win.blit(sprites[i].img,sprites[i].rect)

def main():
    run = True
    clock = pygame.time.Clock()
    

    while run:
        clock.tick(60)
        win.fill(backC)
        move()
        draw(sprites)
        
    
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
main()