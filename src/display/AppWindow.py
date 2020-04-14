import math
from abc import ABC

import pyglet
from pyglet import window
# from pyglet.gl import *
from OpenGL.GL import *
from pyglet.window import key, mouse


class AppWindow(pyglet.window.Window):
    def __init__(self, renderer, scene, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.renderer = renderer
        self.scene = scene
        self.keys = key.KeyStateHandler()
        self.set_exclusive_mouse()
        self.set_location(300, 20)

        self.push_handlers(self.keys)
        self.fps_display = window.FPSDisplay(self)
        pyglet.clock.schedule_interval(self.update, 1 / 60.0)
        glClearColor(0.1, 0.1, 0.1, 1.0)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)

    def on_draw(self):
        self.clear()
        self.renderer.display()
        self.fps_display.draw()

    def update(self, dt):
        self.scene.update(dt)
        for solid in self.scene.solids:
            collides = solid.collides(self.scene.camera)
            if collides:
                print(collides)
                collides_dir = solid.collides_with(self.scene.camera)
                print(collides_dir)

        if self.keys[key.W]:
            self.scene.camera.move_forward(dt * self.scene.camera_speed)
        if self.keys[key.S]:
            self.scene.camera.move_backward(dt * self.scene.camera_speed)
        if self.keys[key.A]:
            self.scene.camera.move_left(dt * self.scene.camera_speed)
        if self.keys[key.D]:
            self.scene.camera.move_right(dt * self.scene.camera_speed)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            self.close()
        if symbol == key.SPACE:
            self.scene.camera.jump()
        # if symbol == key.W:
        #     self.scene.camera.move_forward(self.scene.camera_speed)
        # if symbol == key.S:
        #     self.scene.camera.move_backward(self.scene.camera_speed)
        # if symbol == key.A:
        #     self.scene.camera.move_left(self.scene.camera_speed)
        # if symbol == key.D:
        #     self.scene.camera.move_right(self.scene.camera_speed)

    # def on_mouse_press(self, x, y, button, modifiers):
    #     self.mb1_pressed = button
    #
    #     if button == mouse.LEFT:
    #             self.scene.cam_x = x
    #             self.scene.cam_y = y

    def on_mouse_motion(self, x, y, dx, dy):
        self.scene.camera.add_azimuth((math.radians(0.1) * (-dx)))
        self.scene.camera.add_zenith((math.radians(0.1) * (dy)))

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if buttons == mouse.LEFT:
            self.scene.camera.add_azimuth((math.radians(0.3) * (self.scene.cam_x - x)))
            self.scene.camera.add_zenith((math.radians(0.3) * (self.scene.cam_y - y)))
            self.scene.cam_x = x
            self.scene.cam_y = y
