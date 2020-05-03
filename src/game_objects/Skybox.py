import pyglet

from OpenGL.GL import *

from utils.Utils import load_cubemap_texture


def get_st(sc, tc, ma):
    s = (sc / abs(ma) + 1) / 2
    t = (tc / abs(ma) + 1) / 2
    return s, t


class Skybox:
    # Skybox class

    def __init__(self, flavor, texture):
        self.rotation = 0
        self.batch = pyglet.graphics.Batch()
        self.texture_id = load_cubemap_texture(texture)

        size = 50
        normals = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]

        color = ('c4f', flavor * 4)

        self.bottom = pyglet.graphics.Batch() \
            .add(4, GL_QUADS, None,
                 ('v3f', (
                     -size, -size, -size, size, -size, -size, size, size, -size, -size,
                     size, -size)),
                 ('n3f', (0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1)),
                 color,
                 ('t3f', (1, 1, -1,
                          -1, 1, -1,
                          -1, -1, -1,
                          1, -1, -1)))
        # bottom
        self.top = pyglet.graphics.Batch() \
            .add(4, GL_QUADS, None,
                 ('v3f', (
                     -size, -size, size, size, -size, size, size, size, size, -size, size,
                     size)),
                 ('n3f', (0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1)),
                 color,
                 ('t3f', (-1, -1, 1,
                          1, -1, 1,
                          1, 1, 1,
                          -1, 1, 1)))
        # top
        self.left = pyglet.graphics.Batch() \
            .add(4, GL_QUADS, None,
                 ('v3f', (
                     -size, -size, -size, -size, size, -size, -size, size, size, -size,
                     -size, size,)),
                 ('n3f', (-1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0)),
                 color,
                 ('t3f', (-1, 1, -1,
                          -1, 1, 1,
                          -1, -1, 1,
                          -1, -1, -1,)))
        # left
        self.right = pyglet.graphics.Batch() \
            .add(4, GL_QUADS, None,
                 ('v3f', (
                     size, -size, -size, size, size, -size, size, size, size, size,
                     -size,
                     size,)),
                 ('n3f', (1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0)),
                 color,
                 ('t3f', (1, 1, -1,
                          1, 1, 1,
                          1, -1, 1,
                          1, -1, -1,
                          )))
        # right
        self.back = pyglet.graphics.Batch() \
            .add(4, GL_QUADS, None,
                 ('v3f', (
                     -size, -size, -size, size, -size, -size, size, -size, size, -size,
                     -size, size)),
                 ('n3f', (0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0)),
                 color,
                 ('t3f', (
                     1, -1, 1,
                     -1, -1, 1,
                     -1, -1, -1,
                     1, -1, -1,
                 )))
        # back
        self.front = pyglet.graphics.Batch() \
            .add(4, GL_QUADS, None,
                 ('v3f', (
                     -size, size, size, size, size, size, size, size, -size, -size,
                     size,
                     -size)),
                 ('n3f', (0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0)),
                 color,
                 ('t3f', (
                     -1, 1, 1,
                     1, 1, 1,
                     1, 1, -1,
                     -1, 1, -1,)))
        # front

    def rotate(self):
        # Atmospheric slow rotation

        self.rotation += 0.05
        return self.rotation

    def draw(self):
        glEnable(GL_TEXTURE_CUBE_MAP)

        glBindTexture(GL_TEXTURE_CUBE_MAP, self.texture_id)

        glTexParameterf(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameterf(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_R, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_COMBINE)
        glTexEnvf(GL_TEXTURE_ENV, GL_COMBINE_RGB, GL_ADD_SIGNED)

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

        # self.batch.draw()
        glDisable(GL_TEXTURE_CUBE_MAP)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
