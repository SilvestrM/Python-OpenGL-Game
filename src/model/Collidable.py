import math

import pyglet
import pyglet.gl

from model.BoundingBox import BoundingBox
from model.Vector import Vector


class Collidable:
    bounding_box: BoundingBox = None

    def draw_box(self):
        pass
        # pyglet.graphics.draw(4, pyglet.gl.GL_LINE_LOOP, ('v3f', self.box_faces[0]))
        # pyglet.graphics.draw(4, pyglet.gl.GL_LINE_LOOP, ('v3f', self.box_faces[1]))
        # pyglet.graphics.draw(4, pyglet.gl.GL_LINE_LOOP, ('v3f', self.box_faces[2]))
        # pyglet.graphics.draw(4, pyglet.gl.GL_LINE_LOOP, ('v3f', self.box_faces[3]))
        # pyglet.graphics.draw(4, pyglet.gl.GL_LINE_LOOP, ('v3f', self.box_faces[4]))
        # pyglet.graphics.draw(4, pyglet.gl.GL_LINE_LOOP, ('v3f', self.box_faces[5]))
