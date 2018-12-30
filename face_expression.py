from animation import Animation
import pygame


class Face_expression:

    def __init__(self):
        # list of mouth's images
        self.mouths = [pygame.image.load("images/mouth1.png"),
                       pygame.image.load("images/mouth2.png")]
        # mouth animation
        self.mouth_ani = Animation(self.mouths, 0, 609, 100, True)
        # face animation
        self.face_ani = Animation([pygame.image.load("images/face1.png"),
                                   pygame.image.load("images/face2.png")],
                                  0, 0, 300, True)
        # Loaded eye's image
        self.eye = pygame.image.load("images/eye.png")
        # Position of the middle point of the frame
        self.middle = (732, 394)
        # Default position of the eyes
        self.eyes_default = [(323, 284), (1148, 284)]
        # Position of the eyes
        self.eyes = [[323, 284], [1148, 284]]
        # eye niches's radius - eye's radius
        self.radius = 220 - 27

    # canvas: pygame canvas
    # mouth_animation: default is False
    # eye_follow: default is False
    # x_detect, y_detect: Position of the face, default is None
    def render(self, canvas, mouth_animation=False, eye_follow=False, x_detect=None, y_detect=None):
        # render face's animation
        self.face_ani.render(canvas)
        if mouth_animation:
            # render mouth's animation
            self.mouth_ani.render(canvas)
        if eye_follow:
            # check the default values
            if x_detect is None or y_detect is None:
                destination = (0, 0)
            else:
                # the destination's position from the middle of eye niches
                destination = ((x_detect - self.middle[0]) * self.radius / self.middle[0],
                               (y_detect - self.middle[1]) * self.radius / self.middle[1])
            # the distance between destination and eyes pos
            distance = (abs(destination[0] - (self.eyes[0][0] - self.eyes_default[0][0])),
                        abs(destination[1] - (self.eyes[0][1] - self.eyes_default[0][1])))
            # validate
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
        # blit
        canvas.blit(self.eye, (self.eyes[0][0] - 27, self.eyes[0][1] - 27))
        canvas.blit(self.eye, (self.eyes[1][0] - 27, self.eyes[1][1] - 27))
