from face_expression import Face_expression
import pygame
from pygame.locals import *


clock = pygame.time.Clock()
pygame.init()
canvas = pygame.display.set_mode((1464,788))

def main():
    test = True
    fe = Face_expression()
    while test:
        fe.render(canvas, True, True, 100, 100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
        clock.tick(60)

if __name__ == "__main__":
    main()
