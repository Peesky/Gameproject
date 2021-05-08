import pygame

pygame.init()

width = 500
height = 500
pygame.display.set_caption("MRTS")
win=pygame.display.set_mode((width,height), pygame.RESIZABLE)
backC=pygame.color.Color("#FFFFFF")

class poy:
    def __init__(self):
        self.rect=pygame.Rect(0,0,1366,360)
        self.reccoo=[0,1366,0,360]
        self.mousePos=pygame.mouse.get_pos()
    
    def update(self):
        self.mousePos=pygame.mouse.get_pos()

    def verify(self):
        if self.reccoo[0]<self.mousePos[0]<self.reccoo[1] and self.reccoo[2]<self.mousePos[1]<self.reccoo[3] :
            print("youhooo")
        else:
            print("nooooo")
            print(self.mousePos)
            print(self.reccoo)

player=poy()
def main():
    
    run = True

    clock = pygame.time.Clock()
    red=(255,0,0)
    blue=(0,0,255)
    while run:
        clock.tick(60)
        win.fill(backC)
        pygame.draw.rect(win,red,player.rect)
        
        pygame.display.flip()
        player.update()
        player.verify()
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        
        
main()