import os

import multiprocessing as mp

from OpenGL.GL import *
from OpenGL.GLU import *

from display.Camera import Camera
from display.Scene import Scene
from model.Solid import Solid
from model.Vector import Vector


class Renderer:
    def __init__(self, scene: Scene):
        self.scene = scene
        glClearColor(0.1, 0.1, 0.1, 1.0)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)

    def display(self):

        glViewport(0, 0, self.scene.size[0], self.scene.size[1])
        glEnable(GL_MULTISAMPLE)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)

        # glEnable(GL_TEXTURE_2D)
        glDisable(GL_LIGHTING)
        # glEnable(GL_BLEND)
        # glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        # glMatrixMode(GL_TEXTURE)
        # glPushMatrix()
        # glLoadIdentity()

        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        gluPerspective(60, (self.scene.size[0] / self.scene.size[1]), 0.1, self.scene.render_distance)
        # gluOrtho2D(self.scene.size[0], self.scene.size[1], 0.1, 500)

        glEnable(GL_FOG)
        glFogi(GL_FOG_MODE, GL_EXP2)
        glFogi(GL_FOG_START, 6)
        glFogi(GL_FOG_END, 12)
        glFogf(GL_FOG_DENSITY, self.scene.fog_density)
        glFogfv(GL_FOG_COLOR, [0.93, 0.89, 0.57, 0.1])

        # cam
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glPushMatrix()
        # camera
        self.scene.player.set_matrix()

        glDisable(GL_TEXTURE_2D)
        glEnable(GL_LINE_SMOOTH)

        glBegin(GL_LINES)
        for i, edge in enumerate(self.scene.axes.edges):
            for vertex in edge:
                glColor3fv(self.scene.axes.colors[i])
                glVertex3fv(self.scene.axes.vertices[vertex])
        glEnd()

        sky_cam = Camera(Vector(0, 0, 0), self.scene.player.azimuth, self.scene.player.zenith, self.scene.player.radius)
        glPopMatrix()
        glShadeModel(GL_SMOOTH)

        # with mp.Pool(2) as executor:
        #     for solid in executor.map(self.render, self.scene.solids):
        #         print(solid)

        for solid in self.scene.solids:
            self.render(solid)

        # Skybox
        glDisable(GL_FOG)
        glDisable(GL_CULL_FACE)
        # glDepthMask(GL_FALSE)
        glDisable(GL_MULTISAMPLE)

        glPushMatrix()
        sky_cam.set_matrix()
        glRotatef(self.scene.skybox.rotate(), 0, 0, 1)
        self.scene.skybox.draw()

        glMatrixMode(GL_MODELVIEW)
        glPopMatrix()

        glDepthMask(GL_TRUE)

        # cam
        # glMatrixMode(GL_MODELVIEW)
        # glPopMatrix()
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        # glMatrixMode(GL_TEXTURE)
        # glPopMatrix()

    def render(self, solid: Solid):
        print("Executing our Task on Process {}".format(os.getpid()))
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        # camera
        self.scene.player.set_matrix()
        glMatrixMode(GL_MODELVIEW)
        # glGetFloatv(GL_MODELVIEW_MATRIX, solid.model)
        glMultMatrixf(solid.model)
        glDisable(GL_LIGHTING)

        solid.draw()
        glMatrixMode(GL_MODELVIEW)
        glPopMatrix()
