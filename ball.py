#Imports:
import pygame
import random
from constants import *

#Initialising Pygame:
pygame.init()
pygame.display.init()
pygame.font.init()

class Ball(pygame.sprite.Sprite):
    """Creates a Ball sprite."""

    def __init__(self):
        """Allows a Ball to be instantiated."""

        super().__init__() #inherits attributes from the parent sprite class

        #Calculating paddle dimensions and position:
        size = WIDTH/160
        self.startingx, self.startingy = WIDTH/2, (HEIGHT - HEIGHT/90 - WIDTH/20)

        #Creating the ball shape:
        self.image=pygame.Surface((size,size)) #creates a square object of a given size
        self.image.fill(WHITE) #changes the colour of the square
        self.rect = self.image.get_rect(topleft = (self.startingx,self.startingy)) #allows the object to be manipulated

        self.speed = 3 #the speed of the ball (constant)
        self.reset() #resets the position and direction of the ball to its original values


    def update(self):
        """Updates the position of the ball as it changes in direction."""

        self.rect.x += self.speed * self.xdirection
        self.rect.y += self.speed * self.ydirection
    

    def reset(self):
        """Resets the position and direction of the ball to its original values."""

        self.rect.x, self.rect.y = self.startingx, self.startingy
        self.xdirection = random.randrange(-1, 2, 2) #chooses either -1 or 1 for the initial x-direction
        self.ydirection = -1 #upwards