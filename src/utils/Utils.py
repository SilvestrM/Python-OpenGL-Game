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
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST_MIPMAP_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_LOD_BIAS, 0)
            texture.min_filter = GL_NEAREST_MIPMAP_LINEAR
            texture.mag_filter = GL_LINEAR
            aaf_amount = min(4, glGetFloat(GL_MAX_TEXTURE_MAX_ANISOTROPY))
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAX_ANISOTROPY, aaf_amount)


        else:
            texture = image.get_texture()
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
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

    texture = None
    glEnable(GL_TEXTURE_CUBE_MAP)
    tex_id = glGenTextures(1)
    # image = pyglet.image.load('../resources/' + file)
    # temporary solution

    # tex_width = round(image.width/4)
    # tex_height = round(image.height/3)

    tex_bottom = pyglet.image.load('../resources/skybox/' + file + '-bottom.jpg').get_image_data()
    tex_top = pyglet.image.load('../resources/skybox/' + file + '-top.jpg').get_image_data()
    tex_left = pyglet.image.load('../resources/skybox/' + file + '-left.jpg').get_image_data()
    tex_right = pyglet.image.load('../resources/skybox/' + file + '-right.jpg').get_image_data()
    tex_back = pyglet.image.load('../resources/skybox/' + file + '-back.jpg').get_image_data()
    tex_front = pyglet.image.load('../resources/skybox/' + file + '-front.jpg').get_image_data()

    tex_width = round(tex_bottom.width)
    tex_height = round(tex_bottom.height)

    # tex_bottom = image.get_region(tex_width, 0, tex_width, tex_height).get_image_data()
    # tex_top = image.get_region(tex_width, tex_height*2, tex_width, tex_height).get_image_data()
    # tex_left = image.get_region(0, tex_height, tex_width, tex_height).get_image_data()
    # tex_right = image.get_region(tex_width*2, tex_height, tex_width, tex_height).get_image_data()
    # tex_back = image.get_region(tex_width*3, tex_height, tex_width, tex_height).get_image_data()
    # tex_front = image.get_region(tex_width,tex_height, tex_width, tex_height).get_image_data()

    glBindTexture(GL_TEXTURE_CUBE_MAP, tex_id)
    glTexImage2D(GL_TEXTURE_CUBE_MAP_NEGATIVE_Z, 0, GL_RGB, tex_width, tex_height, 0, GL_RGB, GL_UNSIGNED_BYTE, tex_bottom.get_data())
    glTexImage2D(GL_TEXTURE_CUBE_MAP_POSITIVE_Z, 0, GL_RGB, tex_width, tex_height, 0, GL_RGB, GL_UNSIGNED_BYTE, tex_top.get_data())
    glTexImage2D(GL_TEXTURE_CUBE_MAP_NEGATIVE_X, 0, GL_RGB, tex_width, tex_height, 0, GL_RGB, GL_UNSIGNED_BYTE, tex_left.get_data())
    glTexImage2D(GL_TEXTURE_CUBE_MAP_POSITIVE_X, 0, GL_RGB, tex_width, tex_height, 0, GL_RGB, GL_UNSIGNED_BYTE, tex_right.get_data())
    glTexImage2D(GL_TEXTURE_CUBE_MAP_NEGATIVE_Y, 0, GL_RGB, tex_width, tex_height, 0, GL_RGB, GL_UNSIGNED_BYTE, tex_back.get_data())
    glTexImage2D(GL_TEXTURE_CUBE_MAP_POSITIVE_Y, 0, GL_RGB, tex_width, tex_height, 0, GL_RGB, GL_UNSIGNED_BYTE, tex_front.get_data())
    glGenerateMipmap(GL_TEXTURE_CUBE_MAP)

    # glTexParameterf(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    # glTexParameterf(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    # glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_R, GL_CLAMP_TO_EDGE)
    # glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    # glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    # glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_ADD)
    return tex_id


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
