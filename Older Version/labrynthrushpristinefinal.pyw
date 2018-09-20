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
size = (1238, 720)


screen = pygame.display.set_mode(size)
pygame.display.set_caption("Labrynth Rush")
done = False
clock = pygame.time.Clock()

#TEXT
font = pygame.font.SysFont('Calibri', 40, True, False)
text = font.render("You Win!",True,BLACK)

listball = [0]
xpos = 350
ypos = 250

whoosh = pygame.mixer.Sound("whoosh.ogg")
ghost = pygame.image.load("ghost.png")

class Player(pygame.sprite.Sprite):
    moveX,moveY=0,0 #Players Initial Speed
    x, y = 0, 0 # Postion of Player
    speed = 0
    flipSpeed = 10 #Speed of animation
    flipTime = 0
    currentImage=0 #Image animater
    walls = []
    tagger = False
    score = 50
    stimer = 0
    gtimer = 0
    speedon = "off"
    ghost = "off"
    #Get images 
    def __init__(self, x, y, tagger):
        super(Player, self).__init__()
     
        # Load the images
        if not tagger: #Blue team
            self.right_image0 = pygame.image.load("blue_right_0.png")
            self.right_image1 = pygame.image.load("blue_right_1.png")
            self.left_image0 = pygame.image.load("blue_left_0.png")
            self.left_image1 = pygame.image.load("blue_left_1.png")
            self.straight = pygame.image.load("blue.png")
            self.speed = 3
        elif tagger: #Red team
            self.right_image0 = pygame.image.load("red_right_0.png")
            self.right_image1 = pygame.image.load("red_right_1.png")
            self.left_image0 = pygame.image.load("red_left_0.png")
            self.left_image1 = pygame.image.load("red_left_1.png")
            self.straight = pygame.image.load("red.png")
            self.speed = 3.5
            self.tagger = True
            self.score += 1
        # Select 2 images for the animation    
        self.image0 = self.straight
        self.image1 = self.straight

        self.image = self.image0

        #Make them Sprites
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.x = x
        self.y = y

    def move(self):        
        # Move the player
        if self.ghost != "on":
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
                self.speedon = "on"
                self.speed = 5
                whoosh.play()
            elif power.name == "ghost":
                self.ghost = "on"

    def control(self, pressed, key):
        if pressed:
            if (key == "LEFT"):
                self.moveX = -1*(self.speed)
                print self.moveX
                self.image0 = self.left_image0
                self.image1 = self.left_image1
                    
            if (key == "RIGHT"):
                self.moveX= 1*(self.speed)
                print self.moveX
                self.image0 = self.right_image0
                self.image1 = self.right_image1

            if (key == "UP"):
                self.moveY = -1*(self.speed)
                self.image0 = self.straight
                self.image1 = self.straight
                    
            if (key == "DOWN"):
                self.moveY = 1*(self.speed)
                self.image0 = self.straight
                self.image1 = self.straight

        if not pressed:
            if (key == "LEFT"):
                self.moveX = 0
                self.image0 = self.straight
                self.image1 = self.straight
                    
            if (key == "RIGHT"):
                self.moveX= 0
                self.image0 = self.straight
                self.image1 = self.straight

            if (key == "UP"):
                self.moveY = 0
                self.image0 = self.straight
                self.image1 = self.straight
                    
            if (key == "DOWN"):
                self.moveY = 0
                self.image0 = self.straight
                self.image1 = self.straight

    def update(self):
        self.flipTime += 1
        
        if (self.flipTime == self.flipSpeed):
            if (self.currentImage==0):
                self.image = self.image0
                self.currentImage=1
            else:
                self.image = self.image1
                self.currentImage=0
            self.flipTime=0 #Reset timer
            self.image.set_colorkey(WHITE) #Clear Background

        if self.speedon == "on":
            self.stimer += 1
        if self.stimer == 35:
            self.speedon = "off"
            self.stimer = 0
            self.speed = 3
        if self.ghost == "on":
            self.gtimer += 1
        if self.gtimer == 20:
            self.ghost = "off"
            self.gtimer = 0
    def getScore (self):
        if self.tagger:
            self.score -= 0.016
        elif not self.tagger:
            self.score += 0.016

            
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
        
player1 = Player(100, 100, True)
player2 = Player(100, 210, False)
player3 = Player(100, 410, False)
player4 = Player(500, 300, False)


wallList = pygame.sprite.Group()
#powerList = pygame.sprite.Group()
playerList = pygame.sprite.Group()

