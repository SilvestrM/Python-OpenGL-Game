import math

import pyglet
from OpenGL.GL import *

from model.Vector import Vector


def load_texture(file, cube=False):
    if file:
        image = pyglet.image.load('../resources/' + file)
        # texture = image.get_region(0,0,256,256).get_mipmapped_texture()
        if is_power_two(image.width) and is_power_two(image.height):
            texture = image.get_mipmapped_texture()
        else:
            texture = image.get_texture()
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        return pyglet.graphics.TextureGroup(texture)
    return pyglet.graphics.TextureGroup(pyglet.image.Texture.create(256, 256))


def is_power_two(num):
    return (math.ceil(Log2(num)) ==
            math.floor(Log2(num)))


def Log2(x):
    if x == 0:
        return False
    return math.log10(x) / math.log10(2)


def load_cubemap_texture(file):
    tex_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_CUBE_MAP, tex_id)

    texture = None
    # glEnable(GL_TEXTURE_CUBE_MAP)
    image = pyglet.image.load('../resources/' + file)
    # temporary solution

    tex_front = image.get_region(256, 256, 256, 256).get_texture(True)
    tex_bottom = image.get_region(256, 0, 256, 256).get_texture(True)
    tex_left = image.get_region(0, 256, 256, 256).get_texture(True)
    tex_top = image.get_region(256, 512, 256, 256).get_texture(True)
    pyglet.image.Texture(256,256,GL_TEXTURE_CUBE_MAP_POSITIVE_Z,tex_id)
    # glBindTexture(GL_TEXTURE_CUBE_MAP, tex_top.id)
    # glTexImage2D(GL_TEXTURE_CUBE_MAP_POSITIVE_Z, 0, GL_RGB, tex_top.width, tex_top.height, 0, GL_RGB, GL_UNSIGNED_BYTE,
    #              tex_top.get_data())
    tex_right = image.get_region(512, 256, 256, 256).get_texture()
    tex_back = image.get_region(768, 256, 256, 256).get_texture()

    # img_grid = pyglet.image.ImageGrid(image, 3, 4, 10, 10)
    # textures = pyglet.image.TextureGrid(img_grid)
    # textures = img_grid.get_texture_sequence()
    textures = [tex_bottom, tex_top, tex_left, tex_right, tex_back, tex_front]


    # glTexParameterf(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    # glTexParameterf(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    # glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    # glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    print(textures[0])
    return textures


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


def collides_point(point, box, padding):
    return ((box.min_x - padding) <= point.x <= (box.max_x + padding)) and \
           ((box.min_y - padding) <= point.y <= (box.max_y + padding)) and \
           ((box.min_z - padding) <= point.z <= (box.max_z + padding))


def collides_box(a, b):
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
