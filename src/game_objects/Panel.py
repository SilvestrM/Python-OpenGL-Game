from OpenGL.GL import *

from model.BoundingBox import BoundingBox
from model.Solid import Solid
from model.Vector import Vector


class Panel(Solid):
    def __init__(self, color, texture=""):
        super().__init__(color, texture)
        texture_coords = ('t2f', (0, 0, 0.5, 0, 0.5, 0.5, 0, 0.5))

        size = 1
        self.bounding_box = BoundingBox(self.position, size, size, 0.01)

        colors = ('c3b', [color[0], color[1], color[2]] * 4)

        self.batch.add(4, GL_QUADS, self.texture, ('v3f', (-size, -size, -size, size, -size, -size, size, size, -size, -size, size, -size)),
                       texture_coords)  # front
        # self.batch.add(4, GL_QUADS, self.texture, ('v3f', (1, -1, -1, -1, -1, -1, -1, 1, -1, 1, 1, -1)),
        #                texture_coords)  # bottom

    def set_position(self, translate: Vector, rotate_angle=0, rotate=Vector(0.0, 0.0, 0.0),
                     scale=Vector(1.0, 1.0, 1.0)):
        super().set_position(translate, rotate_angle, rotate, scale)

        self.bounding_box = BoundingBox(self.position, scale.x, scale.y, 0.01)
