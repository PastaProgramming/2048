import pygame

fontSizes = {1: 64,   2: 64,
             3: 60,   4: 46,
             5: 40,   6: 28}

cellColors = {0: (231, 230, 223),
              2: (245, 236, 217),
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

def drawGrid(screen, cells, windowSize, offset, cellSize):
    for i in range(4):
        for j in range(4):
            startX = i * cellSize
            startY = j * cellSize + offset
            rect = pygame.Rect(startX, startY, cellSize, cellSize)
            pygame.draw.rect(screen, (0,0,0), rect, 4)

def drawBoard(screen, cells, windowSize, offset, cellSize):
    for i in range(4):
        for j in range(4):
            startX = i * cellSize
            startY = j * cellSize + offset
            rect = pygame.Rect(startX, startY, cellSize, cellSize)
            centerX = i * cellSize + cellSize // 2
            centerY = j * cellSize + offset + cellSize // 2
            pygame.draw.rect(screen, cellColors[cells[i][j]], rect, 0)
            if cells[i][j] != 0:
                numText = str(cells[i][j])
                font = pygame.font.Font('freesansbold.ttf', fontSizes[len(numText)])
                text = font.render(numText, True, "black")
                textRect = text.get_rect(center = (centerX, centerY))
                screen.blit(text, textRect)

def drawScore(screen, score, windowSize, offset):
    font = pygame.font.Font('freesansbold.ttf', 32)
    scoreStr = "Score: " + str(score)
    text = font.render(scoreStr, True, "black")
    centerX = int(offset * 1.5)
    centerY = offset // 2
    textRect = text.get_rect(center = (centerX, centerY))
    screen.blit(text, textRect)

    def animate(screen, cells, index, windowSize, offset):
        i, j = index

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

def gameOver(screen, windowSize, offset):
    gameEnd(screen, windowSize, offset, "Game Over!")

def gameWon(screen, windowSize, offset):
    gameEnd(screen, windowSize, offset, "You Won!")