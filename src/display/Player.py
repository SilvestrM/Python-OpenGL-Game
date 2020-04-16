from display.Camera import Camera
from model.Collidable import Collidable
from model.Vector import Vector


class Player(Camera):
    def __init__(self, mass, position: Vector, azimuth, zenith, radius: float):
        super().__init__(position, azimuth, zenith, radius)

        self.min_x, self.min_y, self.min_z = self.position.x - 0.5, self.position.y - 0.5, self.position.z - 0.5
        self.max_x, self.max_y, self.max_z = self.min_x + 1, self.min_y + 1, self.min_z + 1

        self.padding = 0.25
        self.velo = 0
        self.mass = mass
        self.is_jumping = False

    def jump(self):
        self.velo = 0.2
        self.is_jumping = True

    def update(self, dt):
        if self.is_jumping:
            self.velo -= self.mass * dt
            self.position.z += self.velo
            print("test")

        # # Calculate force (F). F = 0.5 * mass * velocity^2.
        # if self.velo > 0:
        #     F = (0.5 * self.mass * (self.velo * self.velo))
        # else:
        #     F = -(0.5 * self.mass * (self.velo * self.velo))
        #
        # # Change position
        # self.position.z = self.position.z - F
        #
        # # Change velocity
        # self.position.z = self.position.z - 1

        # If ground is reached, reset variables.
        if self.position.z <= 0:
            self.is_jumping = False
            self.velo = 0
