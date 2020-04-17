import pygame
import sys
import random


WINDOW_SIZE = 400
GRIDBOX_SIZE = 40
MINES = 10
ROWS = 10
COLS = 10

# RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (20, 200, 20)
GRAY = (140, 140, 140)

realBoard = [["-"]*COLS for i in range(ROWS)]
gameBoard = [["-"]*COLS for i in range(ROWS)]


def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("MINESWEEPER")
    CLOCK = pygame.time.Clock()
    SCREEN.fill(WHITE)

    num_font = pygame.font.SysFont("Helvetica", 30)

    placeMines()
    boardOverlay()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                r = getGridRect(x, y)
                checkForMines(x, y, r, num_font)

        pygame.display.update()
        CLOCK.tick(60)


def boardOverlay():
    for x in range(WINDOW_SIZE//GRIDBOX_SIZE):
        for y in range(WINDOW_SIZE//GRIDBOX_SIZE):
            rect = pygame.Rect(x*GRIDBOX_SIZE, y*GRIDBOX_SIZE,
                               GRIDBOX_SIZE, GRIDBOX_SIZE)
            pygame.draw.rect(SCREEN, GRAY, rect)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)


def isValidMove(x, y):
    if x >= 0 and y >= 0:
        try:
            if realBoard[x][y] == "*":
                return True
        except IndexError:
            return False
        else:
            return False
    else:
        return False


def checkForMines(x, y, r, num_font):
    x = x//GRIDBOX_SIZE
    y = y//GRIDBOX_SIZE
    count = 0
    if gameBoard[x][y] == "*":
        print("Game Over")
    elif gameBoard[x][y] != "*":
        if isValidMove(x, y-1):
            count = count + 1
        if isValidMove(x, y+1):
            count = count + 1
        if isValidMove(x+1, y):
            count = count + 1
        if isValidMove(x-1, y):
            count = count + 1
        if isValidMove(x-1, y-1):
            count = count + 1
        if isValidMove(x+1, y+1):
            count = count + 1
        if isValidMove(x-1, y+1):
            count = count + 1
        if isValidMove(x+1, y-1):
            count = count + 1
        pygame.draw.rect(SCREEN, WHITE, r)
        n = num_font.render(str(count), True, BLACK)
        SCREEN.blit(n, r)


def placeMines():
    for i in range(MINES+1):
        mine_x = random.randrange(40, WINDOW_SIZE)
        mine_y = random.randrange(40, WINDOW_SIZE)
        r = getGridRect(mine_x, mine_y)
        x = mine_x//GRIDBOX_SIZE
        y = mine_y//GRIDBOX_SIZE
        realBoard[y][x] = "*"
        gameBoard[y][x] = "*"
        pygame.draw.rect(SCREEN, GREEN, r)


def getGridRect(x, y):
    rect = pygame.Rect(0, 0, GRIDBOX_SIZE, GRIDBOX_SIZE)
    for i in range(0, (x//GRIDBOX_SIZE)+1):
        for j in range(0, (y//GRIDBOX_SIZE)+1):
            rect = pygame.Rect(i*GRIDBOX_SIZE, j*GRIDBOX_SIZE,
                               GRIDBOX_SIZE, GRIDBOX_SIZE)
    return rect


if __name__ == "__main__":
    main()
