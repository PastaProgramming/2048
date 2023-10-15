import pygame
import random

class Player:
    def eval(self):
        pass

    def getMove(self, cells, events):
        pass

class Human(Player):
    def __init__(self):
        pass
    
    def eval(self):
        pass

    def getMove(self, cells, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    return pygame.K_DOWN
                elif event.key == pygame.K_UP:
                    return pygame.K_UP
                elif event.key == pygame.K_LEFT:
                    return pygame.K_LEFT
                elif event.key == pygame.K_RIGHT:
                    return pygame.K_RIGHT
                elif event.key == pygame.K_r:
                    return pygame.K_r
        return 0
    
class DeterministicModel(Player):
    def __init__(self):
        pass
    
    def eval(self):
        pass

    def getMove(self, cells, events):
        return random.choice([pygame.K_DOWN, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT])