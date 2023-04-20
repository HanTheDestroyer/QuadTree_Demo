from settings import *
from random import uniform, randint


class Particle:
    def __init__(self, position=None, velocity=None, radius=None, color=None,
                 acceleration=None, static=None, mass=None):

        if position is None:
            self.position = pygame.Vector2(randint(max_radius * 2, int(resolution[0] - max_radius)),
                                           randint(max_radius * 2, int(resolution[1] - max_radius)))
        else:
            self.position = pygame.Vector2(position)

        if velocity is None:
            self.velocity = pygame.Vector2(uniform(-max_velocity, max_velocity), uniform(-max_velocity, max_velocity))
        else:
            self.velocity = pygame.Vector2(velocity)

        if radius is None:
            self.radius = randint(min_radius, max_radius)
        else:
            self.radius = radius

        if color is None:
            self.color = pygame.Color("red")
        else:
            self.color = color

        if acceleration is None:
            self.acceleration = pygame.Vector2(0, 0)
        else:
            self.acceleration = acceleration

        if static is None:
            self.static = False
        else:
            self.static = static

        if mass is None:
            self.mass = self.radius ** 2
        else:
            self.mass = mass

        self.quadrant = ""

    def move(self):
        self.position += self.velocity
        

    def __lt__(self, other):
        return self.position[0] < other.position[0]

    def __le__(self, other):
        return self.position[0] <= other.position[0]

    def __eq__(self, other):
        return self.position[0] == other.position[0]

    def __ne__(self, other):
        return self.position[0] != other.position[0]

    def __gt__(self, other):
        return self.position[0] > other.position[0]

    def __ge__(self, other):
        return self.position[0] >= other.position[0]

    def __add__(self, other):
        return self.position[0] + other.position[0]

    def __sub__(self, other):
        return self.position[0] - other.position[0]

    def __repr__(self):
        return "{}".format("p")

    def __str__(self):
        return "{}".format(self.position)