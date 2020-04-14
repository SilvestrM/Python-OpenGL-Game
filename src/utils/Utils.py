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


def distance(vec1: Vector, vec2: Vector):
    return math.sqrt(
        (vec1.x - vec2.x) ** 2 +
        (vec1.y - vec2.y) ** 2 +
        (vec1.z - vec2.z) ** 2)
