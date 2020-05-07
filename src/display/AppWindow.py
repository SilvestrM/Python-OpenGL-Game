import math

import pyglet
from OpenGL.GL import *
from pyglet import window
from pyglet.window import key, mouse

from utils.Utils import play_step


class AppWindow(pyglet.window.Window):
    def __init__(self, renderer, scene, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.renderer = renderer
        self.scene = scene

        self.set_caption("PGRF Mikeska")
        self.set_location(int((self.screen.width - self.width) / 2), int((self.screen.height - self.height) / 2))

        self._font_size = 10
        self._font_color = (44,44,44,0)

        # Controls
        self._exclusive_mouse = True
        self.set_exclusive_mouse(self._exclusive_mouse)

        self._keys = key.KeyStateHandler()
        self.push_handlers(self._keys)

        # Clock
        pyglet.clock.schedule_interval(self.update, 1 / 60.0)
        self._fps_display = window.FPSDisplay(self)

        # Audio
        self._dirt_step = pyglet.media.StaticSource(pyglet.resource.media('jogDirt1.wav'))

        self._step_player = pyglet.media.Player()
        self._time_since_last_move = 0

    def on_draw(self):
        self.clear()
        self.renderer.display()

        # Display info labels
        glDisable(GL_DEPTH_TEST)

        # FPS
        self._fps_display.draw()

        # Position
        pyglet.text.Label(self.scene.player.position.to_string(), x=10, y=self.height - 10,
                          color=self._font_color, anchor_y='top', font_size=self._font_size).draw()
        pyglet.text.Label("Collided objects: " + str(self.scene.collided_number), x=10, y=self.height - 30,
                          color=self._font_color, anchor_y='top', font_size=self._font_size).draw()
        pyglet.text.Label("Exclusive mouse mode - (U) : " + ("on" if self._exclusive_mouse else "off"), x=10,
                          y=self.height - 50,
                          color=self._font_color, anchor_y='top', font_size=self._font_size).draw()
        pyglet.text.Label("Change FOV - (K- L+) : " + str(self.scene.player.FOV), x=10,
                          y=self.height - 70,
                          color=self._font_color, anchor_y='top', font_size=self._font_size).draw()
        pyglet.text.Label("Fog mode - (O) : " + ("Dense" if self.scene.fog_mode == 1 else "Clear"), x=10,
                          y=self.height - 90,
                          color=self._font_color, anchor_y='top', font_size=self._font_size).draw()
        pyglet.text.Label("Crouch - (C) : " + str(self.scene.player.is_crouching), x=10,
                          y=self.height - 110,
                          color=self._font_color, anchor_y='top', font_size=self._font_size).draw()
        pyglet.text.Label("Jump - (SPACE) : " + str(self.scene.player.is_jumping), x=10,
                          y=self.height - 130,
                          color=self._font_color, anchor_y='top', font_size=self._font_size).draw()
        pyglet.text.Label("Movement - (WASD)", x=10,
                          y=self.height - 150,
                          color=self._font_color, anchor_y='top', font_size=self._font_size).draw()
        pyglet.text.Label("Toggle AA - (I) : " + str(self.renderer.antialiasing), x=10,
                          y=self.height - 170,
                          color=self._font_color, anchor_y='top', font_size=self._font_size).draw()
        pyglet.text.Label("Toggle Gravity - (P) : " + str(self.scene.gravity), x=10,
                          y=self.height - 190,
                          color=self._font_color, anchor_y='top', font_size=self._font_size).draw()
        pyglet.text.Label("Toggle Fullscreen - (T) : " + str(self.fullscreen), x=10,
                          y=self.height - 210,
                          color=self._font_color, anchor_y='top', font_size=self._font_size).draw()

    def toggle_exclusive(self):
        # toggles pyglet exclusive mouse mode
        if not self._exclusive_mouse:
            self._exclusive_mouse = True
            self.set_exclusive_mouse(self._exclusive_mouse)
        else:
            self._exclusive_mouse = False
            self.set_exclusive_mouse(self._exclusive_mouse)

    def update(self, dt):
        # Set to False
        moved = False

        if self._keys[key.W]:
            play_step(self._step_player, self._dirt_step)
            self.scene.player.move_forward(dt * self.scene.player.speed)
            moved = True
        if self._keys[key.S]:
            play_step(self._step_player, self._dirt_step)
            self.scene.player.move_backward(dt * self.scene.player.speed)
            moved = True
        if self._keys[key.A]:
            play_step(self._step_player, self._dirt_step)
            self.scene.player.move_left(dt * self.scene.player.speed)
            moved = True
        if self._keys[key.D]:
            play_step(self._step_player, self._dirt_step)
            self.scene.player.move_right(dt * self.scene.player.speed)
            moved = True

        if self._keys[key.L]:
            if self.scene.player.FOV < 120:
                self.scene.player.FOV += 1
        if self._keys[key.K]:
            if self.scene.player.FOV > 30:
                self.scene.player.FOV -= 1

        # soft sound cut
        # so the steps are not cut instantly after the player stops moving
        if not moved:
            self._time_since_last_move += dt
            if self._time_since_last_move > 0.2:
                self._step_player.pause()
        else:
            self._time_since_last_move = 0

        # update the scene
        self.scene.update(dt, moved)

    def on_key_press(self, symbol, modifiers):
        # Key listeners not based on FPS

        if symbol == key.ESCAPE:
            self.close()
        if symbol == key.SPACE:
            self.scene.player.jump()
        if symbol == key.U:
            self.toggle_exclusive()
        if symbol == key.M:
            self.scene.render_distance += 1
        if symbol == key.N:
            self.scene.render_distance -= 1
        if symbol == key.O:
            self.scene.toggle_fog_mode()
        if symbol == key.C:
            self.scene.player.crouch()
        if symbol == key.I:
            self.renderer.toggle_aa()
        if symbol == key.T:
            self.set_fullscreen(not self.fullscreen)
            self.scene.size = (self.width, self.height)
        if symbol == key.P:
            self.scene.toggle_gravity()

    def on_mouse_motion(self, x, y, dx, dy):
        if self._exclusive_mouse:
            self.scene.player.add_azimuth((math.radians(0.1) * (-dx)))
            self.scene.player.add_zenith((math.radians(0.1) * (dy)))

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if buttons == mouse.LEFT:
            if not self._exclusive_mouse:
                self.scene.player.add_azimuth((math.radians(0.1) * (dx)))
                self.scene.player.add_zenith((math.radians(0.1) * (dy)))
