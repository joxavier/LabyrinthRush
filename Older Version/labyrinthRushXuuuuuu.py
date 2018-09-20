# Import and initialize pygame
import pygame
pygame.init()

# Define subprograms
def room_menu():   
    # Define colors
    BLACK    = (   0,   0,   0)
    WHITE    = ( 255, 255, 255)
    RED      = ( 255,   0,   0)

    # Set the width and height of the screen [width, height]
    size = (1238, 720)
    screen = pygame.display.set_mode((1238, 720))
     
    pygame.display.set_caption("Labyrinth Rush")
     
    # Loop until the user clicks the close button
    done = False
     
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    
    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop        
        screen.fill(BLACK)

        # Load menu screen
        menu_background = pygame.image.load("menu0.png")
        screen.blit(menu_background, (0,0))
        pygame.display.flip()

        # Get coordinates when user clicks
        mouse_position = pygame.mouse.get_pos()
        mouse_x = mouse_position[0]
        mouse_y = mouse_position[1]

        # User did something
        for event in pygame.event.get():
            
            # If user clicked close
            if event.type == pygame.QUIT:
                # Flag that we are done so we exit this loop
                done = True

            # Based on where user clicked, this will later take user to different screen
            elif (pygame.mouse.get_pressed()[0] == True):
                if (mouse_x > 314 and mouse_x < 913 and mouse_y > 216 and mouse_y < 395):
                    room_game()
                    done = True

                elif (mouse_x > 314 and mouse_x < 604 and mouse_y > 413 and mouse_y < 496):
                    room_controls()
                    done = True

                elif (mouse_x > 621 and mouse_x < 912 and mouse_y > 412 and mouse_y < 498):
                    done = True

        # Limit to 60 frames per second
        clock.tick(60)
        
    # Close the window and quit.
    pygame.quit()


def room_controls():
    # Define colors
    BLACK    = (   0,   0,   0)
    WHITE    = ( 255, 255, 255)
    RED      = ( 255,   0,   0)

    # Set the width and height of the screen [width, height]
    size = (1238, 720)
    #screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    screen = pygame.display.set_mode((1238, 720))
     
    pygame.display.set_caption("Labyrinth Rush")
     
    # Loop until the user clicks the close button
    done = False
     
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    
    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop        
        # Make screen black
        screen.fill(BLACK)

        # Load the controls screen
        controls_background = pygame.image.load("Controls.png")
        screen.blit(controls_background, (0,0))
        pygame.display.flip()

        # Get coordinates when user clicks
        mouse_position = pygame.mouse.get_pos()
        mouse_x = mouse_position[0]
        mouse_y = mouse_position[1]

        # User did something
        for event in pygame.event.get():
            
            # If user clicked close
            if event.type == pygame.QUIT:
                # Flag that we are done so we exit this loop
                done = True

            # Based on where user clicked, this will later take user to different screen          
            elif (pygame.mouse.get_pressed()[0] == True):
                if (mouse_x > 17 and mouse_x < 247 and mouse_y > 18 and mouse_y < 83):
                    room_menu()
                    done = True

                if (mouse_x > 981 and mouse_x < 1218 and mouse_y > 13 and mouse_y < 83):
                    room_game()
                    done = True
                    
        # Limit to 60 frames per second    
        clock.tick(60)

