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

realBoard = [[False]*COLS for i in range(ROWS)]
gameBoard = [[False]*COLS for i in range(ROWS)]


def main():
    global SCREEN, CLOCK
    SCREEN = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("MINESWEEPER")
    CLOCK = pygame.time.Clock()
    pygame.init()
    SCREEN.fill(WHITE)
    showGrid()
    placeMines()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                r = getGridRect(x, y)
                pygame.draw.rect(SCREEN, BLACK, r)

        pygame.display.update()
        CLOCK.tick(60)


def placeMines():
    for i in range(MINES+1):
        mine_x = random.randrange(WINDOW_SIZE)
        mine_y = random.randrange(WINDOW_SIZE)
        r = getGridRect(mine_x, mine_y)
        print(r)
        x = mine_x//GRIDBOX_SIZE
        y = mine_y//GRIDBOX_SIZE
        realBoard[y][x] = True
        pygame.draw.rect(SCREEN, GREEN, r)
    print(realBoard)


def getGridRect(x, y):
    rect = pygame.Rect(0, 0, GRIDBOX_SIZE, GRIDBOX_SIZE)
    for i in range(0, (x//GRIDBOX_SIZE)+1):
        for j in range(0, (y//GRIDBOX_SIZE)+1):
            rect = pygame.Rect(i*GRIDBOX_SIZE, j*GRIDBOX_SIZE,
                               GRIDBOX_SIZE, GRIDBOX_SIZE)
    return rect


def showGrid():
    for x in range(WINDOW_SIZE//GRIDBOX_SIZE):
        for y in range(WINDOW_SIZE//GRIDBOX_SIZE):
            rect = pygame.Rect(x*GRIDBOX_SIZE, y*GRIDBOX_SIZE,
                               GRIDBOX_SIZE, GRIDBOX_SIZE)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)


if __name__ == "__main__":
    main()
