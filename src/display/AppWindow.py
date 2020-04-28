import math

# from pyglet.gl import *
import pyglet
from OpenGL.GL import *
from pyglet import window
from pyglet.window import key, mouse


class AppWindow(pyglet.window.Window):
    def __init__(self, renderer, scene, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.renderer = renderer
        self.scene = scene

        self.keys = key.KeyStateHandler()
        self._exclusive = True
        self.set_exclusive_mouse(self._exclusive)

        self.push_handlers(self.keys)

        pyglet.clock.schedule_interval(self.update, 1 / 60.0)
        self.fps_display = window.FPSDisplay(self)
        self.label = pyglet.text.Label(self.scene.player.position.to_string(), x=10, y=scene.size[1] - 10,
                                       color=(255, 255, 255, 255), anchor_y='top')
        self.dirt_step = pyglet.media.StaticSource(pyglet.resource.media('jogDirt1.wav'))

        self.step_player = pyglet.media.Player()
        self.time_since_last_move = 0

    def on_draw(self):
        self.clear()
        self.renderer.display()

        glDisable(GL_DEPTH_TEST)

        # display labels

        # fps
        self.fps_display.draw()

        # position
        pyglet.text.Label(self.scene.player.position.to_string(), x=10, y=self.scene.size[1] - 10,
                          color=(255, 255, 255, 255), anchor_y='top', bold=True).draw()

    def toggle_exclusive(self):
        # toggles pyglet exclusive mouse mode

        if not self._exclusive:
            self._exclusive = True
            self.set_exclusive_mouse(True)
        else:
            self._exclusive = False
            self.set_exclusive_mouse(False)

    def update(self, dt):
        # if player moved
        moved = False

        if self.keys[key.W]:
            self.play_step(self.step_player, self.dirt_step)
            self.scene.player.move_forward(dt * self.scene.camera_speed)
            moved = True
        if self.keys[key.S]:
            self.play_step(self.step_player, self.dirt_step)
            self.scene.player.move_backward(dt * self.scene.camera_speed)
            moved = True
        if self.keys[key.A]:
            self.play_step(self.step_player, self.dirt_step)
            self.scene.player.move_left(dt * self.scene.camera_speed)
            moved = True
        if self.keys[key.D]:
            self.play_step(self.step_player, self.dirt_step)
            self.scene.player.move_right(dt * self.scene.camera_speed)
            moved = True

        # soft sound cut
        # so the steps are not cut instantly after the player stops moving
        if not moved:
            self.time_since_last_move += dt
            if self.time_since_last_move > 0.2:
                self.step_player.pause()
        else:
            self.time_since_last_move = 0

        # update the scene
        self.scene.update(dt, moved)

    def play_step(self, player, source):
        # checks so the queue is not filled after every update when moving,
        # queues sound only if tehre isnt one already playing

        player.play()
        if not player.source:
            player.queue(source)

    def on_key_press(self, symbol, modifiers):
        # Key listeners not based on FPS

        if symbol == key.ESCAPE:
            self.close()
        if symbol == key.SPACE:
            self.scene.player.jump()
        if symbol == key.O:
            self.toggle_exclusive()
        if symbol == key.M:
            self.scene.render_distance += 1
        if symbol == key.N:
            self.scene.render_distance -= 1
        if symbol == key.U:
            self.scene.toggle_fog_mode()
        # if symbol == key.W:
        #     self.scene.camera.move_forward(self.scene.camera_speed)
        # if symbol == key.S:
        #     self.scene.camera.move_backward(self.scene.camera_speed)
        # if symbol == key.A:
        #     self.scene.camera.move_left(self.scene.camera_speed)
        # if symbol == key.D:
        #     self.scene.camera.move_right(self.scene.camera_speed)

    def on_mouse_motion(self, x, y, dx, dy):
        self.scene.player.add_azimuth((math.radians(0.1) * (-dx)))
        self.scene.player.add_zenith((math.radians(0.1) * (dy)))

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if buttons == mouse.LEFT:
            self.scene.player.add_azimuth((math.radians(0.3) * (self.scene.cam_x - x)))
            self.scene.player.add_zenith((math.radians(0.3) * (self.scene.cam_y - y)))
            self.scene.cam_x = x
            self.scene.cam_y = y
