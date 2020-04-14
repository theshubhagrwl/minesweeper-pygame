import pygame
import sys

WINDOW_SIZE = 400
GRIDBOX_SIZE = 20

# RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def main():
    global SCREEN, CLOCK
    SCREEN = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    CLOCK = pygame.time.Clock()
    pygame.init()
    SCREEN.fill(BLACK)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()

        showGrid()
        pygame.display.update()
        CLOCK.tick(60)


def showGrid():
    for x in range(WINDOW_SIZE//GRIDBOX_SIZE):
        for y in range(WINDOW_SIZE//GRIDBOX_SIZE):
            rect = pygame.Rect(x*GRIDBOX_SIZE, y*GRIDBOX_SIZE,
                               GRIDBOX_SIZE, GRIDBOX_SIZE)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)


if __name__ == "__main__":
    main()
