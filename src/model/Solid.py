import pyglet

from pyglet.gl import *
from model.Vector import Vector


class Solid():
    model = []
    color = []

    def __init__(self):
        self.batch = pyglet.graphics.Batch()

    def get_texture(self, file):
        texture = pyglet.image.load('../resources/' + file).get_texture()
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        return pyglet.graphics.TextureGroup(texture)

    def draw(self):
        pass
        self.batch.draw()
