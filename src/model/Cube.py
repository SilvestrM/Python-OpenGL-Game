from OpenGL.GL import *

from model.Vector import Vector


class Cube:
    size = 1
    cubeVertices = ((1, 1, 1),
                    (1, 1, -1),
                    (1, -1, -1),
                    (1, -1, 1),
                    (-1, 1, 1),
                    (-1, -1, -1),
                    (-1, -1, 1),
                    (-1, 1, -1))
    cubeEdges = ((0, 1), (0, 3), (0, 4), (1, 2), (1, 7), (2, 5), (2, 3), (3, 6), (4, 6), (4, 7), (5, 6), (5, 7))
    textureCoords = (())
    normals = ((-1, 0, 0), (0, 1, 0), (1, 0, 0), (0, -1, 0), (0, 0, 1), (0, 0, 1))
    cubeQuads = ((0, 3, 6, 4),
                 (2, 5, 6, 3),
                 (1, 2, 5, 7),
                 (1, 0, 4, 7),
                 (7, 4, 6, 5),
                 (2, 3, 0, 1))
    # cubeTriangles = (
    #     (0, 2, 1), (1, 2, 3), (4, 5, 6), (5, 7, 6), (6, 7, 8), (7, 9, 8), (1, 3, 4), (3, 5, 4), (1, 11, 10), (1, 4, 11),
    #     (3, 12, 5), (5, 12, 13))
    model = [0, 0, 0, 0,
             0, 0, 0, 0,
             0, 0, 0, 0,
             0, 0, 0, 0]
    translate = [0, 0, 0]

    def __init__(self, color):
        self.color = color

    def set_position(self, translate: Vector):
        self.translate = translate
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(translate.x, translate.y, translate.z)
        self.model = glGetFloatv(GL_MODELVIEW_MATRIX, self.model)
