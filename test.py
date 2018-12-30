from face_expression import Face_expression
import pygame
from pygame.locals import *
from os import sys


clock = pygame.time.Clock()
pygame.init()
canvas = pygame.display.set_mode((1464,788))

def main():
    test = True
    # Initializr Face_expression
    fe = Face_expression()
    while test:
        # render
        fe.render(canvas)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
        clock.tick(60)

if __name__ == "__main__":
    main()
