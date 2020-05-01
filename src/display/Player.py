from display.Camera import Camera
from model.BoundingBox import BoundingBox
from model.Vector import Vector


class Player(Camera):
    is_crouching = False

    def __init__(self, mass, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.height = 0.5
        self.bounding_box = BoundingBox(self.position, 0.4, 0.4, self.height)
        self.speed = 3

        self.padding = 0.25
        self.acc = 0
        self.mass = mass
        self.is_jumping = False
        self.G_constant = 1
        self.r = self.position.z - 0
        self.velo = 9.8

    def jump(self):
        if not self.is_jumping:
            self.velo = 2
            self.is_jumping = True

    def gravity(self):
        g = -9.81
        df = 0.5 * 0.1 * (self.velo * abs(self.velo))
        da = df / self.mass
        return g - da

    def crouch(self):
        self.is_crouching = not self.is_crouching

    def update_pos(self, dt):
        self.bounding_box.recalculate_position(self.position)

    def update_physics(self, dt, ground):

        if self.position.z > ground:
            # self.position.z -= (9.8 * self.velo * dt) / self.mass
            self.position.z = self.position.z + self.velo * dt + self.acc * (dt * dt * 0.5)
            acc_n = self.gravity()
            self.velo = self.velo + (self.acc + acc_n) * (dt * 0.5)
            self.acc = acc_n

        if self.is_jumping:
            self.velo -= self.mass * dt
            self.position.z += self.velo * dt

        if self.velo <= self.acc:
            self.is_jumping = False

    def update(self, dt):
        if self.is_crouching:
            self.bounding_box.size_z -= self.bounding_box.size_z * 0.75
            self.position.z -= 0.75
        else:
            self.bounding_box.size_z = self.height