def room_game():
    # Define colours
    BLACK    = (   0,   0,   0)
    WHITE    = ( 255, 255, 255)

    # Set the width and height of the screen [width, height]
    size = (1238, 720)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Labyrinth Rush")
    
    # Loop until the user clicks the close button
    done = False
     
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Display text
    font = pygame.font.SysFont('Calibri', 40, True, False)
    font_time = pygame.font.SysFont('Calibri', 60, True, False)
    font2 = pygame.font.SysFont('Calibri', 30, True, False)
    
    # Set game timer
    minute = 2
    sec = 59

    # Import powerup and sound effect
    whoosh = pygame.mixer.Sound("whoosh.ogg")
    ghost = pygame.image.load("ghost.png")

    # Create class of player
    class Player(pygame.sprite.Sprite):

        # List attributes of player
        playerNum = 0 #########Craig what is this
        playerHeader = "" ######## Craig....
        moveX,moveY=0,0 #Players Initial Speed
        x, y = 0, 0 # Postion of Player
        startx = 0 ## CRAIG be descriptive and make the variables have meaning
        starty = 0  ###
        speed = 0
        flipSpeed = 10 #Speed of animation
        flipTime = 0
        currentImage=0 #Image animater
        walls = []
        tagger = False
        score = 50
        speedTimer = 0
        ghostTimer = 0
        speedon = "off"
        ghost = "off"
        
        #Get images 
        def __init__(self, x, y, tagger, header, playerNumber):
            super(Player, self).__init__()
         
            # Load the images for blue team
            if not tagger:
                self.right_image0 = pygame.image.load("blue_right_0.png")
                self.right_image1 = pygame.image.load("blue_right_1.png")
                self.left_image0 = pygame.image.load("blue_left_0.png")
                self.left_image1 = pygame.image.load("blue_left_1.png")
                self.straight = pygame.image.load("blue.png")
                self.speed = 3

            # Load the images for red team    
            elif tagger:
                self.right_image0 = pygame.image.load("red_right_0.png")
                self.right_image1 = pygame.image.load("red_right_1.png")
                self.left_image0 = pygame.image.load("red_left_0.png")
                self.left_image1 = pygame.image.load("red_left_1.png")
                self.straight = pygame.image.load("red.png")
                self.speed = 4
                self.tagger = True
                self.score += 1

            # Select 2 images for the animation    
            self.image0 = self.straight
            self.image1 = self.straight
            self.playerNum = playerNumber
            self.image = self.image0
            self.playerHeader = header
            
            #Make them Sprites
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.startx = x
            self.starty = y
            self.x = x
            self.y = y

        def move(self):        
            # Move the player
            if self.ghost != "on":
                self.x += self.moveX

                # When player collides with block sprite #####
                block_hit_list = pygame.sprite.spritecollide(self, wallList, False)

                # Collisions ############Checkpoint
                for block in block_hit_list:
                    if block.rect.top > self.rect.top:
                        if self.moveX > 0:
                            self.rect.right = block.rect.left - 3
                        elif self.moveX ==  0:
                            self.moveX = self.moveX
                        else:               
                            self.rect.left = block.rect.right + 3
                self.rect.y += self.moveY

                self.y += self.moveY
                block_hit_list = pygame.sprite.spritecollide(self, wallList, False)
                for block in block_hit_list:
                    
                    if self.moveY > 0:
                            self.rect.bottom = block.rect.top - 3
                    else:
                        self.rect.top = block.rect.bottom+3
            power_hit_list = pygame.sprite.spritecollide(self, powerList, True)
            for power in power_hit_list:
                if power.name == "speed":
                    self.speedon = "on"
                    self.speed = 5
                    whoosh.play()
                    power.available = False
                elif power.name == "ghost":
                    self.ghost = "on"
                    power.available = False

            for a in range(4):
                if self.playerNum != a:


                    player_hits = pygame.sprite.spritecollide(self, spritecomplete[a], False)
                    for player in player_hits:
                        if self.tagger == True:
                            
                            player.tagger = True
                            self.tagger = False
                            self.change()
                            player.change()
                            player1.reset()
                            player2.reset()
                            player3.reset()
                            player4.reset()
                        elif player.tagger == True:
                            self.tagger = True
                            player.tagger = False
                            self.change()
                            player.change()
                            player1.reset()
                            player2.reset()
                            player3.reset()
                            player4.reset()
                    
        def control(self, pressed, key):
            if pressed:
                if (key == "LEFT"):
                    self.moveX = -1*(self.speed)
                    self.image0 = self.left_image0
                    self.image1 = self.left_image1
                        
                if (key == "RIGHT"):
                    self.moveX= 1*(self.speed)
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
                self.speedTimer += 1
            if self.speedTimer == 200:
                self.speedon = "off"
                self.speedTimer = 0
                self.speed = 3
            if self.ghost == "on":
                self.ghostTimer +=1
            if self.ghostTimer == 300:
                self.ghostTimer = 0
                self.ghost = "off"
            
            if self.rect.x < 0 or self.rect.x >1080 or self.rect.y > 720 or self.rect.y < 0:
                self.reset()

                
            self.player = font2.render(str(self.playerHeader),True,BLACK)
            screen.blit(self.player, [self.rect.x+5, self.rect.y-30])
            
        def getScore (self):
            if self.tagger:
                self.score -= 0.016
            elif not self.tagger:
                self.score += 0.016
        def change(self):
            if self.tagger:
                self.right_image0 = pygame.image.load("red_right_0.png")
                self.right_image1 = pygame.image.load("red_right_1.png")
                self.left_image0 = pygame.image.load("red_left_0.png")
                self.left_image1 = pygame.image.load("red_left_1.png")
                self.straight = pygame.image.load("red.png")
                self.speed = 4
                self.tagger = True
                self.score += 1
            elif not self.tagger:
                self.right_image0 = pygame.image.load("blue_right_0.png")
                self.right_image1 = pygame.image.load("blue_right_1.png")
                self.left_image0 = pygame.image.load("blue_left_0.png")
                self.left_image1 = pygame.image.load("blue_left_1.png")
                self.straight = pygame.image.load("blue.png")
                self.speed = 3
        def reset(self):
            self.rect.x = self.startx
            self.rect.y = self.starty
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
        available = True
        timer = 0
        def __init__(self, x, y, name, pic):
            super(PowerUp, self).__init__()
            self.name = name
            self.xpos = x
            self.ypos = y
            self.image = pygame.image.load(pic).convert()
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        def draw(self):
            if self.available == False:
                self.timer += 1
                if self.timer == 200:
                    self.available = True
                    self.timer = 0
            else:
                powerList.add(self)

    # Create all the players            
    player1 = Player(922, 89, True, "P1",0)
    player2 = Player(100, 210, False, "P2", 1)
    player3 = Player(189, 648, False, "P3", 2)
    player4 = Player(821, 503, False, "P4", 3)


    wallList = pygame.sprite.Group()
    playerList = pygame.sprite.Group()

    # Draw all walls
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
        wall = Wall(80,wall3)
        wall.draw(80,wall3)

    for wall4 in range (96,224,16):
        wall = Wall(wall4,64)
        wall.draw(wall4,64)
        
    for wall5 in range (384,624,16):
        # Loop for 2 columns
        for wall5A in range (80,112,16):
            wall = Wall(wall5A,wall5)
            wall.draw(wall5A,wall5)

    for wall6 in range (112,416,16):
        # Loop for 2 rows
        for wall6A in range (576,612,16):
            wall = Wall(wall6,wall6A)
            wall.draw(wall6,wall6A)

    for wall7 in range (272,416,16):
        # Loop for 6 rows
        for wall7A in range (624,704,16):
            wall = Wall(wall7,wall7A)
            wall.draw(wall7,wall7A)

    for wall8 in range (144,160,16):
        # Loop for 3 rows
        for wall8A in range (128, 160,16):
            wall = Wall(wall8,wall8A)
            wall.draw(wall8,wall8A)

    for wall9 in range (144,224,16):
        wall = Wall(wall9,160)
        wall.draw(wall9,160)

    for wall10 in range (80,160,16):
        wall = Wall(208,wall10)
        wall.draw(208,wall10)

    for wall11 in range (368,624,16):
        wall = Wall(wall11,144)
        wall.draw(wall11,144)

    for wall12 in range (160,336,16):
        # Draw 4 columns
        for wall12A in range (368,432,16):
            wall = Wall(wall12A,wall12)
            wall.draw(wall12A,wall12)
        
    for wall13 in range (704,912,16):
        # Loop for 5 rows
        for wall13A in range (64,128,16):
            wall = Wall(wall13,wall13A)
            wall.draw(wall13,wall13A)

    for wall14 in range (64,224,16):
        wall = Wall(992,wall14)
        wall.draw(992,wall14)

    for wall15 in range (496,992,16):
        wall = Wall(wall15,208)
        wall.draw(wall15,208)

    for wall16 in range (176,320,16):
        wall = Wall(wall16,224)
        wall.draw(wall16,224)
            
    for wall19 in range (240,512,16):
        wall = Wall(176,wall19)
        wall.draw(176,wall19)

    for wall20 in range (256,304,16):
        # Loop for 3 columns
        for wall20A in range (320,512,16):
            wall = Wall(wall20,wall20A)
            wall.draw(wall20,wall20A)

    for wall21 in range (304,416,16):
        wall = Wall(wall21,496)
        wall.draw(wall21,496)

    for wall22 in range (416,512,16):
        wall = Wall(416,wall22)
        wall.draw(416,wall22)
        
    for wall23 in range (368,432,16):
        wall = Wall(wall23,416)
        wall.draw(wall23,416)

    for wall24 in range (304,624,16):
        wall = Wall(992,wall24)
        wall.draw(992,wall24)

    for wall25 in range(928,992,16):
        # Loop for 4 columns
        for wall25A in range (304,496,16):
            wall = Wall(wall25,wall25A)
            wall.draw(wall25,wall25A)

        wall = Wall(wall25,608)
        wall.draw(wall25,608)

    for wall26 in range (496,864,16):
        wall = Wall(wall26,288)
        wall.draw(wall26,288)

    for wall27 in range (304,608,16):
        wall = Wall(496,wall27)
        wall.draw(496,wall27)

    for wall28 in range (288,592,16):
        wall = Wall(848,wall28)
        wall.draw(848,wall28)

    for wall29 in range (576,864,16):
        wall = Wall(wall29,592)
        wall.draw(wall29,592)

    for wall30 in range (368,592,16):
        wall = Wall(576,wall30)
        wall.draw(576,wall30)

    for wall31 in range (592,784,16):
        wall = Wall(wall31,368)
        wall.draw(wall31,368)

    for wall32 in range (384,528,16):
        wall = Wall(768,wall32)
        wall.draw(768,wall32)

    for wall33 in range (656,784,16):
        wall = Wall(wall33,528)
        wall.draw(wall33,528)

    for wall34 in range (448,528,16):
        # Loop for 3 columns
        for wall34A in range (656,704,16):
            wall = Wall(wall34A,wall34)
            wall.draw(wall34A,wall34)

    for wall36 in range (560,608,16):
        wall = Wall(928,wall36)
        wall.draw(928,wall36)

    for wall38 in range (912,980,16):
        wall = Wall(wall38,64)
        wall.draw(wall38,64)

    for wall39 in range (304,624,16):
        wall = Wall(wall39,64)
        wall.draw(wall39,64)

    for wall40 in range (80,224,16):
        wall = Wall(304,wall40)
        wall.draw(304,wall40)


    
    wings = PowerUp(85, 85, "speed", "speed.png")
    ghost = PowerUp(728, 411, "ghost", "ghost.png")
    pygame.mixer.init(1984000)
    pygame.mixer.music.load('backmusic2.ogg')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()
    while not done:
        screen.fill(WHITE)
        sprite1 = pygame.sprite.Group()
        sprite2 = pygame.sprite.Group()
        sprite3 = pygame.sprite.Group()
        sprite4 = pygame.sprite.Group()
        sprite1.add(player1)
        sprite2.add(player2)
        sprite3.add(player3)
        sprite4.add(player4)
        spritecomplete = [sprite1, sprite2, sprite3, sprite4]
        powerList = pygame.sprite.Group()
        spriteList = pygame.sprite.Group()
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                done = True
            elif pygame.mouse.get_pressed()[0] == True:
                mouse_position = pygame.mouse.get_pos()
                mouse_x = mouse_position[0]
                mouse_y = mouse_position[1]
                
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
            elif event.type == pygame.constants.USEREVENT:
                pygame.mixer.music.play()
        #Score
        player1.getScore()
        player2.getScore()
        player3.getScore()
        player4.getScore()

        scores = []
        scores.append((int(player1.score), "Player 1"))
        scores.append((int(player2.score), "Player 2"))
        scores.append((int(player3.score), "Player 3"))
        scores.append((int(player4.score), "Player 4"))
        scores.sort()
        scores.reverse()


        #Scoreboard
        scoreBoard = pygame.image.load("scoreBoard.png")
        screen.blit(scoreBoard, (1088,0))
        
        # Player Icons
        player1_icon = player1.straight
        player1_icon.set_colorkey(WHITE) #Clear Background
        screen.blit(player1_icon, (1094,60))

        player2_icon = player2.straight
        player2_icon.set_colorkey(WHITE) #Clear Background
        screen.blit(player2_icon, (1094, 200))

        player3_icon = player3.straight
        player3_icon.set_colorkey(WHITE) #Clear Background
        screen.blit(player3_icon, (1094, 340))

        player4_icon = player4.straight
        player4_icon.set_colorkey(WHITE) #Clear Background
        screen.blit(player4_icon, (1094, 480))

        #Display the scores
        player1Score = font.render(str(int(player1.score)),True,BLACK)
        screen.blit(player1Score, [1148, 60])
        
        player2Score = font.render(str(int(player2.score)),True,BLACK)
        screen.blit(player2Score, [1148, 200])
        
        player3Score = font.render(str(int(player3.score)),True,BLACK)
        screen.blit(player3Score, [1148, 340])
        
        player4Score = font.render(str(int(player4.score)),True,BLACK)
        screen.blit(player4Score, [1148, 480])

        # Game Timer
        sec -= 0.0167
        if sec < 0:
            minute -=1
            sec = 60

        
        if len(str(int(sec))) < 2:
            str_sec = "0" + str(int(sec))
        else:
            str_sec = str(int(sec))
        gameTimer = str(minute) + ":" + str_sec

        timer = font_time.render(gameTimer,True,BLACK)
        screen.blit(timer, [1108, 640])

        # Game ender
        if (minute <= 0 and sec < 0.02) or player1.score < 0 or player2.score < 0 or player3.score < 0 or player4.score < 0:
            done = True
        
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
        
        wings.draw()
        ghost.draw()
        wallList.draw(screen)

        spriteList.add(player1)
        spriteList.add(player2)
        spriteList.add(player3)
        spriteList.add(player4)
        player1.move()
        player2.move()
        player3.move()
        player4.move()
        spriteList.draw(screen)
        powerList.draw(screen)


        
        pygame.display.flip()
        clock.tick(60)
    room_scores(scores)
    

