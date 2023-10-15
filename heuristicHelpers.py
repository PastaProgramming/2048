# returns the maximum value and index 
# of the highest value on the board
def weightScore(cells):
    boardWeight = 0
    weights = [[10 ,  5, 2  , 2],
               [1 ,  1, 1.2, 1.5],
               [-1, -1, -1 , -1],
               [-2, -2, -2 , -2]]
    
    for i in range(4):
        for j in range(4):
            boardWeight += cells[i][j] * weights[i][j]
    return boardWeight

def adjacencyScore(cells):
    score = 0
    # check vertical combinations
    for i in range(4):
        for j in range(3):
            if cells[i][j] == cells[i][j+1]:
                score += cells[i][j]
            
    # check horizontal combinations
    for i in range(3):
        for j in range(4):
            if cells[i][j] == cells[i+1][j]:
                score += cells[i][j]
    return score