#Imports:
import pygame

#Initialising Pygame:
pygame.init()
pygame.display.init()
pygame.font.init()

class Tile(pygame.sprite.Sprite):
    """Creates a Tile sprite."""

    def __init__(self, pos, size, colour):
        """Allows a Tile to be instantiated."""

        super().__init__() #inherits attributes from the parent sprite class
        self.image=pygame.Surface(size) #creates a rectangle object of a given size
        self.image.fill(colour) #changes the colour of the rectangle
        self.rect = self.image.get_rect(topleft = pos) #allows the object to be manipulated