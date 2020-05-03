from OpenGL.GL import *

from model.BoundingBox import BoundingBox
from model.Collidable import Collidable
from model.Solid import Solid


class Cube(Solid, Collidable):

    def __init__(self, color: list, texture="", size=1):
        super().__init__(color, texture)

        texture_coords = ('t2f', (0, 0, 1, 0, 1, 1, 0, 1))

        colors = ('c3f', [color[0], color[1], color[2]] * 4)
        self.sizes = [size, size, size]
        self.center_dist = 0

        self.batch.add(4, GL_QUADS, self.texture,
                       ('v3f', (size, -size, -size, -size, -size, -size, -size, size, -size, size, size, -size)),
                       ('n3f', (0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1)),
                       texture_coords)  # bottom
        self.batch.add(4, GL_QUADS, self.texture,
                       ('v3f', (-size, -size, size, size, -size, size, size, size, size, -size, size, size)),
                       ('n3f', (0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1)),
                       texture_coords)  # top
        self.batch.add(4, GL_QUADS, self.texture,
                       ('v3f', (-size, size, -size, -size, -size, -size, -size, -size, size, -size, size, size,)),
                       ('n3f', (-1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0)),
                       texture_coords)  # left
        self.batch.add(4, GL_QUADS, self.texture,
                       ('v3f', (size, -size, -size, size, size, -size, size, size, size, size, -size, size,)),
                       ('n3f', (1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0)),
                       texture_coords)  # right
        self.batch.add(4, GL_QUADS, self.texture,
                       ('n3f', (0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0)),
                       ('v3f', (-size, -size, -size, size, -size, -size, size, -size, size, -size, -size, size)),
                       texture_coords)  # back
        self.batch.add(4, GL_QUADS, self.texture,
                       ('v3f', (size, size, -size, -size, size, -size, -size, size, size, size, size, size)),
                       ('n3f', (0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0)),
                       texture_coords)  # front

    def set_position(self, *args, **kwargs):
        super().set_position(*args, **kwargs)
        self.bounding_box = BoundingBox(self.position, self.sizes[0], self.sizes[1], self.sizes[2])
