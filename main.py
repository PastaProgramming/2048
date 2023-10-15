import pygame
import game
import board as b
import drawGame as draw
import players



# who is running this?
player = players.Human()

game.run(player)
 
pygame.quit()


