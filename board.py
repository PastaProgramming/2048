import random

# makes new board
def newBoard():
    cells = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    addNum(cells)
    addNum(cells)
    return cells

# returns a copy of input cells
def copy(cells):
    newCells = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(4):
        for j in range(4):
            newCells[i][j] = cells[i][j]
    return newCells

# adds number to the board
def addNum(cells):
    possibilities = []
    for i in range(4):
        for j in range(4):
            if cells[i][j] == 0:
                possibilities.append((i,j))
    
    # no more space
    if len(possibilities) == 0:
        return
        
    i, j = random.choice(possibilities)
        
    if random.random() > 0.1:
        toAdd = 2
    else:
        toAdd = 4

    cells[i][j] = toAdd

    return i, j

# combines numbers up
def combine(cells, score):
    changed = False

    for i in range(4):
        firstNum = None
        for j in range(4):
            currCell = cells[i][j]
            # if we havent found a nonzero number 
            if firstNum == None:
                if currCell != 0:
                    firstNum = currCell
                    firstI, firstJ = i, j
            # if we have found a number to check
            else:
                # a combination can occur
                if firstNum == currCell:
                    cells[firstI][firstJ] = 2 * firstNum
                    cells[i][j] = 0
                    score += 2 * firstNum
                    changed = True
                    firstNum = None
                # if there's a different nonzero number below, 
                # it becomes the new number to check
                elif currCell != 0:
                    firstNum = currCell
                    firstI, firstJ = i, j
    
    return score, changed

# slides numbers up
def slide(cells):
    changed = False

    # makes all nonzero numbers "bubble" up
    for n in range(3):
        for i in range(4):
            for j in range(3):
                if cells[i][j] == 0:
                    cells[i][j] = cells[i][j+1]
                    cells[i][j+1] = 0
                    if cells[i][j] != 0:
                        changed = True
    return changed

# vertically flips the board
def flip(cells):
    for i in range(4):
        for j in range(2):
            topVal = cells[i][j]
            botVal = cells[i][3-j]
            cells[i][j] = botVal
            cells[i][3-j] = topVal

# reflects the board along its main diagonal
def reflect(cells):
    oldCells = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0],]
    for i in range(4):
        for j in range(4):
            oldCells[i][j] = cells[i][j]

    for i in range(4):
        for j in range(4):
            cells[i][j] =  oldCells[j][i]


# directional moves start

# in place moves

def moveUp(cells, score):
    score, changed1 = combine(cells, score)
    changed2 = slide(cells)

    return score, changed1 | changed2
    
def moveDown(cells, score):
    flip(cells)
    score, changed = moveUp(cells, score)
    flip(cells)

    return score, changed

def moveLeft(cells, score):
    reflect(cells)
    score, changed = moveUp(cells, score)
    reflect(cells)

    return score, changed

def moveRight(cells, score):
    reflect(cells)
    score, changed = moveDown(cells, score)
    reflect(cells)

    return score, changed

# copy moves

def moveUpCopy(cells, score):
    newCells = copy(cells)
    score, changed1 = combine(newCells, score)
    changed2 = slide(newCells)

    return newCells, score, changed1 | changed2
    
def moveDownCopy(cells, score):
    newCells = copy(cells)
    flip(newCells)
    score, changed = moveUp(newCells, score)
    flip(newCells)

    return newCells, score, changed

def moveLeftCopy(cells, score):
    newCells = copy(cells)
    reflect(newCells)
    score, changed = moveUp(newCells, score)
    reflect(newCells)

    return newCells, score, changed

def moveRightCopy(cells, score):
    newCells = copy(cells)
    reflect(newCells)
    score, changed = moveDown(newCells, score)
    reflect(newCells)

    return newCells, score, changed

# directional moves end
    
# checks if the game is over
def gameIsOver(cells):
    # check zeroes
    for i in range(4):
        for j in range(4):
            if cells[i][j] == 0:
                return False
    
    # check vertical combinations
    for i in range(4):
        for j in range(3):
            if cells[i][j] == cells[i][j+1]:
                return False
            
    # check horizontal combinations
    for i in range(3):
        for j in range(4):
            if cells[i][j] == cells[i+1][j]:
                return False
    
    # no possible moves
    return True

# checks if game has been won
def gameIsWon(cells):
    for i in range(4):
        for j in range(4):
            if cells[i][j] == 2048:
                return True
    return False