def room_scores(scores):
    # Define some colors
    BLACK    = (   0,   0,   0)
    WHITE    = ( 255, 255, 255)
    RED      = ( 255,   0,   0)

    # Set the width and height of the screen [width, height]
    size = (1238, 720)
    screen = pygame.display.set_mode((1238, 720))     
    pygame.display.set_caption("Labyrith Rush")

    font = pygame.font.SysFont('Calibri', 60, True, False)
     
    # Loop until the user clicks the close button.
    done = False
     
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop        
        screen.fill(BLACK)
        
        scores_backgound = pygame.image.load("Scores.png")
        screen.blit(scores_backgound, (0,0))
        info_y = 180 
        for score in scores:
            info_y +=  65
            player_name = font.render(score[1],True,BLACK)
            player_score = font.render(str(score[0]),True,BLACK)
            screen.blit(player_name, (146,info_y))
            screen.blit(player_score, (384,info_y))
            
        pygame.display.flip()
        
        mouse_position = pygame.mouse.get_pos()
        mouse_x = mouse_position[0]
        mouse_y = mouse_position[1]
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop

            elif (pygame.mouse.get_pressed()[0] == True):
                if (mouse_x > 53 and mouse_x < 395 and mouse_y > 575 and mouse_y < 680):
                    done = True

                if (mouse_x > 638 and mouse_x < 1176 and mouse_y > 556 and mouse_y < 688):
                    room_menu()
                    done = True
                    
    #######################################################################################################    
        
            
        clock.tick(60)     

room_menu()
pygame.quit()