# Draw all walls
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
player2.walls = wallList
player3.walls = wallList
player4.walls = wallList
wings = PowerUp(85, 85, "speed", "speed.png")
ghost = PowerUp(300, 300, "ghost", "ghost.png")

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
            
        # PLAYER 1
        if (event.type==pygame.KEYDOWN):
            if (event.key==pygame.K_LEFT):
                player1.control(True, "LEFT")
                
            if (event.key==pygame.K_RIGHT):
                player1.control(True, "RIGHT")

            if (event.key==pygame.K_UP):
                player1.control(True, "UP")
                
            if (event.key==pygame.K_DOWN):
                player1.control(True, "DOWN")

        if (event.type==pygame.KEYUP):
            if (event.key==pygame.K_LEFT):
                player1.control(False, "LEFT")
                
            if (event.key==pygame.K_RIGHT):
                player1.control(False, "RIGHT")
                
            if (event.key==pygame.K_UP):
                player1.control(False, "UP")
                
            if (event.key==pygame.K_DOWN):
                player1.control(False, "DOWN")
       
        # PLAYER 2
        if (event.type==pygame.KEYDOWN):
            if (event.key==pygame.K_a):
                player2.control(True, "LEFT")
                
            if (event.key==pygame.K_d):
                player2.control(True, "RIGHT")

            if (event.key==pygame.K_w):
                player2.control(True, "UP")
                
            if (event.key==pygame.K_s):
                player2.control(True, "DOWN")

        if (event.type==pygame.KEYUP):
            if (event.key==pygame.K_a):
                player2.control(False, "LEFT")
                
            if (event.key==pygame.K_d):
                player2.control(False, "RIGHT")
                
            if (event.key==pygame.K_w):
                player2.control(False, "UP")
                
            if (event.key==pygame.K_s):
                player2.control(False, "DOWN")

        # PLAYER 3
        if (event.type==pygame.KEYDOWN):
            if (event.key==pygame.K_KP4):
                player3.control(True, "LEFT")
                
            if (event.key==pygame.K_KP6):
                player3.control(True, "RIGHT")

            if (event.key==pygame.K_KP8):
                player3.control(True, "UP")
                
            if (event.key==pygame.K_KP5):
                player3.control(True, "DOWN")

        if (event.type==pygame.KEYUP):
            if (event.key==pygame.K_KP4):
                player3.control(False, "LEFT")
                
            if (event.key==pygame.K_KP6):
                player3.control(False, "RIGHT")
                
            if (event.key==pygame.K_KP8):
                player3.control(False, "UP")
                
            if (event.key==pygame.K_KP5):
                player3.control(False, "DOWN")
       
        # PLAYER 4
        if (event.type==pygame.KEYDOWN):
            if (event.key==pygame.K_j):
                player4.control(True, "LEFT")
                
            if (event.key==pygame.K_l):
                player4.control(True, "RIGHT")

            if (event.key==pygame.K_i):
                player4.control(True, "UP")
                
            if (event.key==pygame.K_k):
                player4.control(True, "DOWN")

        if (event.type==pygame.KEYUP):
            if (event.key==pygame.K_j):
                player4.control(False, "LEFT")
                
            if (event.key==pygame.K_l):
                player4.control(False, "RIGHT")
                
            if (event.key==pygame.K_i):
                player4.control(False, "UP")
                
            if (event.key==pygame.K_k):
                player4.control(False, "DOWN")
    #Score
    player1.getScore()
    player2.getScore()
    player3.getScore()
    player4.getScore()
    
    #Scoreboard
    scoreBoard = pygame.image.load("scoreBoard.png")
    screen.blit(scoreBoard, (1088,0))

    #Display the scores
    player1Score = font.render(str(int(player1.score)),True,BLACK)
    screen.blit(player1Score, [1148, 60])
    
    player2Score = font.render(str(int(player2.score)),True,BLACK)
    screen.blit(player2Score, [1148, 200])
    
    player3Score = font.render(str(int(player3.score)),True,BLACK)
    screen.blit(player3Score, [1148, 340])
    
    player4Score = font.render(str(int(player4.score)),True,BLACK)
    screen.blit(player4Score, [1148, 480])

    #Move Player
    #Player 1            
    player1.rect.x += player1.moveX
    player1.rect.y += player1.moveY

    #Player 2
    player2.rect.x += player2.moveX
    player2.rect.y += player2.moveY

    #Player 3          
    player3.rect.x += player3.moveX
    player3.rect.y += player3.moveY

    #Player 4
    player4.rect.x += player4.moveX
    player4.rect.y += player4.moveY
    
    #Update Player
    player1.update()
    player2.update()
    player3.update()
    player4.update()
    
    # Add to list
    spriteList.add(player1)
    spriteList.add(player2)
    spriteList.add(player3)
    spriteList.add(player4)
    powerList.add(wings)
    powerList.add(ghost)
    wallList.draw(screen)
    spriteList.draw(screen)
    powerList.draw(screen)

    # Move Players
    player1.move()
    player2.move()
    player3.move()
    player4.move()
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
