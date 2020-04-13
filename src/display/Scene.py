from display.Camera import Camera
from model.Axes import Axes
from model.Cube import Cube
from model.Vector import Vector
from utils.Utils import load_texture


class Scene:
    solids = []

    def __init__(self, size: tuple):
        self.size = size
        self.texture1 = load_texture('../resources/brokenBricks.jpg')
        self.camera = Camera(Vector(25, 0.0, 0.0), 90, -20, 1)
        # gluPerspective(90, (self.win_size[0] / self.win_size[1]), 0.1, 50.0)

        self.axes = Axes()

        cube1 = Cube([1.0, 0, 0])
        cube1.set_position(Vector(0, -2, -9))
        cube2 = Cube([0, 1.0, 0])
        cube2.set_position(Vector(4, -8, 10))
        #
        self.solids.append(cube1)
        self.solids.append(cube2)
