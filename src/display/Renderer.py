from OpenGL.GL import *
from OpenGL.GLU import *

from display.Camera import Camera
from display.Scene import Scene
from model.Solid import Solid
from model.Vector import Vector


class Renderer:
    def __init__(self, scene: Scene):
        self.angle = 0
        self.scene = scene

    def display(self):
        # glViewport(0, 0, self.scene.size[0], self.scene.size[1])
        # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)

        glEnable(GL_TEXTURE_2D)
        glDisable(GL_LIGHTING)
        # glEnable(GL_BLEND)
        # glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        # glMatrixMode(GL_TEXTURE)
        # glPushMatrix()
        # glLoadIdentity()

        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        gluPerspective(60, (self.scene.size[0] / self.scene.size[1]), 0.1, 500)

        glEnable(GL_FOG)
        glFogi(GL_FOG_MODE, GL_EXP2)
        glFogi(GL_FOG_START, 0)
        glFogi(GL_FOG_END, 100)
        glFogf(GL_FOG_DENSITY, 0.05)
        glFogfv(GL_FOG_COLOR, [0.93, 0.89, 0.57, 1])

        # cam

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glPushMatrix()
        # camera
        self.scene.player.set_matrix()

        glDisable(GL_TEXTURE_2D)
        glEnable(GL_LINE_SMOOTH)

        glBegin(GL_LINES)
        e = 0
        for i, edge in enumerate(self.scene.axes.edges):
            for vertex in edge:
                glColor3fv(self.scene.axes.colors[i])
                glVertex3fv(self.scene.axes.vertices[vertex])
            e += 1
        glEnd()

        sky_cam = Camera(Vector(0,0,0), self.scene.player.azimuth, self.scene.player.zenith, self.scene.player.radius)
        glPopMatrix()

        for solid in self.scene.solids:
            glPushMatrix()
            # camera
            self.scene.player.set_matrix()
            self.render(solid)
            glMatrixMode(GL_MODELVIEW)
            glPopMatrix()

        glDisable(GL_FOG)
        glDisable(GL_CULL_FACE)
        glDepthMask(GL_FALSE)
        glPushMatrix()
        sky_cam.set_matrix()
        self.scene.skybox.draw()
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
        # glMatrixMode(GL_TEXTURE)
        glEnable(GL_TEXTURE_2D)
        solid.texture.set_state()
        # pyglet.gl.glBindTexture(GL_TEXTURE_2D, solid.texture.texture)
        glMatrixMode(GL_MODELVIEW)
        # glGetFloatv(GL_MODELVIEW_MATRIX, solid.model)
        glMultMatrixf(solid.model)

        # glPushMatrix()
        # self.angle += 1
        # glRotatef(self.angle, 0.1, 0.1, 0.1)
        # glPopMatrix()

        glEnable(GL_TEXTURE_2D)
        glDisable(GL_LIGHTING)
        glActiveTexture(GL_TEXTURE0)

        glShadeModel(GL_SMOOTH)

        # bind_texture(self.scene.texture1)

        # glPushMatrix()

        solid.draw()

        # glPopMatrix()
