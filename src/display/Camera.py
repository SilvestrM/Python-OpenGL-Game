import math

from OpenGL.raw.GLU import gluLookAt

from model.Vector import Vector


class Camera:

    def __init__(self, position: Vector, azimuth, zenith, radius: float):
        self.azimuth = azimuth
        self.zenith = zenith
        self.radius = radius
        self.position = position
        self.view_vector = Vector(0.0, 0.0, 0.0)
        self.up_vector = Vector(0.0, 0.0, 0.0)

        self.eye = self.position
        self.view_center = Vector(0.0, 0.0, 0.0)
        self.set_matrix()

    def compute(self):
        self.view_vector = Vector(math.cos(self.azimuth) * math.cos(self.zenith),
                                  math.sin(self.azimuth) * math.cos(self.zenith),
                                  math.sin(self.zenith))
        self.up_vector = Vector(math.cos(self.azimuth) * math.cos(self.zenith + math.pi / 2),
                                math.sin(self.azimuth) * math.cos(self.zenith + math.pi / 2),
                                math.sin(self.zenith + math.pi / 2))

        self.eye = self.position
        self.view_center = self.eye.add(self.view_vector.multi_d(self.radius))

    def add_azimuth(self, ang):
        self.azimuth += ang

    def add_zenith(self, ang):
        # self.zenith += ang
        self.zenith = max(-math.pi / 2, min(self.zenith + ang, math.pi / 2))

    def move_forward(self, spd):
        # self.position = self.position.add(
        #     Vector(math.sin(self.azimuth) * math.cos(self.zenith),
        #            math.sin(self.zenith),
        #            -math.cos(self.azimuth) * math.cos(self.zenith)).multi_d(spd))

        self.position = self.position.add(self.view_vector.multi_d(spd))

        print(self.view_vector.to_string())

    def move_backward(self, spd):
        self.move_forward(-spd)

    def move_right(self, spd):
        self.position = self.position.add(
            Vector(math.cos(self.azimuth - math.pi / 2),
                   math.sin(self.azimuth - math.pi / 2),
                   0.0).multi_d(spd))

    def move_left(self, spd):
        self.move_right(-spd)

    def get_matrix(self):
        self.compute()

        return self.position

    def set_matrix(self):
        self.compute()
        gluLookAt(
            self.eye.x, self.eye.y, self.eye.z, self.view_center.x, self.view_center.y, self.view_center.z,
            self.up_vector.x, self.up_vector.y, self.up_vector.z)
