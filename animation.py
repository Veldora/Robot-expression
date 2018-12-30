import pygame


class Animation:

    def __init__(self, images, x, y, delay, loop=False):
        self.images = images
        self.x = x
        self.y = y
        self.image_index = 0
        self.time = 0
        self.delay = delay
        self.finished = False
        self.loop = loop

    def render(self, canvas):
        if not self.finished or self.loop:
            # 1. Display current image
            current_image = self.images[self.image_index]
            render_pos = (self.x, self.y)
            canvas.blit(current_image, render_pos)
            # 2. Check time
            now = pygame.time.get_ticks()
            if self.time == 0:
                self.time = now
            else:
                if now - self.time >= self.delay:
                    self.time = now
                    if self.image_index < len(self.images) - 1:
                        self.image_index += 1
                    elif self.loop:
                        self.image_index = 0
                    else:
                        self.finished = True
