import pyglet

from OpenGL.GL import *
from OpenGL.raw.GL.EXT.texture_cube_map import GL_REFLECTION_MAP_EXT

from model.Solid import load_texture
from utils.Utils import load_cubemap_texture


def get_st(sc, tc, ma):
    s = (sc / abs(ma) + 1) / 2
    t = (tc / abs(ma) + 1) / 2
    return s, t


class Skybox:
    def __init__(self, texture):
        self.batch = pyglet.graphics.Batch()
        # texture_map = load_cubemap_texture("skybox2.jpg")
        self.texture_id = load_cubemap_texture("sbx_2")
        # self.textures = texture_map
        # glBindTexture(GL_TEXTURE_CUBE_MAP, glGenTextures(1))
        # glTexParameterf(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_S, GL_REPEAT)
        texture_coords = ('t2f', (0, 0, 1, 0, 1, 1, 0, 1))
        size = 250
        normals = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]
        print(get_st(0,0,1))

        self.bottom = pyglet.graphics.Batch().add(4, GL_QUADS, None,
                       ('v3f', (-size, -size, -size, size, -size, -size, size, size, -size, -size, size, -size)),
                       ('n3f', (0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1)),
                       ('t3f', ( 1, 1, -1,
                                -1, 1, -1,
                                -1, -1, -1,
                                1, -1, -1)))  # bottom
        self.top = pyglet.graphics.Batch().add(4, GL_QUADS, None,
                       ('v3f', (-size, -size, size, size, -size, size, size, size, size, -size, size, size)),
                       ('n3f', (0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1)),
                       ('t3f', (-1, -1, 1,
                                1, -1, 1,
                                1, 1, 1,
                                -1, 1, 1)))  # top
        self.left = pyglet.graphics.Batch().add(4, GL_QUADS, None,
                       ('v3f', (-size, -size, -size, -size, size, -size, -size, size, size, -size, -size, size,)),
                       ('n3f', (-1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0)),
                       ('t3f', (-1, -1, 1,
                                -1, -1, -1,
                                -1, 1, -1,
                                -1, 1, 1,)))  # left
        self.right = pyglet.graphics.Batch().add(4, GL_QUADS, None,
                       ('v3f', (size, -size, -size, size, size, -size, size, size, size, size, -size, size,)),
                       ('n3f', (1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0)),
                       ('t3f', (1, -1, 1,
                                1, -1, -1,
                                1, 1, -1,
                                1, 1, 1
                                )))  # right
        self.back = pyglet.graphics.Batch().add(4, GL_QUADS, None,
                       ('v3f', (-size, -size, -size, size, -size, -size, size, -size, size, -size, -size, size)),
                       ('n3f', (0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0)),
                       ('t3f', (-1, 1, 1,
                                1, 1, 1,
                                1, 1, -1,
                                -1, 1, -1,)))  # back
        self.front = pyglet.graphics.Batch().add(4, GL_QUADS, None,
                       ('v3f', (-size, size, size, size, size, size, size, size, -size, -size, size, -size)),
                       ('n3f', (0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0)),
                       ('t3f', (1, -1, 1,
                                -1, -1, 1,
                                -1, -1, -1,
                                1, -1,-1,)))  # front

    def draw(self):
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
        glEnable(GL_TEXTURE_CUBE_MAP)

        glBindTexture(GL_TEXTURE_CUBE_MAP, self.texture_id)

        glTexParameterf(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameterf(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_R, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        # glTexGenfv(GL_S, GL_TEXTURE_GEN_MODE, GL_NORMAL_MAP)
        # glTexGenfv(GL_T, GL_TEXTURE_GEN_MODE, GL_NORMAL_MAP)
        # glTexGenfv(GL_R, GL_TEXTURE_GEN_MODE, GL_NORMAL_MAP)
        # glEnable(GL_TEXTURE_GEN_S)
        # glEnable(GL_TEXTURE_GEN_T)
        # glEnable(GL_TEXTURE_GEN_R)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
        glColor3f(0.93, 0.89, 0.57)
        glMatrixMode(GL_TEXTURE)

        glPushMatrix()
        glLoadIdentity()
        glRotatef(0, 0, 0, 1)
        self.bottom.draw(GL_QUADS)
        glPopMatrix()

        glPushMatrix()
        glLoadIdentity()
        glRotatef(0, 0, 0, 1)
        self.top.draw(GL_QUADS)
        glPopMatrix()

        glPushMatrix()
        glLoadIdentity()
        glRotatef(0, 1, 0, 0)
        self.left.draw(GL_QUADS)
        glPopMatrix()

        glPushMatrix()
        glLoadIdentity()
        glRotatef(0, 1, 0, 0)
        self.right.draw(GL_QUADS)
        glPopMatrix()

        glPushMatrix()
        glLoadIdentity()
        glRotatef(0, 0, 1, 0)
        self.back.draw(GL_QUADS)
        glPopMatrix()

        glPushMatrix()
        glLoadIdentity()
        glRotatef(0, 0, 1, 0)
        self.front.draw(GL_QUADS)
        glPopMatrix()


        self.batch.draw()
        # glDisable(GL_TEXTURE_GEN_S)
        # glDisable(GL_TEXTURE_GEN_T)
        # glDisable(GL_TEXTURE_GEN_R)
        glDisable(GL_TEXTURE_CUBE_MAP)
