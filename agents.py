import pygame
import random
import time
import board as b
from abc import ABC, abstractmethod

# key constants
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

# abstract player class
class Agent(ABC):
    @abstractmethod
    def eval(self, cells, score):
        pass

    @abstractmethod
    def getMove(self, cells, score, events):
        pass

class Human(Agent):
    def eval(self, cells, score):
        pass 

    def getMove(self, cells, score, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    return DOWN
                elif event.key == pygame.K_UP:
                    return UP
                elif event.key == pygame.K_LEFT:
                    return LEFT
                elif event.key == pygame.K_RIGHT:
                    return RIGHT
                elif event.key == pygame.K_r:
                    return pygame.K_r
        return -1
    
class RandomModel(Agent):
    def eval(self, cells, score):
        pass

    def getMove(self, cells, score, events):
        return random.choice([UP, DOWN, LEFT, RIGHT])
    
class GreedyModel(Agent):
    def eval(self, cells, score):
        pass

    def getMove(self, cells, score, events):
        scoreDirs = [0,0,0,0]
        changedDirs = [False,False,False,False]
        _, scoreDirs[UP], changedDirs[UP] = b.moveUpCopy(cells, score)
        _, scoreDirs[DOWN], changedDirs[DOWN] = b.moveDownCopy(cells, score)
        _, scoreDirs[LEFT], changedDirs[LEFT] = b.moveLeftCopy(cells, score)
        _, scoreDirs[RIGHT], changedDirs[RIGHT] = b.moveRightCopy(cells, score)

        firstMaxDir = scoreDirs.index(max(scoreDirs))
        if changedDirs[firstMaxDir]:
            return firstMaxDir
        else:
            return random.choice([UP, DOWN, LEFT, RIGHT])

