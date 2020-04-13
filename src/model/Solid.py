import pyglet

from OpenGL.GL import *

import pyglet.gl

from model.Collidable import Collidable
from model.Vector import Vector


class Solid(Collidable):
    model = [0, 0, 0, 0,
             0, 0, 0, 0,
             0, 0, 0, 0,
             0, 0, 0, 0]
    # model = (GLfloat * len(pymodel))(*pymodel)
    translate = [0, 0, 0]
    color = []

    def __init__(self, color, texture):
        self.batch = pyglet.graphics.Batch()
        self.color = color
        self.texture = self.load_texture(texture)

    def load_texture(self, file):
        image = pyglet.image.load('../resources/' + file)
        texture = pyglet.image.load('../resources/' + file).get_texture()
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        return pyglet.graphics.TextureGroup(texture)

    def set_position(self, translate: Vector,rotate_angle=0, rotate=Vector(0.0, 0.0, 0.0), scale=Vector(1.0, 1.0, 1.0)):
        self.translate = translate
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glScalef(scale.x, scale.y, scale.z)
        glRotatef(rotate_angle, rotate.x, rotate.y, rotate.z)
        glTranslatef(translate.x, translate.y, translate.z)

        self.model = glGetFloatv(GL_MODELVIEW_MATRIX, self.model)

    def rotate(self, rotate: Vector, angle):
        glMatrixMode(GL_MODELVIEW)
        # glLoadIdentity()
        glTranslatef(-self.translate.x, -self.translate.y, -self.translate.z)
        glRotatef(angle, rotate.x, rotate.y, rotate.z)
        glTranslatef(self.translate.x, self.translate.y, self.translate.z)
        self.model = glGetFloatv(GL_MODELVIEW_MATRIX, self.model)

    def draw(self):
        glColor3f(self.color[0], self.color[1], self.color[2])
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
        self.batch.draw()
