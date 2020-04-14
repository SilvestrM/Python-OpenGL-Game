from OpenGL.GL import *

from model.Solid import Solid
from model.Vector import Vector


class Panel(Solid):
    def __init__(self, color, texture=""):
        super().__init__(color, texture)
        texture_coords = ('t2f', (0, 0, 0.5, 0, 0.5, 0.5, 0, 0.5))

        size = 2
        self.bounding_box = Vector(size, size, 0)

        colors = ('c3b', [color[0], color[1], color[2]] * 4)

        self.batch.add(4, GL_QUADS, self.texture, ('v3f', (0, 0, 0, size, 0, 0, size, size, 0, 0, size, 0)),
                       texture_coords)  # front
        # self.batch.add(4, GL_QUADS, self.texture, ('v3f', (1, -1, -1, -1, -1, -1, -1, 1, -1, 1, 1, -1)),
        #                texture_coords)  # bottom

    # def get_texture(self, file):
    #     texture = super().__init__(file)
    #     glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    #     glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    #     glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
    #     # glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    #     # glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    #     return texture
