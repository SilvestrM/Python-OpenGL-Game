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
        print("Initialising scene...")
        self.scene = Scene(self.win_size, level1)
        self.renderer = Renderer(self.scene)

        # Window
        screen = pyglet.canvas.get_display().get_screens()
        configs = screen[0].get_matching_configs(config)
        if not configs:
            print("OGL config not supported...")
            self.win = AppWindow(self.renderer, self.scene, width=self.win_size[0], height=self.win_size[1])
        else:
            self.win = AppWindow(self.renderer, self.scene, width=self.win_size[0], height=self.win_size[1], config=configs[0])

        pyglet.resource.reindex()
        print("Launching app")
        app.run()
