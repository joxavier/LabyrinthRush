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
#Colors
black = (   0,   0,   0)
white = ( 255, 255, 255)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Labrynth Rush")
done = False
clock = pygame.time.Clock()
font = pygame.font.SysFont('Calibri', 50, True, False)
text = font.render("You Win!",True,BLACK)
listball = [0]
xpos = 350
ypos = 250

class Player(pygame.sprite.Sprite):
    moveX,moveY=0,0 #Players Initial Speed
    x, y = 0, 0 # Postion of Player
    flipSpeed = 10 #Speed of animation
    flipTime = 0
    currentImage=0 #Image animater
    walls = []
    #Get images 
    def __init__(self, x, y, blue):
        super(Player, self).__init__()
     
        # Load the images
        if blue: #Blue team
            self.right_image0 = pygame.image.load("blue_right_0.png")
            self.right_image1 = pygame.image.load("blue_right_1.png")
            self.left_image0 = pygame.image.load("blue_left_0.png")
            self.left_image1 = pygame.image.load("blue_left_1.png")
            self.straight = pygame.image.load("blue.png")
        else: #Red team
            self.right_image0 = pygame.image.load("red_right_0.png")
            self.right_image1 = pygame.image.load("red_right_1.png")
            self.left_image0 = pygame.image.load("red_left_0.png")
            self.left_image1 = pygame.image.load("red_left_1.png")
            self.straight = pygame.image.load("red.png")

        # Select 2 images for the animation    
        self.image0 = self.straight
        self.image1 = self.straight
        self.image = self.image0
        #Make them Sprites
        self.rect = self.image0.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Set our transparent color
        self.image0.set_colorkey(white)
        self.image1.set_colorkey(white)

        self.x = x
        self.y = y

    def move(self):        
        # Move the player
        self.x += self.moveX
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            
            if self.moveX > 0:
                self.rect.right = block.rect.left
            elif self.moveX ==  0:
                self.moveX = self.moveX
            else:               
                self.rect.left = block.rect.right
                self.rect.y += self.moveY
 
        
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:

            if self.moveY > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

    def update(self):
        self.flipTime += 1
        if (self.flipTime == self.flipSpeed):
            if (self.currentImage==0):
                self.currentImage=1
            else:
                self.currentImage=0
            if (self.currentImage==0):
                self.image = self.image0
            else:
                self.image = self.image1 
            self.flipTime=0 #Reset timer

        #self.draw()
        
    """def draw(self):
        if (self.currentImage==0):
            screen.blit(self.image0, (self.x,self.y))
        else:
            screen.blit(self.image1, (self.x,self.y))"""
            
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
                "hi"
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
player1 = Player(100, 100, True)
player2 = Player(10, 210, True)
player3 = Player(10, 410, True)
player4 = Player(500, 300, False)


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
player1.walls = wallList
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


        if (event.type==pygame.KEYDOWN):
            if (event.key==pygame.K_LEFT):
                player1.moveX = -3
                player1.image0 = player1.left_image0
                player1.image1 = player1.left_image1
                
            if (event.key==pygame.K_RIGHT):
                player1.moveX= 3
                player1.image0 = player1.right_image0
                player1.image1 = player1.right_image1

            if (event.key==pygame.K_UP):
                player1.moveY = -3
                player1.image0 = player1.straight
                player1.image1 = player1.straight
                
            if (event.key==pygame.K_DOWN):
                player1.moveY = 3
                player1.image0 = player1.left_image0
                player1.image1 = player1.left_image1

        if (event.type==pygame.KEYUP):
            player1.image0 = player1.straight
            player1.image1 = player1.straight
            if (event.key==pygame.K_LEFT):
                player1.moveX=0
                #player1.image0 = player1.straight
                #player1.image1 = player1.straight
            if (event.key==pygame.K_RIGHT):
                player1.moveX=0
                #player1.image0 = player1.right_image1
                #player1.image1 = player1.right_image1

            if (event.key==pygame.K_UP):
                player1.moveY=0

                #player1.image0 = player1.right_image1
                #player1.image1 = player1.right_image1
                
            if (event.key==pygame.K_DOWN):
                player1.moveY=0
                #player1.image0 = player1.left_image1
                #player1.image1 = player1.left_image1
            
    #screen.fill(white)
    


    #Move Player
    player1.rect.x += player1.moveX
    player1.rect.y += player1.moveY
    #Update Player
    player1.update()
    player2.update()
    player3.update()
    player4.update()
    
    wallList.draw(screen)
    mario.rect.x += mario.xspd
    mario.rect.y += mario.yspd
    mario.update()
    
    spriteList.add(mario)
    spriteList.add(player1)
    #wallList.draw(screen)
    spriteList.draw(screen)
    player1.move()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
