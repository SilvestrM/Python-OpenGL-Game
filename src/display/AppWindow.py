import math
from abc import ABC

import pyglet
from pyglet import window
# from pyglet.gl import *
from OpenGL.GL import *
from pyglet.window import key, mouse

from game_objects.Cube import Cube
from utils import Utils


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
        collides = False
        direction = ""
        collided_object = []

        normalised_pos = self.scene.camera.position.normalise()
        # d = self.scene.camera.position.x - normalised_pos.x
        # print(d)
        for solid in self.scene.solids:
            if isinstance(solid, Cube):
                collides = Utils.insersects_point(self.scene.camera.position, solid)
                if collides:
                    print(collides)
                    direction = Utils.get_collision_dir(self.scene.camera.position, solid)
                    collided_object = solid
                    break


        # if collides:
        #     print(collides)
        #     collides_dir = solid.collides_with(self.scene.camera)
        #     print(collides_dir)

        if self.keys[key.W]:
            print(collided_object)
            # if collides:
            #     if direction == "x" and (
            #             self.scene.camera.position.x < collided_object.min_x or self.scene.camera.position.x > collided_object.max_x):
            #         dist_min = collided_object.min_x - self.scene.camera.position.x
            #         dist_max = collided_object.max_x - self.scene.camera.position.x
            #         print(dist_min)
            #         print(dist_max)
            #         self.scene.camera.move_forward(dt * self.scene.camera_speed)
            #     elif direction == "y" and (
            #             self.scene.camera.position.y < collided_object.min_y or self.scene.camera.position.y > collided_object.max_y):
            #         self.scene.camera.move_forward(dt * self.scene.camera_speed)
            #     elif direction == "z" and (
            #             self.scene.camera.position.z < collided_object.min_z or self.scene.camera.position.z > collided_object.max_z):
            #         self.scene.camera.move_forward(dt * self.scene.camera_speed)
            #     else:
            #         self.scene.camera.move_backward((dt + 0.2) * self.scene.camera_speed)
            #         dist_min = collided_object.min_x - self.scene.camera.position.x
            #         dist_max = collided_object.max_x - self.scene.camera.position.x
            #         print(dist_min)
            #         print(dist_max)
            #         print("blocked")
            # else:
            self.scene.camera.move_forward(dt * self.scene.camera_speed)

        if self.keys[key.S]:
            self.scene.camera.move_backward(dt * self.scene.camera_speed)
        if self.keys[key.A]:
            self.scene.camera.move_left(dt * self.scene.camera_speed)
        if self.keys[key.D]:
            self.scene.camera.move_right(dt * self.scene.camera_speed)

        if collides:
            dist_min_x = collided_object.min_x - self.scene.camera.position.x
            dist_max_x = self.scene.camera.position.x - collided_object.max_x
            dist_min_y = collided_object.min_y - self.scene.camera.position.y
            dist_max_y = self.scene.camera.position.y - collided_object.max_y
            dist_min_z = collided_object.min_z - self.scene.camera.position.z
            dist_max_z = collided_object.max_z - self.scene.camera.position.z

            print("nX", dist_min_x)
            print("xX", dist_max_x)
            print("nY", dist_min_y)
            print("xY", dist_max_y)
            print("nZ", dist_min_z)
            print("xZ", dist_max_z)


            # if direction == "x":
            #     if dist_min_x < dist_max_x:
            #         self.scene.camera.position.x = collided_object.min_x
            #     if dist_max_x < dist_min_x:
            #         self.scene.camera.position.x = collided_object.max_x
            #     # self.scene.camera.move_backward(dt * self.scene.camera_speed)
            #     # d = (p[i] - np[i]) * face[i]
            #
            # elif direction == "y":
            #     if dist_min_y < dist_max_y:
            #         self.scene.camera.position.x = collided_object.min_y
            #     if dist_max_y < dist_min_y:
            #         self.scene.camera.position.x = collided_object.max_y
            # elif direction == "z" and (
            #         self.scene.camera.position.z < collided_object.min_z or self.scene.camera.position.z > collided_object.max_z):
            #     self.scene.camera.move_forward(dt * self.scene.camera_speed)



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
