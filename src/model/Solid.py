import ctypes

import numpy
import pyglet

from OpenGL.GL import *

# from pyglet.gl import *

from model.Collidable import Collidable
from model.Vector import Vector
from utils.Utils import load_texture


class Solid:
    model = [0, 0, 0, 0,
             0, 0, 0, 0,
             0, 0, 0, 0,
             0, 0, 0, 0]
    # model = (GLfloat * len(pymodel))(*pymodel
    color = []
    position = Vector(0, 0, 0)
    sizes = [1, 1, 1]

    def __init__(self, color, texture):
        self.batch = pyglet.graphics.Batch()
        self.color = color
        self.texture = texture
        # self.texture = load_texture(texture)
        # print("Generating solid..." + str(self))

    def set_position(self, translate: Vector, rotate_angle=0, rotate=Vector(0.0, 0.0, 0.0),
                     scale=Vector(1.0, 1.0, 1.0)):
        self.position = translate
        self.sizes = [self.sizes[0] * scale.x, self.sizes[1] * scale.y, self.sizes[2] * scale.z]
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(translate.x, translate.y, translate.z)
        glRotatef(rotate_angle, rotate.x, rotate.y, rotate.z)
        glScalef(scale.x, scale.y, scale.z)

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
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
        self.texture.set_state()
        self.batch.draw()
        glDisable(GL_TEXTURE_2D)
