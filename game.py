#Imports:
import pygame
import time
from settings import *
from paddle import Paddle
from ball import Ball
from tile import Tile

#Initialising Pygame:
pygame.init()
pygame.display.init()
pygame.font.init()
clock=pygame.time.Clock()


class Game():
    """Handles sprites, collisions, and user inputs."""

    def __init__(self, window):
        """Allows a Game to be instantiated."""

        self.window = window #allows the PyGame window to be accessed

        #Game logic:
        self.score = 0
        self.lives = 5
        self.win = False
        self.gameOver = False

        #Creating border rects:
        borderWidth= WIDTH/20
        self.topBorder = pygame.Rect(0, 0, WIDTH, borderWidth)
        self.leftBorder = pygame.Rect(0, borderWidth, borderWidth, HEIGHT - borderWidth)
        self.rightBorder = pygame.Rect(WIDTH - borderWidth, borderWidth, borderWidth, HEIGHT - borderWidth)

        #Creating sprite groups:
        self.paddle = pygame.sprite.GroupSingle() #initialises an empty sprite group for the paddle
        self.ball = pygame.sprite.GroupSingle() #initialises an empty sprite group for the ball
        self.tiles = pygame.sprite.Group() #initialises an empty sprite group for the tiles

        #Adding objects to their sprite groups:
        paddle = Paddle()
        self.paddle.add(paddle)
        ball = Ball()
        self.ball.add(ball)
        self.addTiles()


    def addTiles(self):
        """Iterating over each column and row of the tiles to add tile objects to the sprite group."""

        self.tiles.empty() #removes any existing sprites if the game has been reset
        borderWidth= WIDTH/20
        tileWidth = (WIDTH - 2*borderWidth)/COLUMNS #calculating tile width
        tileHeight = HEIGHT//22 #calculating tile height
        for row in range(ROWS):
            for col in range(COLUMNS):
                x = borderWidth + (col * tileWidth) #calculates x-pos for each tile
                y = 2*borderWidth + (row * tileHeight) #calculates y-pos for each tile
                tile = Tile(pos=(x, y),size=(tileWidth, tileHeight),colour=TILECOLOURS[row]) #instantiating a tile
                self.tiles.add(tile) #adding each tile to the sprite group


    def collisions(self):
        """Updates direction of ball based on what it collides with."""

        ball = self.ball.sprite #will allow the rect of the ball to be accessed more easily later on
        
        #Updating the y-direction of the ball depending on its collisions with the tiles:
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(ball.rect):
                #If the rect of a tile touches the rect of the ball:
                ball.ydirection = -ball.ydirection #reverses the y-direction of the ball
                self.score += 1 #increments the score
                sprite.kill() #deletes the tile from the sprite group

        #Updating the y-direction of the ball depending on its collisions with the paddle:
        if self.paddle.sprite.rect.colliderect(ball.rect):
            #If the rect of the paddle touches the rect of the ball:
            ball.ydirection = -ball.ydirection #reverses the y-direction of the ball

        #Updating the y-direction of the ball depending on its collisions with the top border:
        if self.topBorder.colliderect(ball.rect):
            #If the rect of the top border touches the rect of the ball:
            ball.ydirection = -ball.ydirection #reverses the y-direction of the ball

        #Updating the x-direction of the ball depending on its collisions with the left border:
        if self.leftBorder.colliderect(ball.rect):
            #If the rect of the left border touches the rect of the ball:
            ball.xdirection = -ball.xdirection #reverses the x-direction of the ball
        
        #Updating the x-direction of the ball depending on its collisions with the right border:
        if self.rightBorder.colliderect(ball.rect):
            #If the rect of the right border touches the rect of the ball:
            ball.xdirection = -ball.xdirection #reverses the x-direction of the ball


    def checkIfMissed(self):
        """Removes a life if the ball touches the bottom of the screen."""

        if self.ball.sprite.rect.y > HEIGHT:
            #If the ball moves past the bottom of the screen:
            if self.lives != 0:
                self.lives -= 1 #removes a life
                time.sleep(1) #adds a short delay before resetting the ball
                self.ball.sprite.reset() #moves the ball to its original position
            else:
                self.gameOver = True #causes the game to end


    def checkIfWin(self):
        """Checks if all the tiles have disappeared and the player has won."""

        if not self.tiles: #tells us whether there are no tiles, since an empty sprite group returns False
            self.win = True #causes the game to end


    def checkIfSpace(self):
        """Resets the game if the space bar has been pressed after the game ends."""

        keys = pygame.key.get_pressed() #checks which keys are being pressed
        if keys[pygame.K_SPACE]: #if the space bar is pressed
            self.score = 0
            self.lives = 5
            self.win = False
            self.gameOver = False
            self.addTiles()
            self.ball.sprite.reset() #moves the ball to its original position


    def update(self):
        """Draws sprites, updates positions, handles user inputs."""

        self.window.fill(BLACK) #fills the background with black

        #Drawing and updating sprites:
        if (self.gameOver == False) and (self.win == False):
            #These sprites only show while the game has not ended:
            self.paddle.draw(self.window)
            self.paddle.update()
            self.ball.draw(self.window)
            self.ball.update()
            self.tiles.draw(self.window)
            self.collisions()
            self.checkIfMissed()
            self.checkIfWin()
        
        #Drawing borders:
        pygame.draw.rect(self.window, DARK_GREY, self.topBorder) #drawing the top border
        pygame.draw.rect(self.window, DARK_GREY, self.leftBorder) #drawing the left border
        pygame.draw.rect(self.window, DARK_GREY, self.rightBorder) #drawing the right border

        #Updating text:
        borderWidth = WIDTH//20
        self.scoreText = "Score: " + str(self.score) #updates the score text
        self.livesText = "Lives: " + str(self.lives) #updates the lives text
        font = pygame.font.SysFont(FONTSTYLE, borderWidth//2) #creates the font to be used for the text
        scoreTextRender = font.render(self.scoreText, True, LIGHT_GREY) #renders the score text
        livesTextRender = font.render(self.livesText, True, LIGHT_GREY) #renders the lives text
        winTextRender = font.render("You Win!", True, LIGHT_GREY) #renders the win message
        loseTextRender = font.render("Game Over!", True, LIGHT_GREY) #renders the game over message
        playAgainTextRender = font.render("Press [space] to play again", True, LIGHT_GREY) #renders the play again message

        #Drawing text:
        self.window.blit(scoreTextRender, (borderWidth*2,borderWidth/4)) #draws the score text
        self.window.blit(livesTextRender, (WIDTH - borderWidth*4,borderWidth/4)) #draws the lives text
        if self.win: 
            self.window.blit(winTextRender, (WIDTH/2-borderWidth,borderWidth/4)) #draws the win message, if the player has won
            self.window.blit(playAgainTextRender, (WIDTH/2-borderWidth*3,HEIGHT/2)) #draws the play again message
            self.checkIfSpace() #checks if the space bar has been pressed
        if self.gameOver: 
            self.window.blit(loseTextRender, (WIDTH/2-borderWidth*1.4,borderWidth/4)) #draws the game over text, if the player has lost
            self.window.blit(playAgainTextRender, (WIDTH/2-borderWidth*3,HEIGHT/2)) #draws the play again message
            self.checkIfSpace() #checks if the space bar has been pressed
