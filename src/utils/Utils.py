import math

from OpenGL.GL import *

import pygame

from model.Vector import Vector


def load_texture(path):
    textureSurface = pygame.image.load(path)

    if not textureSurface:
        return

    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    texture = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texture)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    return texture


def bind_texture(texture):
    glBindTexture(GL_TEXTURE_2D, texture)


def insersects_point(point, box, padding):
    return ((box.min_x - padding) <= point.x <= (box.max_x + padding)) and \
           ((box.min_y - padding) <= point.y <= (box.max_y + padding)) and \
           ((box.min_z - padding) <= point.z <= (box.max_z + padding))


def intersect(a, b):
    return (a.minX <= b.maxX and a.maxX >= b.minX) and \
           (a.minY <= b.maxY and a.maxY >= b.minY) and \
           (a.minZ <= b.maxZ and a.maxZ >= b.minZ)


def distance(vec1: Vector, vec2: Vector):
    return math.sqrt(
        (vec1.x - vec2.x) ** 2 +
        (vec1.y - vec2.y) ** 2 +
        (vec1.z - vec2.z) ** 2)


def get_collision_dir(point, box):
    if box.min_x <= point.x <= box.max_x: return "x"
    if box.min_y <= point.y <= box.max_y: return "y"
    if box.min_z <= point.z <= box.max_z: return "z"
