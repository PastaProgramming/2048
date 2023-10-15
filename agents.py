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
    def getMove(self, cells, score, events):
        pass

# represents human player
class Human(Agent):
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

# always makes random moves  
class RandomModel(Agent):
    def getMove(self, cells, score, events):
        return random.choice([UP, DOWN, LEFT, RIGHT])

# makes the move that gives the highest score   
class GreedyModel(Agent):
    # evaluates a move
    def evalMove(self, cells, score, direction):
        
        newCells, score, changed = b.moveCopy(cells, score, direction)
        
        if b.gameIsOver(newCells):
            return 0
        
        if changed:
            score += 1

        return score

    def getMove(self, cells, score, events):
        dirScores = [0,0,0,0]
        for direction in [UP, DOWN, LEFT, RIGHT]:
            dirScores[direction] = self.evalMove(cells, score, direction)

        bestDir = dirScores.index(max(dirScores))
        return bestDir

# represents BFS search through the game
class BFSModel(Agent):
    def __init__(self, depth):
        self.searchDepth = depth
    
    def evalState(self, cells, score, depth):
        if b.gameIsOver(cells):
            return 0
        
        if depth == 0:
            return score
        
        dirScores = [0,0,0,0]
        for direction in [UP, DOWN, LEFT, RIGHT]:
            newCells, score, changed = b.moveCopy(cells, score, direction)
            if changed:
                dirScores[direction] = self.evalState(newCells, score, depth - 1)
        return max(dirScores)

    def getMove(self, cells, score, events):
        dirScores = [0,0,0,0]
        
        for direction in [UP, DOWN, LEFT, RIGHT]:
            newCells, score, changed = b.moveCopy(cells, score, direction)
            if changed:
                dirScores[direction] = self.evalState(newCells, score, self.searchDepth)
            
        bestDir = dirScores.index(max(dirScores))
        return bestDir

# I'm trying to build a heuristic

import heuristicHelpers as h
import numpy

class HeuristicModel(Agent):
    def evalDir(self, direction):
        if direction == LEFT:
            return 10
        if direction == UP:
            return 5
        if direction == DOWN:
            return 2
        if direction == RIGHT:
            return 1
    
    def evalState(self, cells, score):
        if b.gameIsOver(cells):
            return 0
        
        evalScore = score

        evalScore += h.weightScore(cells) * (score // 1000)
        # evalScore += h.adjacencyScore(cells)
        evalScore += h.differenceScore(cells) * (score // 1000)
        evalScore += h.zeroCount(cells) * (score // 8)

        return evalScore

    def getMove(self, cells, score, events):
        # time.sleep(0.4)
        dirScores = [-numpy.inf,-numpy.inf,-numpy.inf,-numpy.inf]

        if score < 1000:
            dirScores = [5, 2, 10, 1]
            for direction in [UP, DOWN, LEFT, RIGHT]:
                _, _, changed = b.moveCopy(cells, score, direction)
                if changed == False:
                    dirScores[direction] = 0
            bestDir = dirScores.index(max(dirScores))
            return bestDir
        
        # score >= 2000
        for direction in [UP, DOWN, LEFT, RIGHT]:
            newCells, score, changed = b.moveCopy(cells, score, direction)
            if changed:
                dirScores[direction] = self.evalState(newCells, score)
            
        bestDir = dirScores.index(max(dirScores))
        return bestDir