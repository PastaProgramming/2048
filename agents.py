import pygame
import random
import board as b
from abc import ABC, abstractmethod

# global array for looping through the directions 
moveDirections = [b.Dir.UP, b.Dir.DOWN, b.Dir.LEFT, b.Dir.RIGHT]

# abstract player class
class Agent(ABC):
    @abstractmethod
    def getMove(self, cells, score):
        pass

# represents human player
# note: doesn't inherit from Agent
class Human():
    def getMove(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    return b.Dir.DOWN
                elif event.key == pygame.K_UP:
                    return b.Dir.UP
                elif event.key == pygame.K_LEFT:
                    return b.Dir.LEFT
                elif event.key == pygame.K_RIGHT:
                    return b.Dir.RIGHT
                elif event.key == pygame.K_r:
                    return pygame.K_r
        return -1

# always makes random moves  
class RandomModel(Agent):
    def getMove(self, cells, score):
        return random.choice(moveDirections)

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

    def getMove(self, cells, score):
        dirScores = [0,0,0,0]
        for direction in moveDirections:
            dirScores[direction.value] = self.evalMove(cells, score, direction)

        bestDirIndex = dirScores.index(max(dirScores))
        return moveDirections[bestDirIndex]

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
        for direction in moveDirections:
            newCells, score, changed = b.moveCopy(cells, score, direction)
            b.addNum(newCells)
            if changed:
                dirScores[direction.value] = self.evalState(newCells, score, depth - 1)
        return max(dirScores)

    def getMove(self, cells, score):
        dirScores = [0,0,0,0]
        
        for direction in moveDirections:
            newCells, score, changed = b.moveCopy(cells, score, direction)
            if changed:
                dirScores[direction.value] = self.evalState(newCells, score, self.searchDepth)
            
        bestDirIndex = dirScores.index(max(dirScores))
        return moveDirections[bestDirIndex]

# I'm trying to build a heuristic

import heuristicHelpers as h
import numpy as np

class HeuristicModel(Agent):
    def evalState(self, cells, score):
        if b.gameIsOver(cells):
            return 0
        
        evalScore = score

        evalScore += h.weightScore(cells) * (score // 1000)
        evalScore += h.differenceScore(cells) * (score // 1000)
        evalScore += h.zeroCount(cells) * (score // 8)

        return evalScore

    def getMove(self, cells, score):
        dirScores = [-np.inf,-np.inf,-np.inf,-np.inf]

        if score < 1000:
            dirScores = [5, 2, 10, 1]
            for direction in moveDirections:
                _, _, changed = b.moveCopy(cells, score, direction)
                if changed == False:
                    dirScores[direction.value] = 0
            bestDirIndex = dirScores.index(max(dirScores))
            return moveDirections[bestDirIndex]
        
        # score >= 1000
        for direction in moveDirections:
            newCells, score, changed = b.moveCopy(cells, score, direction)
            if changed:
                dirScores[direction.value] = self.evalState(newCells, score)
            
        bestDirIndex = dirScores.index(max(dirScores))
        return moveDirections[bestDirIndex]