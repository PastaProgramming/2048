import math

def highestCell(cells):
    high, highI, highJ = 0, 0, 0
    for i in range(4):
        for j in range(4):
            if cells[i][j] > high:
                high = cells[i][j]
                highI, highJ = i, j
    return high, highI, highJ

def low(num):
    return num <= 16

def high(num):
    return num >= 128


def findStableCells(cells):
    stableCells = []
    for i in range(4):
        for k in range(4):
            if i % 2 == 0:
                j = k
            else:
                j = 3 - k
            
            if high(cells[i][j]):
                stableCells.append((i, j))
    return stableCells


tunedWeights = [[5, 3, 2, 1.5],
                [0.8, 0.8, 1, 1.25],
                [-1, -1, -0.75, -0.5],
                [-2, -2, -2, -1]]
 
def makeWeights(cells):
    stable = findStableCells(cells)
    """ if len(stable) == 0:
        return tunedWeights """
    
    weights = [tunedWeights[i].copy() for i in range(4)]
    for i in range(4):
        for k in range(4):
            if i % 2 == 0:
                j = k
            else:
                j = 3 - k
            
            weights[i][j] = 5
            stable.pop
    
    for (i, j) in stable:
        weights[i][j] = 5
    return weights

# returns the maximum value and index 
# of the highest value on the board
def weightScore(cells):
    boardWeight = 0
    weights = tunedWeights
    
    for i in range(4):
        for j in range(4):
            boardWeight += cells[i][j] * weights[i][j]
    return boardWeight

def adjacencyScore(cells):
    score = 0
    # check vertical combinations
    for i in range(4):
        if i == 0:
            mult = 3
        else:
            mult = 1
        for j in range(3):
            if cells[i][j] == cells[i][j+1]:
                score += cells[i][j] * mult
            
    # check horizontal combinations
    for i in range(3):
        if i == 0:
            mult = 3
        else:
            mult = 1
        for j in range(4):
            if cells[i][j] == cells[i+1][j]:
                score += cells[i][j] * mult
    return score

def differenceScore(cells):
    score = 0
    # check vertical combinations
    for i in range(4):
        if i == 0:
            mult = 3
        else:
            mult = 1
        for j in range(3):
            if (cells[i][j] != 0) & (cells[i][j+1] != 0):
                curr = math.log2(cells[i][j])
                next = math.log2(cells[i][j+1])
                diff = curr - next
                if diff == 0:
                    score += 4 * cells[i][j] * mult
                elif diff > 0:
                    score += cells[i][j] * mult / diff**2
                elif diff < 0:
                    if i % 2 == 0:
                        score -= cells[i][j] * mult * diff**2
                    else:
                        score = cells[i][j] * mult / diff**2
            
    # check horizontal combinations
    for i in range(3):
        if i == 0:
            mult = 3
        else:
            mult = 1
        for j in range(4):
            if (cells[i][j] != 0) & (cells[i+1][j] != 0):
                curr = math.log2(cells[i][j])
                next = math.log2(cells[i+1][j])
                diff = curr - next
                if diff == 0:
                    score += 4 * cells[i][j] * mult
                elif diff > 0:
                    score += cells[i][j] * mult / diff**2
                elif diff < 0:
                    score -= cells[i][j] * mult * diff**2
    return score

def zeroCount(cells):
    count = 0
    for i in range(4):
        for j in range(4):
            if cells[i][j] == 0:
                count += 1
    return count


fullWeights = [[30 ,  10, 2  , 2],
               [1 ,  1, 1.2, 1.5],
               [-1, -1, -1 , -1],
               [-2, -2, -2 , -2]]

ThreeFourWeights = [[10 ,  5, 2  , 2],
                    [1 ,  1, 1.2, 1.5],
                    [-1, -1, -1 , -1],
                    [-2, -2, -2 , -2]]

minimalWeights = [[15, 10, 2, 2],
                  [1.5, 1, 1.25, 1.75],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]]