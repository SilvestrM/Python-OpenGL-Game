from display.Player import Player
from game_objects.Axes import Axes
from game_objects.Cube import Cube
from game_objects.Panel import Panel
from levels.Level import Level
from model.Vector import Vector


class Scene:
    solids = []

    def __init__(self, size: tuple, level: Level):
        self.angle = 0
        self.camera_speed = 3
        self.FPS = 1000 / 60
        self.cam_x = 0
        self.cam_y = 0

        self.solids = level.solids

        self.size = size
        texture1 = 'brokenBricks.jpg'
        texture2 = 'dirt1.jpg'
        texture3 = 'woodenWall1.jpg'

        # self.camera = Camera(Vector(25, 0.0, 0.0), 90, -20, 1)
        self.camera = Player(0.5, Vector(4, 0, 0.0), 60, 0, 1)

        # gluPerspective(90, (self.win_size[0] / self.win_size[1]), 0.1, 50.0)

        self.axes = Axes()

    def update(self, dt):
        if self.camera.position.z > 0 and not self.camera.is_jumping:
            self.camera.position.z -= dt * self.camera.mass
        # elif self.camera.position.z < 0.5 and not self.camera.is_jumping:
        #     self.camera.position.z += dt * self.camera_speed
        self.camera.update(dt)
        # self.solids[0].rotate(Vector(0, 0, 0.1))
