import math

import glfw
import pyglet
from OpenGL.GLU import *

from display.Renderer import Renderer
from display.Scene import Scene


class Window:
    def __init__(self):
        self.delta_speed = 0
        self.solids = []
        self.win_size = (1280, 920)
        self.angle = 0
        self.speed = 1
        self.mb1_pressed = False
        # self.camera = Camera(Vector(25, 0.0, 0.0), 90, -20, 1)
        self.cam_x = 0
        self.cam_y = 0

        if not glfw.init():
            return
            # Create a windowed mode window and its OpenGL context
        glfw.default_window_hints()
        self.window = glfw.create_window(self.win_size[0], self.win_size[1], "Hello World", None, None)
        if not self.window:
            glfw.terminate()
            return

        # Make the window's context current
        glfw.make_context_current(self.window)
        self.scene = Scene(self.win_size)
        self.renderer = Renderer(self.scene)

        self.listeners()
        self.loop()

    def listeners(self):
        glfw.set_mouse_button_callback(self.window, self.mouseclick_listener)
        glfw.set_cursor_pos_callback(self.window, self.mousemove_listener)
        glfw.set_key_callback(self.window, self.key_listener)

    def loop(self):
        gluLookAt(25, 0, 0, 0, 0, -15, 0, 0, 1)

        while not glfw.window_should_close(self.window):
            self.renderer.display()

            glfw.swap_buffers(self.window)

            # Poll for and process events
            glfw.poll_events()
        glfw.terminate()

    def mouseclick_listener(self, win, button, action, mods):
        cam_pos = glfw.get_cursor_pos(win)
        self.mb1_pressed = glfw.get_mouse_button(win, glfw.MOUSE_BUTTON_1) == glfw.PRESS
        if action == glfw.PRESS:
            if button == glfw.MOUSE_BUTTON_1:
                self.cam_x = cam_pos[0]
                self.cam_y = cam_pos[1]

    def mousemove_listener(self, win, x, y):
        if self.mb1_pressed:
            # delta_x = x - self.cam_x
            # delta_y = y - self.cam_y
            # self.cam_x = x
            # self.cam_y = y
            #
            # width = glfw.get_window_size(self.window)[0]
            # height = glfw.get_window_size(self.window)[1]
            # self.scene.camera.zenith -= delta_y / width * 180
            # if self.scene.camera.zenith > 90:
            #     self.scene.camera.zenith = 90
            # if self.scene.camera.zenith <= -90:
            #     self.scene.camera.zenith = -90
            #
            # self.scene.camera.azimuth += delta_x / height * 180
            # self.scene.camera.azimuth = self.scene.camera.azimuth % 360

            self.scene.camera.addAzimuth((math.radians(0.3) * (self.cam_x - x)))
            self.scene.camera.addZenith((math.radians(0.3) * (self.cam_y - y)))
            self.cam_x = x
            self.cam_y = y

    def key_listener(self, win, key, scancode, action, mods):
        if action == glfw.RELEASE:
            pass
            # self.speed = 0

        if action == glfw.PRESS:
            if key == glfw.KEY_ESCAPE:
                glfw.set_window_should_close(win, True)
            if key == glfw.KEY_W:
                self.scene.camera.move_forward(self.speed)
            if key == glfw.KEY_S:
                self.scene.camera.move_backward(self.speed)
            if key == glfw.KEY_A:
                self.scene.camera.move_left(self.speed)
            if key == glfw.KEY_D:
                self.scene.camera.move_right(self.speed)
