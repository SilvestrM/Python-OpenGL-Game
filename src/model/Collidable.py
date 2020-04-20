import math

import pyglet
import pyglet.gl

from model.Vector import Vector


class Collidable:
    min_x, min_y, min_z = 0, 0, 0
    max_x, max_y, max_z = min_x + 2, min_y + 2, min_z + 2

    box_faces = (
        [max_x, min_y, min_z, min_x, min_y, min_z, min_x, max_y, min_z, max_x, max_y, min_z],
        [min_x, min_y, max_z, max_x, min_y, max_z, max_x, max_y, max_z, min_x, max_y, max_z],
        [min_x, min_y, max_z, min_x, max_y, max_z, min_x, max_y, min_z, min_x, min_y, min_z],
        [max_x, min_y, min_z, max_x, max_y, min_z, max_x, max_y, max_z, max_x, min_y, max_z],
        [min_x, min_y, min_z, max_x, min_y, min_z, max_x, min_y, max_z, min_x, min_y, max_z],
        [min_x, max_y, max_z, max_x, max_y, max_z, max_x, max_y, min_z, min_x, max_y, min_z]
    )

    position: Vector

    def __init__(self):
        pass
        # for i, face in enumerate(self.box_faces):
        #     for j, Vertex in enumerate(face):
        #         self.box_faces[i][j] = Vertex * 2

    def insersects_point(self, point, box):
        return (box.minX <= point.x <= box.maxX) and (box.minY <= point.y <= box.maxY) and (
                box.minZ <= point.z <= box.maxZ)

    def collision(self, other):
        col_x = self.position.x + self.bounding_box.x >= other.position.x and other.position.x >= self.position.x
        col_y = self.position.y + self.bounding_box.y >= other.position.y and other.position.y >= self.position.y
        return col_x and col_y

    def collides_with(self, other_object):
        collision = self.bounding_box / 2 + other_object.bounding_box / 2
        distance = self.distance(self.position, other_object.position)
        collides = distance <= collision
        if collides:
            direction = self.collides_direction(self.position, other_object.position, self.bounding_box / 2)

            # point > 1 , point <2, point < 3

            # if other_object.position.x = self.position.x -

            if direction == "x": print("x"); return self.position.x + self.bounding_box / 2
            if direction == "y": print("y"); return self.position.y + self.bounding_box / 2
            if direction == "z": print("z"); return self.position.z + self.bounding_box / 2

            # return collides

    def collides(self, other_object):
        collision = self.bounding_box / 2 + other_object.bounding_box / 2
        distance = self.distance(self.position, other_object.position)
        collides = distance <= collision
        return collides

    def collides_direction(self, vec1: Vector, vec2: Vector, box):
        x = vec1.x - vec2.x
        if x <= box: return 'x'
        y = vec1.y - vec2.y
        if y <= box: return 'y'
        z = vec1.z - vec2.z
        if z <= box: return 'z'

    def distance(self, vec1: Vector, vec2: Vector):
        return math.sqrt(
            (vec1.x - vec2.x) ** 2 +
            (vec1.y - vec2.y) ** 2 +
            (vec1.z - vec2.z) ** 2)

    def draw_box(self):

        pyglet.graphics.draw(4, pyglet.gl.GL_LINE_LOOP, ('v3f', self.box_faces[0]))
        pyglet.graphics.draw(4, pyglet.gl.GL_LINE_LOOP, ('v3f', self.box_faces[1]))
        pyglet.graphics.draw(4, pyglet.gl.GL_LINE_LOOP, ('v3f', self.box_faces[2]))
        pyglet.graphics.draw(4, pyglet.gl.GL_LINE_LOOP, ('v3f', self.box_faces[3]))
        pyglet.graphics.draw(4, pyglet.gl.GL_LINE_LOOP, ('v3f', self.box_faces[4]))
        pyglet.graphics.draw(4, pyglet.gl.GL_LINE_LOOP, ('v3f', self.box_faces[5]))
