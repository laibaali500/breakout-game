#Imports:
import pygame
from constants import *
from game import Game

#Initialising Pygame:
pygame.init()
pygame.display.init()
pygame.font.init()
clock=pygame.time.Clock()

#Main code:
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT)) #creates a PyGame window
pygame.display.set_caption("Breakout") #titles the window
myGame = Game(WINDOW) #instantiates a Game object
run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False #closes the window if the user presses the 'X' button
    myGame.update()
    pygame.display.update() #updates the pygame display
    clock.tick(100) #makes the game operate at 100 frames per second
pygame.quit()