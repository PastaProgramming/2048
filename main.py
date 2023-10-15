import pygame
import game
import agents

# who is running this?
player = agents.GreedyModel()

game.run(player)
 
pygame.quit()


