import pygame
import game
import agents

# who is running this?
player = agents.HeuristicModel()

game.run(player)
 
pygame.quit()


