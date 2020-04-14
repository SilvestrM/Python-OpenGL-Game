class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, v):
        return Vector(self.x + v.x, self.y + v.y, self.z + v.z)

    def multi_v(self, v):
        return Vector(self.x * v.x, self.y * v.y, self.z * v.z)

    def multi_d(self, v):
        return Vector(self.x * v, self.y * v, self.z * v)

    def to_string(self):
        return str.format(str(self.x) + str(self.y) + str(self.z))
