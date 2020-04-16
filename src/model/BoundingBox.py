from model.Vector import Vector


class BoundingBox:
    def __init__(self, position, size_x, size_y, size_z):
        self.min_x, self.min_y, self.min_z = position.x - size_x, position.y - size_y, position.z - size_z
        self.max_x, self.max_y, self.max_z = position.x + size_x, position.y + size_y, position.z + size_z

        # min_x, min_y
        # min_x, max_y
        self.corners = [
            (self.min_x, self.min_y, self.min_z),
            (self.min_x, self.max_y, self.min_z),
            (self.max_x, self.min_y, self.min_z),
            (self.max_x, self.max_y, self.min_z),
            (self.min_x, self.min_y, self.max_z),
            (self.min_x, self.max_y, self.max_z),
            (self.max_x, self.min_y, self.max_z),
            (self.max_x, self.max_y, self.max_z),
        ]

        self.faces = [
            (self.corners[0], self.corners[1], self.corners[2], self.corners[3]),
            (self.corners[4], self.corners[5], self.corners[6], self.corners[7]),
            (self.corners[0], self.corners[1], self.corners[4], self.corners[5]),
            (self.corners[2], self.corners[3], self.corners[6], self.corners[7]),
            (self.corners[0], self.corners[2], self.corners[4], self.corners[6]),
            (self.corners[1], self.corners[3], self.corners[5], self.corners[7]),
        ]

    def recalculate_position(self, position, size_x, size_y, size_z):
        self.min_x, self.min_y, self.min_z = position.x - size_x, position.y - size_y, position.z - size_z
        self.max_x, self.max_y, self.max_z = position.x + size_x, position.y + size_y, position.z + size_z
        self.corners = [
            Vector(self.min_x, self.min_y, self.min_z),
            Vector(self.min_x, self.max_y, self.min_z),
            Vector(self.max_x, self.min_y, self.min_z),
            Vector(self.max_x, self.max_y, self.min_z),
            Vector(self.min_x, self.min_y, self.max_z),
            Vector(self.min_x, self.max_y, self.max_z),
            Vector(self.max_x, self.min_y, self.max_z),
            Vector(self.max_x, self.max_y, self.max_z),
        ]
