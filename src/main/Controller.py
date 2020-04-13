import math
from abc import ABC

import glfw
import pygame
from pyglet import *
from OpenGL.GLU import *

from display.AppWindow import AppWindow
from display.Renderer import Renderer
from display.Scene import Scene
from levels.Initial import Initial


class Controller:
    def __init__(self):
        # pygame.init()
        self.win_size = (1280, 920)
        level1 = Initial()
        self.scene = Scene(self.win_size, level1)
        self.renderer = Renderer(self.scene)
        self.win = AppWindow(self.renderer, self.scene)
        # self.win = pygame.display.set_mode(self.win_size)

        self.win.set_size(self.win_size[0], self.win_size[1])
        self.win.set_caption("PGRF")
        # self.win.set_exclusive_mouse()
        app.run()