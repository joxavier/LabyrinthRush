import pygame
pygame.init()

window = pygame.display.set_mode((800,600))

pygame.display.set_caption("Players")
clock = pygame.time.Clock()

#Colors
black = (   0,   0,   0)
white = ( 255, 255, 255)

#Players Initial Speed
moveX,moveY=0,0

#Create the Players
class Player(pygame.sprite.Sprite):  
    x, y = 0, 0 # Postion of Player
    flipSpeed = 10 #Speed of animation
    flipTime = 0
    currentImage=0 #Image animater

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
            
        self.image0 = self.straight
        self.image1 = self.straight

        # Set our transparent color
        self.image0.set_colorkey(white)
        self.image1.set_colorkey(white)

        self.x = x
        self.y = y

    def update(self):
        self.flipTime += 1
        if (self.flipTime == self.flipSpeed):
            if (self.currentImage==0):
                self.currentImage=1
            else:
                self.currentImage=0

            self.flipTime=0 #Reset timer

        self.draw()
        
    def draw(self):
        if (self.currentImage==0):
            window.blit(self.image0, (self.x,self.y))
        else:
            window.blit(self.image1, (self.x,self.y))

# Create Players
player1 = Player(10, 10, True)
player2 = Player(10, 210, True)
player3 = Player(10, 410, True)
player4 = Player(500, 300, False)

gameLoop=True
while gameLoop:

    for event in pygame.event.get():
        if (event.type==pygame.QUIT):
            gameLoop=False

        if (event.type==pygame.KEYDOWN):
            if (event.key==pygame.K_LEFT):
                moveX = -3
                player1.image0 = player1.left_image0
                player1.image1 = player1.left_image1
                
            if (event.key==pygame.K_RIGHT):
                moveX= 3
                player1.image0 = player1.right_image0
                player1.image1 = player1.right_image1

            if (event.key==pygame.K_UP):
                moveY = -3
                player1.image0 = player1.straight
                player1.image1 = player1.straight
                
            if (event.key==pygame.K_DOWN):
                moveY = 3
                player1.image0 = player1.left_image0
                player1.image1 = player1.left_image1

        if (event.type==pygame.KEYUP):
            player1.image0 = player1.straight
            player1.image1 = player1.straight
            if (event.key==pygame.K_LEFT):
                moveX=0
                #player1.image0 = player1.straight
                #player1.image1 = player1.straight
            if (event.key==pygame.K_RIGHT):
                moveX=0
                #player1.image0 = player1.right_image1
                #player1.image1 = player1.right_image1

            if (event.key==pygame.K_UP):
                moveY=0
                #player1.image0 = player1.right_image1
                #player1.image1 = player1.right_image1
                
            if (event.key==pygame.K_DOWN):
                moveY=0
                #player1.image0 = player1.left_image1
                #player1.image1 = player1.left_image1
            
    window.fill(white)
    
    #Update Co-ordinates
    player1.x+=moveX
    player1.y+=moveY

    #Update Player
    player1.update()
    player2.update()
    player3.update()
    player4.update()
    
    clock.tick(50)

    pygame.display.flip()

pygame.quit()
