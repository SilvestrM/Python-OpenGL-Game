import pyglet

from OpenGL.GL import *

import pyglet.gl

from model.Collidable import Collidable
from model.Vector import Vector


class Solid:
    model = [0, 0, 0, 0,
             0, 0, 0, 0,
             0, 0, 0, 0,
             0, 0, 0, 0]
    # model = (GLfloat * len(pymodel))(*pymodel
    color = []
    position = Vector(0, 0, 0)

    def __init__(self, color, texture):
        super().__init__()
        self.batch = pyglet.graphics.Batch()
        self.color = color
        self.texture = self.load_texture(texture)

    def load_texture(self, file):
        if file:
            texture = pyglet.image.load('../resources/' + file).get_texture()
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
            return pyglet.graphics.TextureGroup(texture)
        return pyglet.image.Texture.create(250, 250)

    def set_position(self, translate: Vector, rotate_angle=0, rotate=Vector(0.0, 0.0, 0.0),
                     scale=Vector(1.0, 1.0, 1.0)):
        self.position = translate
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glScalef(scale.x, scale.y, scale.z)
        glRotatef(rotate_angle, rotate.x, rotate.y, rotate.z)
        glTranslatef(translate.x, translate.y, translate.z)

        self.model = glGetFloatv(GL_MODELVIEW_MATRIX, self.model)

    def rotate(self, rotate: Vector, angle):
        glMatrixMode(GL_MODELVIEW)
        # glLoadIdentity()
        glTranslatef(-self.position.x, -self.position.y, -self.position.z)
        glRotatef(angle, rotate.x, rotate.y, rotate.z)
        glTranslatef(self.position.x, self.position.y, self.position.z)
        self.model = glGetFloatv(GL_MODELVIEW_MATRIX, self.model)

    def draw(self):
        # glDisable(GL_TEXTURE_2D)
        # glColor3f(self.color[0], self.color[1], self.color[2])
        # self.draw_box()
        glEnable(GL_TEXTURE_2D)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
        self.batch.draw()
