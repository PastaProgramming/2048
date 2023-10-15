import random

# adds number to the board
def addNum(cells):
    possibilities = []
    for i in range(4):
        for j in range(4):
            if cells[i][j] == 0:
                possibilities.append((i,j))

    if len(possibilities) == 0:
        # NO MORE SPACE
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
            # if we havent found a number yet
            if firstNum == None:
                if currCell != 0:
                    firstNum = currCell
                    firstI, firstJ = i, j
            # if we have found a number to check
            else:
                # if a combination can occur
                if firstNum == currCell:
                    cells[firstI][firstJ] = 2 * firstNum
                    cells[i][j] = 0
                    score += 2 * firstNum
                    changed = True
                    firstNum = None
                # if there's a different number below, it becomes
                # the new number to check
                elif currCell != 0:
                    firstNum = currCell
                    firstI, firstJ = i, j
    
    return score, changed

# slides numbers up
def slide(cells):
    changed = False

    for n in range(3):
        for i in range(4):
            for j in range(3):
                if cells[i][j] == 0:
                    cells[i][j] = cells[i][j+1]
                    cells[i][j+1] = 0
                    if cells[i][j] != 0:
                        changed = True
    return changed

def flip(cells):
    for i in range(4):
        for j in range(2):
            topVal = cells[i][j]
            botVal = cells[i][3-j]
            cells[i][j] = botVal
            cells[i][3-j] = topVal

def reflect(cells):
    oldCells = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0],]
    for i in range(4):
        for j in range(4):
            oldCells[i][j] = cells[i][j]

    for i in range(4):
        for j in range(4):
            cells[i][j] =  oldCells[j][i]


def slideUp(cells, score):
    score, changed1 = combine(cells, score)
    changed2 = slide(cells)

    return score, changed1 | changed2
    
def slideDown(cells, score):
    flip(cells)
    score, changed = slideUp(cells, score)
    flip(cells)

    return score, changed

def slideLeft(cells, score):
    reflect(cells)
    score, changed = slideUp(cells, score)
    reflect(cells)

    return score, changed

def slideRight(cells, score):
    reflect(cells)
    score, changed = slideDown(cells, score)
    reflect(cells)

    return score, changed
    
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

def gameIsWon(cells):
    for i in range(4):
        for j in range(4):
            if cells[i][j] == 2048:
                return True
    return False