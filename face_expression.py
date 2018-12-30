from animation import Animation
import pygame


class Face_expression:

    def __init__(self):
        self.mouths = [pygame.image.load("images/mouth1.png"),
                       pygame.image.load("images/mouth2.png")]
        self.mouth_ani = Animation(self.mouths, 0, 609, 100, True)
        self.face_ani = Animation([pygame.image.load("images/face1.png"),
                                   pygame.image.load("images/face2.png")],
                                  0, 0, 300, True)
        self.eye = pygame.image.load("images/eye.png")
        self.middle = (732, 394)
        self.eyes_default = [(323, 284), (1148, 284)]
        self.eyes = [[323, 284], [1148, 284]]
        self.radius = 220 - 27

    def render(self, canvas, mouth_animation=False, eye_follow=False, x_detect=None, y_detect=None):
        self.face_ani.render(canvas)
        if mouth_animation:
            self.mouth_ani.render(canvas)
        if eye_follow:
            if x_detect is None or y_detect is None:
                destination = (0, 0)
            else:
                destination = ((x_detect - self.middle[0]) * self.radius / self.middle[0],
                               (y_detect - self.middle[1]) * self.radius / self.middle[1])
            distance = (abs(destination[0] - (self.eyes[0][0] - self.eyes_default[0][0])),
                        abs(destination[1] - (self.eyes[0][1] - self.eyes_default[0][1])))
            if distance[0] != 0 and distance[1] != 0:
                if distance[0] < distance[1]:
                    if self.eyes[0][1] - self.eyes_default[0][1] > destination[1]:
                        self.eyes[0][1] -= 1
                        self.eyes[1][1] -= 1
                    elif self.eyes[0][1] - self.eyes_default[0][1] < destination[1]:
                        self.eyes[0][1] += 1
                        self.eyes[1][1] += 1
                else:
                    if self.eyes[0][0] - self.eyes_default[0][0] > destination[0]:
                        self.eyes[0][0] -= 1
                        self.eyes[1][0] -= 1
                    elif self.eyes[0][0] - self.eyes_default[0][0] < destination[0]:
                        self.eyes[0][0] += 1
                        self.eyes[1][0] += 1
        else:
            self.eyes = [[323, 284], [1148, 284]]
        canvas.blit(self.eye, (self.eyes[0][0] - 27, self.eyes[0][1] - 27))
        canvas.blit(self.eye, (self.eyes[1][0] - 27, self.eyes[1][1] - 27))
