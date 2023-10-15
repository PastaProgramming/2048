import pygame
import board as b
import drawGame as draw
import agents

# key constants
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

# runs the game for given player
def run(player):

    # game setup 

    WINDOW_SIZE = 480
    OFFSET = 80
    cellSize = WINDOW_SIZE // 4

    cells = b.newBoard()
    score = 0

    # pygame setup

    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + OFFSET))
    clock = pygame.time.Clock()
    running = True
    
    # gameplay loop

    while running:
        events = pygame.event.get()

        # if the player wants to quit
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        # get and act on player move
        move = player.getMove(cells, score, events)

        if move == UP:
            score, changed = b.moveUp(cells, score)
            if changed:
                b.addNum(cells)
        elif move == DOWN:
            score, changed = b.moveDown(cells, score)
            if changed:
                b.addNum(cells)
        elif move == LEFT:
            score, changed = b.moveLeft(cells, score)
            if changed:
                b.addNum(cells)
        elif move == RIGHT:
            score, changed = b.moveRight(cells, score)
            if changed:
                b.addNum(cells)
        elif move == pygame.K_r:
            cells = b.newBoard()
            score = 0

        # display frame
        screen.fill("white")
        draw.drawBoard(screen, cells, WINDOW_SIZE, OFFSET, cellSize)
        draw.drawGrid(screen, cells, WINDOW_SIZE, OFFSET, cellSize)
        draw.drawScore(screen, score, WINDOW_SIZE, OFFSET)

        # check if game is over
        if b.gameIsOver(cells):
            if type(player) == agents.Human:
                draw.gameOver(screen, WINDOW_SIZE, OFFSET)
            else:
                return score
        elif b.gameIsWon(cells):
            if type(player) == agents.Human:
                draw.gameWon(screen, WINDOW_SIZE, OFFSET)
        
        # display the rendered frame
        pygame.display.flip()

def runNoRender(player):
    
    cells = b.newBoard()
    score = 0
    running = True
    
    while running:

        # get and act on player move
        move = player.getMove(cells, score, [])

        if move == UP:
            score, changed = b.moveUp(cells, score)
            if changed:
                b.addNum(cells)
        elif move == DOWN:
            score, changed = b.moveDown(cells, score)
            if changed:
                b.addNum(cells)
        elif move == LEFT:
            score, changed = b.moveLeft(cells, score)
            if changed:
                b.addNum(cells)
        elif move == RIGHT:
            score, changed = b.moveRight(cells, score)
            if changed:
                b.addNum(cells)

        # check if game is over
        if b.gameIsOver(cells):
            return score