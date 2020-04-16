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
    # placeNumbers(num_font)
    # showGrid()
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
                # pygame.draw.rect(SCREEN, BLACK, r)

        pygame.display.update()
        CLOCK.tick(60)


def boardOverlay():
    for x in range(WINDOW_SIZE//GRIDBOX_SIZE):
        for y in range(WINDOW_SIZE//GRIDBOX_SIZE):
            rect = pygame.Rect(x*GRIDBOX_SIZE, y*GRIDBOX_SIZE,
                               GRIDBOX_SIZE, GRIDBOX_SIZE)
            pygame.draw.rect(SCREEN, GRAY, rect)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)


def checkForMines(x, y, r, num_font):
    x = x//GRIDBOX_SIZE
    y = y//GRIDBOX_SIZE
    if gameBoard[y][x] == "*":
        print("Game Over")
    try:
        if realBoard[x][y-1] == "*":
            print(x, y-1)
    except IndexError:
        pass
    else:
        pygame.draw.rect(SCREEN, WHITE, r)
        n = num_font.render("1", True, BLACK)
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


def showGrid():
    for x in range(WINDOW_SIZE//GRIDBOX_SIZE):
        for y in range(WINDOW_SIZE//GRIDBOX_SIZE):
            rect = pygame.Rect(x*GRIDBOX_SIZE, y*GRIDBOX_SIZE,
                               GRIDBOX_SIZE, GRIDBOX_SIZE)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)


if __name__ == "__main__":
    main()


# def placeNumbers(num_font):
#     for x in range(ROWS+1):
#         for y in range(COLS+1):
#             # if realBoard[x-1][y-1] == "*":
#             #     font = num_font.render("1", True, BLACK)
#             #     rect = getGridRect(x*GRIDBOX_SIZE, y*GRIDBOX_SIZE)
#             #     SCREEN.blit(font, (rect.x, rect.y))
#             # if realBoard[x][y+1] == "*" or realBoard[x+1][y+1] == "*":
#             #     f = num_font.render("1", True, BLACK)
#             #     rect = getGridRect(x*GRIDBOX_SIZE, y*GRIDBOX_SIZE)
#             #     SCREEN.blit(f, (rect.x, rect.y))
#             try:
#                 if realBoard[x][y+1] == "*":
#                     f = num_font.render("1", True, BLACK)
#                     rect = getGridRect(x*GRIDBOX_SIZE, y*GRIDBOX_SIZE)
#                     SCREEN.blit(f, (rect.x, rect.y))
#             except IndexError:
#                 print(IndexError)
#             else:
#                 pass
