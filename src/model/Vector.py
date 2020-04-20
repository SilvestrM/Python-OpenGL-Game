class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, v):
        return Vector(self.x + v.x, self.y + v.y, self.z + v.z)

    def __add__(self, v):
        return Vector(self.x + v, self.y + v, self.z + v)

    def sub(self, v):
        return Vector(self.x - v.x, self.y - v.y, self.z - v.z)

    def __sub__(self, v: float or int):
        return Vector(self.x - v, self.y - v, self.z - v)

    def multi_v(self, v: super):
        return Vector(self.x * v.x, self.y * v.y, self.z * v.z)

    def multi_d(self, v):
        return Vector(self.x * v, self.y * v, self.z * v)

    def multi_m(self, m: list or tuple):
        return Vector(m[0] * self.x + m[3] * self.y + m[6] * self.z,
                      m[1] * self.x + m[4] * self.y + m[7] * self.z,
                      m[2] * self.x + m[5] * self.y + m[8] * self.z)

    def normalise(self):
        return Vector(int(round(self.x)), int(round(self.y)), int(round(self.z)))

    def to_string(self):
        return str.format(str(self.x) + ":" + str(self.y) + ":" + str(self.z))
