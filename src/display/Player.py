from display.Camera import Camera
from model.Collidable import Collidable
from model.Vector import Vector


class Player(Camera):
    def __init__(self, mass, position: Vector, azimuth, zenith, radius: float):
        super().__init__(position, azimuth, zenith, radius)

        self.min_x, self.min_y, self.min_z = self.position.x - 0.5, self.position.y - 0.5, self.position.z - 0.5
        self.max_x, self.max_y, self.max_z = self.min_x + 1, self.min_y + 1, self.min_z + 1

        self.padding = 0.25
        self.acc = 0
        self.mass = mass
        self.is_jumping = False
        self.G_constant = 1
        self.r = self.position.z - 0
        self.velo = 9.8

    def jump(self):
        if not self.is_jumping:
            self.velo = 10
            self.is_jumping = True

    def gravity(self):
        g = -9.81
        df = 0.5 * 0.1 * (self.velo * abs(self.velo))
        da = df / self.mass
        return g - da

    def update(self, dt):
        if self.position.z > 0:
            # self.position.z -= (9.8 * self.velo * dt) / self.mass
            self.position.z = self.position.z + self.velo * dt + self.acc * (dt * dt * 0.5)
            acc_n = self.gravity()
            self.velo = self.velo + (self.acc + acc_n) * (dt * 0.5)
            self.acc = acc_n

        if self.is_jumping:
            self.velo -= self.mass * dt
            self.position.z += self.velo * dt
            print(self.acc, self.velo, self.position.z)

        if self.velo <= self.acc:
            self.is_jumping = False
