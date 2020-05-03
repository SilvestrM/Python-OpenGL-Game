import pyglet
from pyglet import *

from display.AppWindow import AppWindow
from display.Renderer import Renderer
from display.Scene import Scene
from levels.Initial import Initial


class Controller:
    def __init__(self):
        pyglet.resource.path = ['./resources', './resources/SFX', './resources/skybox']
        pyglet.resource.reindex()

        self.win_size = (1280, 920)

        # options['debug_graphics_batch'] = True

        # OGL config
        config = gl.Config()
        config.stencil_size = 8
        # Antialiasing
        config.sample_buffers = 1
        config.samples = 16
        config.aux_buffers = 4

        # Level init
        level1 = Initial()

        # Scene with level
        self.scene = Scene(self.win_size, level1)
        self.renderer = Renderer(self.scene)

        screen = pyglet.canvas.get_display().get_screens()
        # Window
        self.win = AppWindow(self.renderer, self.scene, width=self.win_size[0], height=self.win_size[1], config=config)

        pyglet.resource.reindex()
        print("Launching app")
        app.run()
