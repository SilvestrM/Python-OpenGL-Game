from OpenGL.GL import *

from model.Solid import Solid
from model.Vector import Vector


class Panel(Solid):
    def __init__(self, color, texture="", size=1):
        super().__init__(color, texture)
        texture_coords = ('t2f', (0, 0, 1, 0, 1, 1, 0, 1))

        self.batch.add(4, GL_QUADS, self.texture,
                       ('v3f', (-size, -size, -size, size, -size, -size, size, size, -size, -size, size, -size)),
                       ('n3f', (0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1)),
                       texture_coords)  # top
        self.batch.add(4, GL_QUADS, self.texture,
                       ('v3f', (size, -size, -size, -size, -size, -size, -size, size, -size, size, size, -size)),
                       ('n3f', (0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1)),
                       texture_coords)  # bottom

    def set_position(self, translate: Vector, rotate_angle=0, rotate=Vector(0.0, 0.0, 0.0),
                     scale=Vector(1.0, 1.0, 1.0)):
        super().set_position(translate, rotate_angle, rotate, scale)

        # self.bounding_box = BoundingBox(self.position, self.sizes[0], self.sizes[1], 0.05)
