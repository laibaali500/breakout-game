#Imports:
import pygame
from settings import *

#Initialising Pygame:
pygame.init()
pygame.display.init()
pygame.font.init()

class Paddle(pygame.sprite.Sprite):
    """Creates a paddle sprite."""

    def __init__(self):
        """Allows a Paddle to be instantiated."""

        super().__init__() #inherits attributes from the parent sprite class

        #Calculating paddle dimensions and position:
        self.width, self.height = WIDTH/10, HEIGHT/90
        startingx, startingy = (WIDTH/2 - self.width/2), (HEIGHT - HEIGHT/20 - self.height) #at the centre near the bottom of the screen

        #Creating the paddle shape:
        self.image=pygame.Surface((self.width, self.height)) #creates a rectangle object of a given size
        self.image.fill(LIGHT_GREY) #changes the colour of the rectangle
        self.rect = self.image.get_rect(topleft = (startingx, startingy)) #allows the object to be manipulated

        #Paddle movement:
        self.xdirection = 0 #the x-direction of the paddle (either -1,0,or 1)
        self.speed = 0 #the speed at which the paddle moves (in the x-direction)
        self.maxSpeed = 15 #the maximum possible speed the paddle can accelerate to


    def update(self):
        """Handles arrow key events."""

        #Updating the speed and direction of the paddle:
        keys = pygame.key.get_pressed() #checks which keys are being pressed
        if keys[pygame.K_RIGHT]: #if the right arrow key is pressed
            if self.speed < self.maxSpeed:
                self.speed += 0.5 #updates speed
            self.xdirection = 1
        elif keys[pygame.K_LEFT]: #if the left arrow key is pressed
            if self.speed > -self.maxSpeed:
                self.speed += -0.5 #updates speed
            self.xdirection = -1
        else:
            if self.speed != 0: #if the ball is moving, but no keys are pressed
                if self.xdirection == 1: self.speed += -0.5 #reduces speed
                elif self.xdirection == -1: self.speed += 0.5 #reduces speed
            else:
                self.xdirection = 0 #sets the direction to 0 if the ball is stationary
            
        
        #Updating the x-position of the paddle:
        borderWidth = WIDTH/20 #the width of the borders
        if self.rect.x < borderWidth: #if the paddle's right side is touching the left border
            self.rect.x = borderWidth #moves the paddle back to the outside of the border
        elif self.rect.x > (WIDTH - borderWidth - self.width): #if the paddle's left side is touching the right border
            self.rect.x = (WIDTH - borderWidth - self.width) #moves the paddle back to the outside of the border
        else:
            self.rect.x += self.speed #changes x-pos of object by the speed
