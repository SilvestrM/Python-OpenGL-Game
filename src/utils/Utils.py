import math

import pyglet
from OpenGL.GL import *

import pygame

from model.Vector import Vector


def load_texture(file, cube=False):
    if file:
        texture = pyglet.image.load('../resources/' + file).get_texture()
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        return pyglet.graphics.TextureGroup(texture)
    if cube:
        texture = pyglet.image.load('../resources/' + file).get_texture()
        tex_id = None
        glGenTextures(1, tex_id)
        glBindTexture(GL_TEXTURE_CUBE_MAP, tex_id)

        glTexParameterf(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        return pyglet.graphics.TextureGroup(texture)
    return pyglet.image.Texture.create(250, 250)


def load_cubemap_texture(file):
    tex_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_CUBE_MAP, tex_id)

    texture = None
    image = pyglet.image.load('../resources/' + file)

    tex_top = image.get_region(256, 256, 256, 256).get_texture()
    # glTexImage2D(GL_TEXTURE_CUBE_MAP_POSITIVE_Z,0, GL_RGB, tex_top.width, tex_top.height, 0, GL_RGB, GL_UNSIGNED_BYTE, tex_top)
    tex_top = pyglet.image.Texture(tex_top.width, tex_top.height, GL_TEXTURE_CUBE_MAP, tex_id)
    # tex_bot = image.get_region(256, 256, 256, 256).get_image_data()
    # glTexImage2D(GL_TEXTURE_CUBE_MAP_POSITIVE_Z, 0, GL_RGB, tex_top.width, tex_top.height, 0, GL_RGB, GL_UNSIGNED_BYTE,
    #              tex_top)
    # tex_top = image.get_region(256, 256, 256, 256).get_image_data()
    # glTexImage2D(GL_TEXTURE_CUBE_MAP_POSITIVE_Z, 0, GL_RGB, tex_top.width, tex_top.height, 0, GL_RGB, GL_UNSIGNED_BYTE,
    #              tex_top)
    #
    # tex_top = image.get_region(256, 256, 256, 256).get_image_data()
    # glTexImage2D(GL_TEXTURE_CUBE_MAP_POSITIVE_Z, 0, GL_RGB, tex_top.width, tex_top.height, 0, GL_RGB, GL_UNSIGNED_BYTE,
    #              tex_top)
    #
    # tex_top = image.get_region(256, 256, 256, 256).get_image_data()
    # glTexImage2D(GL_TEXTURE_CUBE_MAP_POSITIVE_Z, 0, GL_RGB, tex_top.width, tex_top.height, 0, GL_RGB, GL_UNSIGNED_BYTE,
    #              tex_top)

    glTexParameterf(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    return pyglet.graphics.TextureGroup(tex_top)


# def load_texture(path):
#     textureSurface = pygame.image.load(path)
#
#     if not textureSurface:
#         return
#
#     textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
#     width = textureSurface.get_width()
#     height = textureSurface.get_height()
#
#     texture = glGenTextures(1)
#
#     glBindTexture(GL_TEXTURE_2D, texture)
#     glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
#                  0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)
#
#     glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
#     glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
#     glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
#     glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
#     glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
#     return texture


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
