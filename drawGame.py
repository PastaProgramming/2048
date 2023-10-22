import pygame

# font sizing for different lengths of numbers
fontSizes = {1: 64,   2: 60,
             3: 55,   4: 40,
             5: 32,   6: 28}

# cell color for each number
cellColors = {0: (214, 213, 209),
              2: (248, 239, 225),
              4: (243, 229, 198),
              8: (243, 195, 152),
              16: (243, 173, 134),
              32: (245, 135, 103),
              64: (243, 92, 78),
              128: (255, 236, 185),
              256: (255, 232, 162),
              512: (255, 225, 140),
              1024: (250, 215, 130),
              2048: (245, 205, 125),
              4096: (190, 245, 250),
              8192: (170, 210, 240),
              16384: (150, 175, 242),
              32768: (130, 130, 241),
              65536: (140, 90, 200),
              131072: (110, 60, 170)}

# functions!

# draws a grid, to separate cells
def drawGrid(screen, offset, cellSize):
    for i in range(4):
        for j in range(4):
            startX = i * cellSize
            startY = j * cellSize + offset
            rect = pygame.Rect(startX, startY, cellSize, cellSize)
            pygame.draw.rect(screen, (156, 154, 141), rect, 4)

# draws game cells
def drawBoard(screen, cells, offset, cellSize):
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
def drawScore(screen, score, offset):
    font = pygame.font.Font('freesansbold.ttf', 32)
    scoreStr = "Score: " + str(score)
    text = font.render(scoreStr, True, "black")
    rightX = int(offset * 0.2)
    topY = offset // 4
    textRect = text.get_rect()
    textRect.move_ip(rightX, topY)
    screen.blit(text, textRect)

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