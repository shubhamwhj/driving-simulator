import pygame, sys,random

pygame.init()
pygame.mixer.init()

clock=pygame.time.Clock()
width=780
height=360
screen = pygame.display.set_mode((width,height))
  
#load the images in dict
images={}
images["bg"] = pygame.image.load("bg.png").convert_alpha()
images["car"] = pygame.image.load("car1.png").convert_alpha()
groundx=0

class Vehicle:
    rect= pygame.Rect(100,200,30,30)
   
    def display(self):
        screen.blit(images["car"],self.rect) 
        
    def moveLeft(self):
        self.rect.y=self.rect.y-100
        
    def moveRight(self):
        self.rect.y=self.rect.y+100
        
    
car=Vehicle()

while True:    
    screen.fill((50,150,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit() 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car.moveLeft()
            if event.key == pygame.K_RIGHT:
                car.moveRight()
                        
    
    groundx=groundx-5
    if(groundx < -190):
        groundx=0
   
    
    screen.blit(images["bg"],[groundx,0]) 
    car.display() 
    
    
    pygame.display.update()
    clock.tick(30) 