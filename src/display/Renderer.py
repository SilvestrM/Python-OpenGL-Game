from OpenGL.GL import *
from OpenGL.GLU import *

from display.Camera import Camera
from display.Scene import Scene
from model.Solid import Solid
from model.Vector import Vector


class Renderer:
    @property
    def antialiasing(self) -> bool:
        return self._antialiasing

    def __init__(self, scene: Scene):

        self.scene = scene
        self._antialiasing = True

        glClearColor(0.1, 0.1, 0.1, 1.0)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)

    def display(self):

        glViewport(0, 0, self.scene.size[0], self.scene.size[1])
        if self._antialiasing:
            glEnable(GL_MULTISAMPLE)

        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)

        glDisable(GL_LIGHTING)

        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        gluPerspective(60, (self.scene.size[0] / self.scene.size[1]), 0.1, self.scene.render_distance)

        # Fog
        glEnable(GL_FOG)
        glFogi(GL_FOG_MODE, GL_EXP2)
        glFogi(GL_FOG_START, 6)
        glFogi(GL_FOG_END, 12)
        glFogf(GL_FOG_DENSITY, self.scene.fog_density)
        glFogfv(GL_FOG_COLOR, self.scene.flavor_color)

        # cam
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glPushMatrix()
        # camera
        self.scene.player.set_matrix()

        glDisable(GL_TEXTURE_2D)
        glEnable(GL_LINE_SMOOTH)

        # Axes
        glBegin(GL_LINES)
        for i, edge in enumerate(self.scene.axes.edges):
            for vertex in edge:
                glColor3fv(self.scene.axes.colors[i])
                glVertex3fv(self.scene.axes.vertices[vertex])
        glEnd()

        sky_cam = Camera(Vector(0, 0, 0), self.scene.player.azimuth, self.scene.player.zenith, self.scene.player.radius)
        glPopMatrix()
        glShadeModel(GL_SMOOTH)

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

        glMatrixMode(GL_PROJECTION)
        glPopMatrix()

    def render(self, solid: Solid):
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

    def toggle_aa(self):
        self._antialiasing = not self._antialiasing
