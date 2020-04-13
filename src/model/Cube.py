from OpenGL.GL import *

from model.Solid import Solid
from model.Vector import Vector
import pyglet.graphics


class Cube(Solid):
    size = 1
    cubeVertices = ((1, 1, 1),
                    (1, 1, -1),
                    (1, -1, -1),
                    (1, -1, 1),
                    (-1, 1, 1),
                    (-1, -1, -1),
                    (-1, -1, 1),
                    (-1, 1, -1))

    # vertices = pyglet.graphics.vertex_list(8, ('v3f', [1, 1, 1,
    #                                                    1, 1, -1,
    #                                                    1, -1, -1,
    #                                                    1, -1, 1,
    #                                                    -1, 1, 1,
    #                                                    -1, -1, -1,
    #                                                    -1, -1, 1,
    #                                                    -1, 1, -1]),
    #                                        ('c3b', [100,200,220])
    #                                        )

    cubeEdges = ((0, 1), (0, 3), (0, 4), (1, 2), (1, 7), (2, 5), (2, 3), (3, 6), (4, 6), (4, 7), (5, 6), (5, 7))
    textureCoords = (())
    normals = ((-1, 0, 0), (0, 1, 0), (1, 0, 0), (0, -1, 0), (0, 0, 1), (0, 0, 1))
    cubeQuads = ((0, 3, 6, 4),
                 (2, 5, 6, 3),
                 (1, 2, 5, 7),
                 (1, 0, 4, 7),
                 (7, 4, 6, 5),
                 (2, 3, 0, 1))
    # cubeTriangles = (
    #     (0, 2, 1), (1, 2, 3), (4, 5, 6), (5, 7, 6), (6, 7, 8), (7, 9, 8), (1, 3, 4), (3, 5, 4), (1, 11, 10), (1, 4, 11),
    #     (3, 12, 5), (5, 12, 13))
    model = [0, 0, 0, 0,
             0, 0, 0, 0,
             0, 0, 0, 0,
             0, 0, 0, 0]
    translate = [0, 0, 0]

    def __init__(self, color: list, texture):
        super().__init__()
        texture = self.get_texture(texture)
        texture_coords = ('t2f', (0, 0, 0.5, 0, 0.5, 0.5, 0, 0.5))

        colors = ('c3b', [color[0], color[1], color[2]] * 4)

        self.batch.add(4, GL_QUADS, texture, ('v3f', (1, -1, -1, -1, -1, -1, -1, 1, -1, 1, 1, -1)),
                       texture_coords)  # back
        self.batch.add(4, GL_QUADS, texture, ('v3f', (-1, -1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1)),
                       texture_coords)  # front
        self.batch.add(4, GL_QUADS, texture, ('v3f', (-1, -1, -1, -1, -1, 1, -1, 1, 1, -1, 1, -1)),
                       texture_coords)  # left
        self.batch.add(4, GL_QUADS, texture, ('v3f', (1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1)),
                       texture_coords)  # right
        self.batch.add(4, GL_QUADS, texture, ('v3f', (-1, -1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1)),
                       texture_coords)  # bottom
        self.batch.add(4, GL_QUADS, texture, ('v3f', (-1, 1, 1, 1, 1, 1, 1, 1, -1, -1, 1, -1)),
                       texture_coords)  # top

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
        self.color = color

    def get_texture(self, file):
        texture = super().get_texture(file)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
        return texture

    def set_position(self, translate: Vector):
        self.translate = translate
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(translate.x, translate.y, translate.z)
        self.model = glGetFloatv(GL_MODELVIEW_MATRIX, self.model)

    def rotate(self, rotate: Vector):
        glMatrixMode(GL_MODELVIEW)
        glTranslatef(-self.translate.x, -self.translate.y, -self.translate.z)
        glRotatef(1, rotate.x, rotate.y, rotate.z)
        glTranslatef(self.translate.x, self.translate.y, self.translate.z)
        self.model = glGetFloatv(GL_MODELVIEW_MATRIX, self.model)
        # self.model = glMultMatrixf(self.model)

    def draw(self):
        glColor3f(self.color[0], self.color[1], self.color[2])
        # glEnable(GL_TEXTURE_2D)
        # glBindTexture(GL_TEXTURE_2D, self.texture)
        self.batch.draw()
        # pyglet.graphics.draw(6, GL_QUADS, self.batch)

        # glColor3f(self.color[0], self.color[1], self.color[2])
        # glBegin(GL_QUADS)
        # # glDrawElements()
        # i = 0
        # for cubeQuad in self.cubeQuads:
        #     glNormal3dv(self.normals[i])
        #     glTexCoord2f(0, 0)
        #     glTexCoord2f(1, 0)
        #     glTexCoord2f(1, 1)
        #     glTexCoord2f(0, 1)
        #     for cubeVertex in cubeQuad:
        #         glVertex3fv(self.cubeVertices[cubeVertex])
        #     i += 1
        # glEnd()
