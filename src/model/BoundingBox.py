
from model.Vector import Vector


class BoundingBox:
    def __init__(self, position, size_x, size_y, size_z):
        self.size_x = size_x
        self.size_y = size_y
        self.size_z = size_z

        self.min_x, self.min_y, self.min_z = position.x - size_x, position.y - size_y, position.z - size_z
        self.max_x, self.max_y, self.max_z = position.x + size_x, position.y + size_y, position.z + size_z

        # min_x, min_y
        # min_x, max_y
        self.corners = [
            (self.min_x, self.min_y, self.min_z),
            (self.min_x, self.max_y, self.min_z),
            (self.max_x, self.min_y, self.min_z),
            (self.max_x, self.max_y, self.min_z),
            (self.min_x, self.min_y, self.max_z),
            (self.min_x, self.max_y, self.max_z),
            (self.max_x, self.min_y, self.max_z),
            (self.max_x, self.max_y, self.max_z),
        ]

        self.faces = [
            (self.corners[0], self.corners[1], self.corners[2], self.corners[3]),
            (self.corners[4], self.corners[5], self.corners[6], self.corners[7]),
            (self.corners[0], self.corners[1], self.corners[4], self.corners[5]),
            (self.corners[2], self.corners[3], self.corners[6], self.corners[7]),
            (self.corners[0], self.corners[2], self.corners[4], self.corners[6]),
            (self.corners[1], self.corners[3], self.corners[5], self.corners[7]),
        ]

    def recalculate_position(self, position):
        self.min_x, self.min_y, self.min_z = position.x - self.size_x, position.y - self.size_y, position.z - self.size_z
        self.max_x, self.max_y, self.max_z = position.x + self.size_x, position.y + self.size_y, position.z + self.size_z
        self.corners = [
            Vector(self.min_x, self.min_y, self.min_z),
            Vector(self.min_x, self.max_y, self.min_z),
            Vector(self.max_x, self.min_y, self.min_z),
            Vector(self.max_x, self.max_y, self.min_z),
            Vector(self.min_x, self.min_y, self.max_z),
            Vector(self.min_x, self.max_y, self.max_z),
            Vector(self.max_x, self.min_y, self.max_z),
            Vector(self.max_x, self.max_y, self.max_z),
        ]

    def draw_box(self):
        pass
        # pyglet.graphics.draw(4, pyglet.gl.GL_LINE_LOOP, ('v3f', (self.faces[0][0], self.faces[0][1]))
        # pyglet.graphics.draw(4, pyglet.gl.GL_LINE_LOOP, ('v3f', (self.faces[1][0], self.faces[1][1]))
        # pyglet.graphics.draw(4, pyglet.gl.GL_LINE_LOOP, ('v3f', (self.faces[2][0], self.faces[2][1]), self.faces[2][2]))
        # pyglet.graphics.draw(4, pyglet.gl.GL_LINE_LOOP, ('v3f', (self.faces[3][0], self.faces[3][1]), self.faces[3][2]))
        # pyglet.graphics.draw(4, pyglet.gl.GL_LINE_LOOP, ('v3f', (self.faces[4][0], self.faces[4][1]), self.faces[4][2]))
        # pyglet.graphics.draw(4, pyglet.gl.GL_LINE_LOOP, ('v3f', (self.faces[5][0], self.faces[5][1]), self.faces[5][2]))
