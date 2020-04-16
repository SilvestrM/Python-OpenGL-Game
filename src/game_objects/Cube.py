from OpenGL.GL import *
import pyglet.gl

from model.BoundingBox import BoundingBox
from model.Collidable import Collidable
from model.Solid import Solid
from model.Vector import Vector
import pyglet.graphics


class Cube(Solid):

    def __init__(self, color: list, texture=""):
        super().__init__(color, texture)
        texture_coords = ('t2f', (0, 0, 0.5, 0, 0.5, 0.5, 0, 0.5))

        colors = ('c3f', [color[0], color[1], color[2]] * 4)
        size = 1
        self.size = size
        self.center_dist = 0
        self.bounding_box = BoundingBox(self.position, size, size, size)

        self.vertices = [
            [size, 0, 0], [0, 0, 0], [0, size, 0], [size, size, 0], [0, 0, size], [size, 0, size], [size, size, size],
            [0, size, size]]
        self.bounding_box = self.vertices

        self.batch.add(4, GL_QUADS, self.texture,
                       ('v3f', (size, -size, -size, -size, -size, -size, -size, size, -size, size, size, -size)),
                       colors,
                       texture_coords)  # bottom
        self.batch.add(4, GL_QUADS, self.texture,
                       ('v3f', (-size, -size, size, size, -size, size, size, size, size, -size, size, size)),
                       texture_coords)  # top
        self.batch.add(4, GL_QUADS, self.texture,
                       ('v3f', (-size, -size, size, -size, size, size, -size, size, -size, -size, -size, -size,)),
                       texture_coords)  # left
        self.batch.add(4, GL_QUADS, self.texture,
                       ('v3f', (size, -size, -size, size, size, -size, size, size, size, size, -size, size,)),
                       texture_coords)  # right
        self.batch.add(4, GL_QUADS, self.texture,
                       ('v3f', (-size, -size, -size, size, -size, -size, size, -size, size, -size, -size, size)),
                       texture_coords)  # back
        self.batch.add(4, GL_QUADS, self.texture,
                       ('v3f', (-size, size, size, size, size, size, size, size, -size, -size, size, -size)),
                       texture_coords)  # front

        self.min_x, self.min_y, self.min_z = self.position.x - size, self.position.y - size, self.position.z - size
        self.max_x, self.max_y, self.max_z = self.position.x + size, self.position.y + size, self.position.z + size



        # box_faces = (
        #     [max_x, min_y, min_z, min_x, min_y, min_z, min_x, max_y, min_z, max_x, max_y, min_z],
        #     [min_x, min_y, max_z, max_x, min_y, max_z, max_x, max_y, max_z, min_x, max_y, max_z],
        #     [min_x, min_y, max_z, min_x, max_y, max_z, min_x, max_y, min_z, min_x, min_y, min_z],
        #     [max_x, min_y, min_z, max_x, max_y, min_z, max_x, max_y, max_z, max_x, min_y, max_z],
        #     [min_x, min_y, min_z, max_x, min_y, min_z, max_x, min_y, max_z, min_x, min_y, max_z],
        #     [min_x, max_y, max_z, max_x, max_y, max_z, max_x, max_y, min_z, min_x, max_y, min_z]
        # )

    def set_position(self, translate: Vector, rotate_angle=0, rotate=Vector(0.0, 0.0, 0.0),
                     scale=Vector(1.0, 1.0, 1.0)):
        super().set_position(translate, rotate_angle, rotate, scale)
        self.min_x, self.min_y, self.min_z = translate.x - self.size, translate.y - self.size, translate.z - self.size
        self.max_x, self.max_y, self.max_z = translate.x + self.size, translate.y + self.size, translate.z + self.size

        self.bounding_box = BoundingBox(self.position, scale.x, scale.y, scale.z)

    # def draw(self):
    #
    #     # glEnable(GL_TEXTURE_2D)
    #     # glBindTexture(GL_TEXTURE_2D, self.texture)
    #     self.batch.draw()
    #     # pyglet.graphics.draw(6, GL_QUADS, self.batch)
    #
    #     # glColor3f(self.color[0], self.color[1], self.color[2])
    #     # glBegin(GL_QUADS)
    #     # # glDrawElements()
    #     # i = 0
    #     # for cubeQuad in self.cubeQuads:
    #     #     glNormal3dv(self.normals[i])
    #     #     glTexCoord2f(0, 0)
    #     #     glTexCoord2f(1, 0)
    #     #     glTexCoord2f(1, 1)
    #     #     glTexCoord2f(0, 1)
    #     #     for cubeVertex in cubeQuad:
    #     #         glVertex3fv(self.cubeVertices[cubeVertex])
    #     #     i += 1
    #     # glEnd()
