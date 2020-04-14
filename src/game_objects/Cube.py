from OpenGL.GL import *
# from pyglet.gl import *

from model.Solid import Solid
from model.Vector import Vector
import pyglet.graphics


class Cube(Solid):

    def __init__(self, color: list, texture=""):
        super().__init__(color, texture)
        texture_coords = ('t2f', (0, 0, 0.5, 0, 0.5, 0.5, 0, 0.5))

        self.bounding_box = 2


        colors = ('c3f', [color[0], color[1], color[2]] * 4)

        vertices = ('v3f', (1, -1, -1, -1, -1, -1, -1, 1, -1, 1, 1, -1))
        self.batch.add(4, GL_QUADS, self.texture, vertices, colors, texture_coords)  # bottom
        self.batch.add(4, GL_QUADS, self.texture, ('v3f', (-1, -1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1)),
                       texture_coords)  # top
        self.batch.add(4, GL_QUADS, self.texture, ('v3f', (-1, -1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1,)),
                       texture_coords)  # left
        self.batch.add(4, GL_QUADS, self.texture, ('v3f', (1, -1, -1, 1, 1, -1, 1, 1, 1, 1, -1, 1,)),
                       texture_coords)  # right
        self.batch.add(4, GL_QUADS, self.texture, ('v3f', (-1, -1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1)),
                       texture_coords)  # back
        self.batch.add(4, GL_QUADS, self.texture, ('v3f', (-1, 1, 1, 1, 1, 1, 1, 1, -1, -1, 1, -1)),
                       texture_coords)  # front

        # colors = ('c3b', [color[0], color[1], color[2]] * 8)
        # # texture = ('c3b', [color.x, color.y, color.z] * 8)
        # self.batch.add(8, GL_QUADS, ('v3f', [1, 1, 1,
        #                                      1, 1, -1,
        #                                      1, -1, -1,
        #                                      1, -1, 1,
        #                                      -1, 1, 1,
        #                                      -1, -1, -1,
        #                                      -1, -1, 1,
        #                                      -1, 1, -1]), colors)

    # def get_texture(self, file):
    #     texture = super().get_texture(file)
    #     glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    #     glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    #     glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
    #     return texture
    #     # self.model = glMultMatrixf(self.model)

    def draw(self):
        glDisable(GL_TEXTURE_2D)
        glColor3f(self.color[0], self.color[1], self.color[2])
        self.draw_box()
        super().draw()


    # def draw(self):
    #
    #     # glEnable(GL_TEXTURE_2D)
    #     # glBindTexture(GL_TEXTURE_2D, self.texture)
    #     self.batch.draw()
    #     # pyglet.graphics.draw(6, GL_QUADS, self.batch)
    #
    #     # glColor3f(self.color[0], self.color[1], self.color[2])
    #     # glBegin(GL_QUADS)
    #     # # glDrawElements()
    #     # i = 0
    #     # for cubeQuad in self.cubeQuads:
    #     #     glNormal3dv(self.normals[i])
    #     #     glTexCoord2f(0, 0)
    #     #     glTexCoord2f(1, 0)
    #     #     glTexCoord2f(1, 1)
    #     #     glTexCoord2f(0, 1)
    #     #     for cubeVertex in cubeQuad:
    #     #         glVertex3fv(self.cubeVertices[cubeVertex])
    #     #     i += 1
    #     # glEnd()
