import pygame
import board as b
import drawGame as draw
import agents

# runs the game for given agent
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    cells = b.newBoard()
                    score = 0

        # get next move
        if type(player) == agents.Human:
            moveDir = player.getMove(events)
        elif isinstance(player, agents.Agent):
            moveDir = player.getMove(cells, score)
        else:
            raise TypeError("input player is not a valid player")
        
        # execute move
        if moveDir in [b.Dir.UP, b.Dir.DOWN, b.Dir.LEFT, b.Dir.RIGHT]:
            score, changed = b.move(cells, score, moveDir)
            if changed:
                b.addNum(cells)

        # display frame
        screen.fill("white")
        draw.drawBoard(screen, cells, OFFSET, cellSize)
        draw.drawGrid(screen, OFFSET, cellSize)
        draw.drawScore(screen, score, OFFSET)

        # check if game is over
        if b.gameIsOver(cells):
            draw.gameOver(screen, WINDOW_SIZE, OFFSET)
        elif b.gameIsWon(cells):
            draw.gameWon(screen, WINDOW_SIZE, OFFSET)
        
        # display the rendered frame
        pygame.display.flip()

# runs a game without rendering visuals
# not designed for human players
def runNoRender(agent):
    
    cells = b.newBoard()
    score = 0
    running = True
    
    while running:

        # get and act on agent move
        moveDir = agent.getMove(cells, score)

        if moveDir in [b.Dir.UP, b.Dir.DOWN, b.Dir.LEFT, b.Dir.RIGHT]:
            score, changed = b.move(cells, score, moveDir)
            if changed:
                b.addNum(cells)

        # check if game is over
        if b.gameIsOver(cells):
            return score, b.gameIsWon(cells)