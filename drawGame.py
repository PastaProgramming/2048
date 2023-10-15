import pygame

# font sizing for different lengths of numbers
fontSizes = {1: 64,   2: 64,
             3: 60,   4: 46,
             5: 40,   6: 28}

# cell color for each number
cellColors = {0: (214, 213, 209),
              2: (248, 239, 225),
              4: (243, 229, 198),
              8: (243, 195, 152),
              16: (243, 173, 134),
              32: (245, 135, 103),
              64: (243, 92, 78),
              128: (253, 236, 158),
              256: (253, 232, 132),
              512: (251, 225, 102),
              1024: (251, 220, 72),
              2048: (251, 216, 41),
              4096: (185, 219, 255),
              8192: (176, 205, 253),
              16384: (158, 179, 249),
              32768: (151, 157, 249),
              65536: (129, 127, 241),
              131072: (135, 91, 239)}

# functions!

# draws a grid, to separate cells
def drawGrid(screen, cells, windowSize, offset, cellSize):
    for i in range(4):
        for j in range(4):
            startX = i * cellSize
            startY = j * cellSize + offset
            rect = pygame.Rect(startX, startY, cellSize, cellSize)
            pygame.draw.rect(screen, (156, 154, 141), rect, 4)

# draws game cells
def drawBoard(screen, cells, windowSize, offset, cellSize):
    for i in range(4):
        for j in range(4):
            # draws rectangle based on number color
            startX = i * cellSize
            startY = j * cellSize + offset
            rect = pygame.Rect(startX, startY, cellSize, cellSize)
            centerX = i * cellSize + cellSize // 2
            centerY = j * cellSize + offset + cellSize // 2
            pygame.draw.rect(screen, cellColors[cells[i][j]], rect, 0)

            # draws text if cell has nonzero value
            if cells[i][j] != 0:
                numText = str(cells[i][j])
                font = pygame.font.Font('freesansbold.ttf', fontSizes[len(numText)])
                text = font.render(numText, True, "black")
                textRect = text.get_rect(center = (centerX, centerY))
                screen.blit(text, textRect)

# draws score on top of the board
def drawScore(screen, score, windowSize, offset):
    font = pygame.font.Font('freesansbold.ttf', 32)
    scoreStr = "Score: " + str(score)
    text = font.render(scoreStr, True, "black")
    rightX = int(offset * 0.2)
    topY = offset // 4
    textRect = text.get_rect()
    textRect.move_ip(rightX, topY)
    screen.blit(text, textRect)

def animate(screen, cells, index, windowSize, offset):
    pass

# prints game ending text based on winning or losing
def gameEnd(screen, windowSize, offset, endText):
    font = pygame.font.Font('freesansbold.ttf', 24)
    
    text = font.render(endText, True, "black")
    centerX = (windowSize + 2 *offset) // 2
    centerY = offset // 4
    textRect = text.get_rect(center = (centerX, centerY))
    screen.blit(text, textRect)

    text = font.render("Press r to replay", True, "black")
    centerX = (windowSize + 2 *offset) // 2
    centerY = 3 * offset // 4
    textRect = text.get_rect(center = (centerX, centerY))
    screen.blit(text, textRect)

# prints game over message
def gameOver(screen, windowSize, offset):
    gameEnd(screen, windowSize, offset, "Game Over!")

# prints win message
def gameWon(screen, windowSize, offset):
    gameEnd(screen, windowSize, offset, "You Won!")