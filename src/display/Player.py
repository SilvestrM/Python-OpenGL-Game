from display.Camera import Camera
from model.BoundingBox import BoundingBox
from model.Collidable import Collidable


class Player(Camera, Collidable):
    _is_crouching = False

    @property
    def speed(self) -> float:
        return self._speed

    @property
    def height(self) -> float:
        return self._height

    @property
    def is_crouching(self) -> bool:
        return self._is_crouching

    def __init__(self, mass, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._height = 0.5
        self.bounding_box = BoundingBox(self.position, 0.4, 0.4, self._height)
        self._speed = 3

        self._acc = 0
        self._mass = mass
        self._is_jumping = False
        self._G_constant = 1
        self._r = self.position.z - 0
        self._velo = 9.8

    def jump(self):
        if not self._is_jumping:
            self._velo = 2
            self._is_jumping = True

    def gravity(self):
        g = -9.81
        df = 0.5 * 0.1 * (self._velo * abs(self._velo))
        da = df / self._mass
        return g - da

    def crouch(self):
        self._is_crouching = not self._is_crouching

    def update_pos(self, dt):
        self.bounding_box.recalculate_position(self.position)

    def update_physics(self, dt, ground):

        if self.position.z > ground:
            # self.position.z -= (9.8 * self.velo * dt) / self.mass
            self.position.z = self.position.z + self._velo * dt + self._acc * (dt * dt * 0.5)
            acc_n = self.gravity()
            self._velo = self._velo + (self._acc + acc_n) * (dt * 0.5)
            self._acc = acc_n

        if self._is_jumping:
            self._velo -= self._mass * dt
            self.position.z += self._velo * dt

        if self._velo <= self._acc:
            self._is_jumping = False

    def update(self, dt):
        if self._is_crouching:
            self.bounding_box.size_z -= self._height * 0.5
            self.position.z -= 0.5
        else:
            self.bounding_box.size_z = self._height


