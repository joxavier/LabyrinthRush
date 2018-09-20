import pygame
import time
import random
import math
pygame.init()


BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
DBLUE    = (   0,  76, 255)
YELLOW   = (  255, 221, 0)

PI = 3.141592653
ite = 0
size = (1080, 720)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Labrynth Rush")
done = False
clock = pygame.time.Clock()
font = pygame.font.SysFont('Calibri', 50, True, False)
text = font.render("You Win!",True,BLACK)
listball = [0]
xpos = 350
ypos = 250
class Character(pygame.sprite.Sprite):
    xspd = ""
    yspd = ""
    walls = ""
    def __init__(self,x,y):
        super(Character, self).__init__()
        pygame.sprite.Sprite
        self.image = pygame.image.load("mario.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.xspd = 0
        self.yspd = 0
    def update(self):
        
        
        self.rect.x += self.xspd
 
        block_hit_list = pygame.sprite.spritecollide(self, wallList, False)
        for block in block_hit_list:
            
            if self.xspd > 0:
                self.rect.right = block.rect.left
            elif self.xspd ==  0:
                self.xspd = self.xspd
            else:
               
                self.rect.left = block.rect.right
 
       
        self.rect.y += self.yspd
 
        
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:

            if self.yspd > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

class Wall(pygame.sprite.Sprite):
    xpos = ""
    ypos = ""

    def __init__(self, x, y):
        super(Wall, self).__init__()
        pygame.sprite.Sprite
        self.xpos = x
        self.ypos = y
        self.image = pygame.image.load("wall11.png").convert()
        self.rect = self.image.get_rect()
    def draw(self):
        screen.blit(self.img, [self.xpos, self.ypos])

mario = Character(350, 250)


wallList = pygame.sprite.Group()
for i in range (0,1080, 16):
    wall = Wall(i,0)
    wall.rect.x = i
    wall.rect.y = 0
    wallList.add(wall)
    
    wall = Wall(i,704)
    wall.rect.x = i
    wall.rect.y = 704
        
    wallList.add(wall)
    
for j in range (16,704, 16):
    wall = Wall(0,j)
    wall.rect.x = 0
    wall.rect.y = j
    wallList.add(wall)
    
    wall = Wall(1064,j)
    wall.rect.x = 1064
    wall.rect.y = j
    wallList.add(wall)

for k in range (14):
    wall = Wall(70,65 + (k*16))
    wall.rect.x = 70
    wall.rect.y = 65 +k*16
    wallList.add(wall)

mario.walls = wallList
while not done:
    pygame.FULLSCREEN 
    screen.fill(WHITE)
   
    
    spriteList = pygame.sprite.Group()
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True
        elif pygame.mouse.get_pressed()[0] == True:
            mouse_position = pygame.mouse.get_pos()
            mouse_x = mouse_position[0]
            mouse_y = mouse_position[1]
            print mouse_x,mouse_y
    
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                 mario.xspd = -2
            elif event.key == pygame.K_RIGHT:
                 mario.xspd = 2
            elif event.key == pygame.K_UP:
                 mario.yspd = -2
            elif event.key == pygame.K_DOWN:
                 mario.yspd = 2
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                 mario.xspd = 0
            elif event.key == pygame.K_RIGHT:
                 mario.xspd = 0
            elif event.key == pygame.K_UP:
                 mario.yspd = 0
            elif event.key == pygame.K_DOWN:
                 mario.yspd = 0
    wallList.draw(screen)
    mario.rect.x += mario.xspd
    mario.rect.y += mario.yspd
    mario.update()
    
    spriteList.add(mario)
    #wallList.draw(screen)
    spriteList.draw(screen)
    pygame.display.flip()
    clock.tick(65)
pygame.quit()
