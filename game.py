import pygame
import board as b
import drawGame as draw
import players

def run(player):
    WINDOW_SIZE = 480
    OFFSET = 80

    cells = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    cellSize = int(WINDOW_SIZE // 4)
    b.addNum(cells)
    b.addNum(cells)

    score = 0

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + OFFSET))
    clock = pygame.time.Clock()
    running = True


    while running:
        # react to buttom presses
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                running = False

        move = player.getMove(cells, events)

        if move == pygame.K_DOWN:
            score, changed = b.slideDown(cells, score)
            if changed:
                index = b.addNum(cells)
        elif move == pygame.K_UP:
            score, changed = b.slideUp(cells, score)
            if changed:
                b.addNum(cells)
        elif move == pygame.K_LEFT:
            score, changed = b.slideLeft(cells, score)
            if changed:
                b.addNum(cells)
        elif move == pygame.K_RIGHT:
            score, changed = b.slideRight(cells, score)
            if changed:
                b.addNum(cells)
        elif move == pygame.K_r:
            cells = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
            b.addNum(cells)
            b.addNum(cells)
            score = 0

        # display frame
        screen.fill("white")
        draw.drawBoard(screen, cells, WINDOW_SIZE, OFFSET, cellSize)
        draw.drawGrid(screen, cells, WINDOW_SIZE, OFFSET, cellSize)
        draw.drawScore(screen, score, WINDOW_SIZE, OFFSET)

        # check if game is over
        if b.gameIsWon(cells):
            if type(player) == players.Human:
                draw.gameWon(screen, WINDOW_SIZE, OFFSET)
            else:
                return
        elif b.gameIsOver(cells):
            if type(player) == players.Human:
                draw.gameOver(screen, WINDOW_SIZE, OFFSET)
            else:
                return
        
        # flip() the display to put your work on screen
        pygame.display.flip()