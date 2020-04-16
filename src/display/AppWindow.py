import math
from abc import ABC

import pyglet
from pyglet import window
# from pyglet.gl import *
from OpenGL.GL import *
from pyglet.window import key, mouse

from game_objects.Cube import Cube
from model.Vector import Vector
from utils import Utils


class AppWindow(pyglet.window.Window):
    def __init__(self, renderer, scene, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.renderer = renderer
        self.scene = scene
        self.keys = key.KeyStateHandler()
        self.set_exclusive_mouse()
        self.set_location(500, 20)

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

        collides = False
        direction = ""
        collided_object = []
        padding = self.scene.camera.padding
        moved = False

        normalised_pos = self.scene.camera.position.normalise()
        # d = self.scene.camera.position.x - normalised_pos.x
        # print(d)

        # if collides:
        #     print(collides)
        #     collides_dir = solid.collides_with(self.scene.camera)
        #     print(collides_dir)

        if self.keys[key.W]:
            self.scene.camera.move_forward(dt * self.scene.camera_speed)
            moved = True
        if self.keys[key.S]:
            self.scene.camera.move_backward(dt * self.scene.camera_speed)
            moved = True
        if self.keys[key.A]:
            self.scene.camera.move_left(dt * self.scene.camera_speed)
            moved = True
        if self.keys[key.D]:
            self.scene.camera.move_right(dt * self.scene.camera_speed)
            moved = True

        self.scene.update(dt)
        if moved:
            for solid in self.scene.solids:
                if isinstance(solid, Cube):
                    collides = Utils.insersects_point(self.scene.camera.position, solid, padding)
                    if collides:
                        print(collides)
                        direction = Utils.get_collision_dir(self.scene.camera.position, solid)
                        print(direction)
                        collided_object = solid
                        break
        if collides:
            center_dist = self.scene.camera.position.add(Vector(padding, padding, padding)).sub(
                collided_object.position)

            dist_min_x = math.fabs(self.scene.camera.position.x + padding - collided_object.min_x)
            dist_max_x = math.fabs(self.scene.camera.position.x + padding - collided_object.max_x)
            dist_min_y = math.fabs(self.scene.camera.position.y + padding - collided_object.min_y)
            dist_max_y = math.fabs(self.scene.camera.position.y + padding - collided_object.max_y)
            dist_min_z = math.fabs(self.scene.camera.position.z - collided_object.min_z)
            dist_max_z = math.fabs(self.scene.camera.position.z - collided_object.max_z)

            distances = [dist_min_x - math.fabs(center_dist.x), dist_max_x - math.fabs(center_dist.x),
                         dist_min_y - math.fabs(center_dist.y), dist_max_y - math.fabs(center_dist.y),
                         dist_min_z - math.fabs(center_dist.z), dist_max_z - math.fabs(center_dist.z)]

            print("nX", dist_min_x, "-", distances[0])
            print("xX", dist_max_x, "-", distances[1])
            print("nY", dist_min_y, "-", distances[2])
            print("xY", dist_max_y, "-", distances[3])
            print("nZ", dist_min_z, "-", distances[4])
            print("xZ", dist_max_z, "-", distances[5])
            print("center", center_dist.to_string())
            # # min x min y
            # if distances[0] == distances[2]:
            #     self.scene.camera.position.x = collided_object.min_x - padding
            #     self.scene.camera.position.y = collided_object.min_y - padding
            #
            # # min x max y
            # elif distances[0] == distances[3]:
            #     self.scene.camera.position.x = collided_object.min_x - padding
            #     self.scene.camera.position.y = collided_object.max_y + padding
            #
            # # max x min y
            # elif distances[1] == distances[2]:
            #     self.scene.camera.position.x = collided_object.max_x + padding
            #     self.scene.camera.position.y = collided_object.min_y - padding
            #
            # # max x max y
            # elif distances[1] == distances[3]:
            #     self.scene.camera.position.x = collided_object.max_x + padding
            #     self.scene.camera.position.y = collided_object.max_y + padding

            minimum = min(range(len(distances)), key=distances.__getitem__)
            # while True:
            #     minimum = min(range(len(distances)), key=distances.__getitem__)
            #     if distances[minimum] > -1:
            #         break
            print("min", minimum)
            # if din

            # min x
            if minimum == 0:
                if distances[0] == distances[2] and not distances[0] == distances[3]:
                    self.scene.camera.position.y = collided_object.min_y - padding
                    self.scene.camera.position.x = collided_object.min_x - padding
                elif distances[0] == distances[3] and not distances[0] == distances[2]:
                    self.scene.camera.position.x = collided_object.min_x - padding
                    self.scene.camera.position.y = collided_object.max_y + padding
                else:
                    self.scene.camera.position.x = collided_object.min_x - padding
            # max x
            if minimum == 1:
                if distances[1] == distances[2] and not distances[1] == distances[3]:
                    self.scene.camera.position.x = collided_object.max_x + padding
                    self.scene.camera.position.y = collided_object.min_y - padding
                elif distances[1] == distances[3] and not distances[1] == distances[2]:
                    self.scene.camera.position.x = collided_object.max_x + padding
                    self.scene.camera.position.y = collided_object.max_y + padding
                else:
                    self.scene.camera.position.x = collided_object.max_x + padding

            # min y
            if minimum == 2:
                if distances[0] == distances[2] and not distances[1] == distances[2]:
                    self.scene.camera.position.x = collided_object.min_x - padding
                    self.scene.camera.position.y = collided_object.min_y - padding
                elif distances[1] == distances[2] and not distances[0] == distances[2]:
                    self.scene.camera.position.x = collided_object.max_x + padding
                    self.scene.camera.position.y = collided_object.min_y - padding
                else:
                    self.scene.camera.position.y = collided_object.min_y - padding

            # max y
            if minimum == 3:
                if distances[0] == distances[3] and not distances[1] == distances[3]:
                    self.scene.camera.position.y = collided_object.max_y + padding
                    self.scene.camera.position.x = collided_object.min_x - padding
                elif distances[1] == distances[3] and not distances[0] == distances[3]:
                    self.scene.camera.position.y = collided_object.max_y + padding
                    self.scene.camera.position.x = collided_object.max_x + padding
                else:
                    self.scene.camera.position.y = collided_object.max_y + padding
            if minimum == 4:
                self.scene.camera.position.z = collided_object.min_z - padding
            if minimum == 5:
                self.scene.camera.position.z = collided_object.max_z + padding

        if self.scene.camera.position.z < 0:
            self.scene.camera.position.z = 0

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

    def on_mouse_motion(self, x, y, dx, dy):
        self.scene.camera.add_azimuth((math.radians(0.1) * (-dx)))
        self.scene.camera.add_zenith((math.radians(0.1) * (dy)))

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if buttons == mouse.LEFT:
            self.scene.camera.add_azimuth((math.radians(0.3) * (self.scene.cam_x - x)))
            self.scene.camera.add_zenith((math.radians(0.3) * (self.scene.cam_y - y)))
            self.scene.cam_x = x
            self.scene.cam_y = y
