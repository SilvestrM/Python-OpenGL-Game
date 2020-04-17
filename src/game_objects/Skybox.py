import pyglet
from OpenGL.GL import *

from model.Solid import load_texture
from utils.Utils import load_cubemap_texture


class Skybox:
    def __init__(self, texture):
        self.batch = pyglet.graphics.Batch()
        test_tex = load_cubemap_texture("skybox1.png")
        # glBindTexture(GL_TEXTURE_CUBE_MAP, glGenTextures(1))
        # glTexParameterf(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_S, GL_REPEAT)
        texture_coords = ('t2f', (0, 0, 1, 0, 1, 1, 0, 1))
        size = 250
        normals = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]

        self.batch.add(4, GL_QUADS, test_tex,
                       ('v3f', (size, -size, -size, -size, -size, -size, -size, size, -size, size, size, -size)),
                       ('n3f', (0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1)),
                       texture_coords)  # bottom
        self.batch.add(4, GL_QUADS, load_texture("skb1maxz.png"),
                       ('v3f', (-size, -size, size, size, -size, size, size, size, size, -size, size, size)),
                       ('n3f', (0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1)),
                       texture_coords)  # top
        self.batch.add(4, GL_QUADS, load_texture("skb1minx.png"),
                       ('v3f', (-size, -size, size, -size, size, size, -size, size, -size, -size, -size, -size,)),
                       ('n3f', (1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0)),
                       texture_coords)  # left
        self.batch.add(4, GL_QUADS, load_texture("skb1maxx.png"),
                       ('v3f', (size, -size, -size, size, size, -size, size, size, size, size, -size, size,)),
                       ('n3f', (1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0)),
                       texture_coords)  # right
        self.batch.add(4, GL_QUADS, load_texture("skb1miny.png"),
                       ('v3f', (-size, -size, -size, size, -size, -size, size, -size, size, -size, -size, size)),
                       ('n3f', (0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0)),
                       texture_coords)  # back
        self.batch.add(4, GL_QUADS, load_texture("skb1maxy.png"),
                       ('v3f', (-size, size, size, size, size, size, size, size, -size, -size, size, -size)),
                       ('n3f', (0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0)),
                       texture_coords)  # front

    def draw(self):
        glDisable(GL_TEXTURE_2D)
        glEnable(GL_TEXTURE_CUBE_MAP)
        # glBindTexture(GL_TEXTURE_CUBE_MAP, self.texture)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
        self.batch.draw()
        glDisable(GL_TEXTURE_CUBE_MAP)
