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
    speed = "off"
    timer = 0
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
        #self.image0.set_colorkey(white)
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

        power_hit_list = pygame.sprite.spritecollide(self, powerList, True)
        for power in power_hit_list:
            if power.name == "speed":
                self.speed = "on"
                
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
    def draw(self,x,y):
        self.rect.x = x
        self.rect.y = y
        wallList.add(wall)


class PowerUp(pygame.sprite.Sprite):
    name = ""
    def __init__(self, x, y, name, pic):
        super(PowerUp, self).__init__()
        self.name = name
        pygame.sprite.Sprite
        self.xpos = x
        self.ypos = y
        self.image = pygame.image.load(pic).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
player1 = Player(200, 200, True)
player2 = Player(10, 210, True)
player3 = Player(10, 410, True)
player4 = Player(500, 300, False)


wallList = pygame.sprite.Group()
for wall1 in range (0,1088,16):
    wall = Wall(wall1,0)
    wall.draw(wall1,0)
    
    wall = Wall(wall1,704)
    wall.draw(wall1,704)
    
for wall2 in range (16,704,16):
    wall = Wall(0,wall2)
    wall.draw(0,wall2)
    
    wall = Wall(1072,wall2)
    wall.draw(1072,wall2)

for wall3 in range (64,304,16):
    wall = Wall(64,wall3)
    wall.draw(64,wall3)

for wall4 in range (80,208,16):
    wall = Wall(wall4,64)
    wall.draw(wall4,64)
    
for wall5 in range (384,624,16):
    # Loop for 3 columns
    for wall5A in range (64,112,16):
        wall = Wall(wall5A,wall5)
        wall.draw(wall5A,wall5)

for wall6 in range (112,416,16):
    # Loop for 2 rows
    for wall6A in range (576,612,16):
        wall = Wall(wall6,wall6A)
        wall.draw(wall6,wall6A)

for wall7 in range (272,416,16):
    #Loop for x rows
    for wall7A in range (608,704,16):
        wall = Wall(wall7,wall7A)
        wall.draw(wall7,wall7A)




for wall51 in range (300,620,16):
    wall = Wall(wall51,65)
    wall.draw(wall51,65)

for wall52 in range (710,918,16):
    # Loop for 4 rows
    for wall52A in range (80,144,16):
        wall = Wall(wall52,wall52A)
        wall.draw(wall52,wall52A)

player1.walls = wallList
wings = PowerUp(85, 85, "speed", "speed.png")

while not done:
    pygame.FULLSCREEN 
    screen.fill(WHITE)
   
    powerList = pygame.sprite.Group()
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
    
        if (event.type==pygame.KEYDOWN):
            if (event.key==pygame.K_LEFT):
                if player1.speed == "on":
                    player1.moveX = -10
                else:
                    player1.moveX = -3
                player1.image0 = player1.left_image0
                player1.image1 = player1.left_image1
                
            if (event.key==pygame.K_RIGHT):
                if player1.speed == "on":
                    player1.moveX = 10
                else:
                    player1.moveX= 3
                player1.image0 = player1.right_image0
                player1.image1 = player1.right_image1

            if (event.key==pygame.K_UP):
                if player1.speed == "on":
                    player1.moveY = -10
                else:
                    player1.moveY = -3
                player1.image0 = player1.straight
                player1.image1 = player1.straight
                
            if (event.key==pygame.K_DOWN):
                if player1.speed == "on":
                    player1.moveY = 10
                else:
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
    if player1.speed == "on":
        player1.timer += 1
    if player1.timer == 5:
        player1.speed == "off" 


    #Move Player
    player1.rect.x += player1.moveX
    player1.rect.y += player1.moveY
    #Update Player
    player1.update()
    player2.update()
    player3.update()
    player4.update()
    powerList.add(wings)
    wallList.draw(screen)
    spriteList.add(player1)
    spriteList.draw(screen)
    powerList.draw(screen)
    player1.move()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
