from OpenGL.GL import *
from OpenGL.GLU import *

from display.Scene import Scene
from model.Cube import Cube
from utils.Utils import bind_texture


class Renderer:
    def __init__(self, scene: Scene):
        self.scene = scene


    def display(self):
        glViewport(0, 0, self.scene.size[0], self.scene.size[1])
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)
        glDisable(GL_LIGHTING)
        glEnable(GL_TEXTURE_2D)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        # glActiveTexture(GL_TEXTURE0)
        # self.displayline()
        # self.speed += self.delta_speed

        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        gluPerspective(60, (self.scene.size[0] / self.scene.size[1]), 0.1, 50.0)

        # cam
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()
        self.scene.camera.set_matrix()

        glDisable(GL_TEXTURE_2D);
        glEnable(GL_LINE_SMOOTH)
        glBegin(GL_LINES)
        e = 0
        for edge in self.scene.axes.edges:
            for vertex in edge:
                glColor(self.scene.axes.colors[e])
                glVertex3fv(self.scene.axes.vertices[vertex])
            e += 1
        glEnd()
        for solid in self.scene.solids:
            self.render(solid)

        # cam
        glMatrixMode(GL_MODELVIEW)
        glPopMatrix()
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()

    def render(self, solid: Cube):
        glMatrixMode(GL_TEXTURE)
        glLoadIdentity()

        glMatrixMode(GL_MODELVIEW)
        # glGetFloatv(GL_MODELVIEW_MATRIX, solid.model)
        glMultMatrixf(solid.model)
        # self.angle += 1
        # glRotatef(self.angle, 0.1, 0.1, 0.1)
        # glPushMatrix()

        glEnable(GL_TEXTURE_2D)
        glDisable(GL_LIGHTING)
        glActiveTexture(GL_TEXTURE0)

        bind_texture(self.scene.texture1)

        glPushMatrix()
        glColor3f(solid.color[0], solid.color[1], solid.color[2])
        glBegin(GL_QUADS)
        # glDrawElements()
        i = 0
        for cubeQuad in solid.cubeQuads:
            glNormal3dv(solid.normals[i])
            glTexCoord2f(0, 0)
            glTexCoord2f(0, 1)
            glTexCoord2f(1, 1)
            glTexCoord2f(1, 0)
            for cubeVertex in cubeQuad:
                glVertex3fv(solid.cubeVertices[cubeVertex])
            i += 1
        glEnd()
        glPopMatrix()
        # glPopMatrix()
