from game_objects.Cube import Cube
from game_objects.Panel import Panel
from levels.Level import Level
from model.Vector import Vector


class Initial(Level):
    def __init__(self):
        texture2 = 'stoneWall1.jpg'
        texture1 = 'dirt1.jpg'
        texture3 = 'woodenWall1.jpg'
        texture_ceil = 'darkstone1.jpg'

        cube1 = Cube([1.0, 0, 0], texture1)
        cube1.set_position(Vector(0, -2, -9))

        # panel1 = Panel([1.0, 0, 0], texture1)
        # panel1.set_position(Vector(0, 0, 0), Vector(2, 2, 0))

        self.solids.append(cube1)
        # self.solids.append(panel1)

        cube2 = Cube([0, 1.0, 0], texture2)
        cube2.set_position(Vector(4, -8, 10))

        cube3 = Cube([0, 1.0, 0], texture2)
        cube3.set_position(Vector(2, 12, 2))

        self.solids.append(cube2)
        self.solids.append(cube3)

        max = 20
        i = -max
        while True:
            if i >= max: break
            j = -max
            while True:
                if j >= max: break
                panel1 = Panel([1.0, 0.5, 0], texture1)
                panel1.set_position(Vector(i, j, 0))
                self.solids.append(panel1)
                j += 2
            i += 2

        # i = -max
        # while True:
        #     if i >= max: break
        #     j = -max
        #     while True:
        #         if j >= max: break
        #         panel1 = Panel([0.05, 0.05, 0.05], texture3)
        #         panel1.set_position(Vector(i, j, -1), 180, Vector(0, 1, 0))
        #         self.solids.append(panel1)
        #         j += 2
        #     i += 2

        # panelc = Panel([1.0, 0.5, 0], texture_ceil)
        # panelc.set_position(Vector(0, 0, -1), 180, Vector(0, 1, 0), Vector(20,20,0))
        # self.solids.append(panelc)

        wall1 = Panel([1.0, 0.5, 0], texture2)
        wall1.set_position(Vector(0, 0, -2), 90, Vector(1, 0, 0))
        self.solids.append(wall1)
        wall1 = Panel([1.0, 0.5, 0], texture2)
        wall1.set_position(Vector(-3, 0, -2))
        wall1.rotate(Vector(1, 0, 0), 90)
        wall1.rotate(Vector(0, 1, 0), 180)
        self.solids.append(wall1)

        # Maze

        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(2, 2, 0))
        self.solids.append(cubeWall)

        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(4, 2, 0))
        self.solids.append(cubeWall)

        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-2, 2, 0))
        self.solids.append(cubeWall)

        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-4, 2, 0))
        self.solids.append(cubeWall)

        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-6, 2, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-8, 2, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-10, 2, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-12, 2, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-12, 0, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-12, -2, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-12, -4, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-8, -4, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-8, -6, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture3)
        cubeWall.set_position(Vector(-4, -4, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture3)
        cubeWall.set_position(Vector(-2, -4, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture3)
        cubeWall.set_position(Vector(0, -4, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture3)
        cubeWall.set_position(Vector(2, -4, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture3)
        cubeWall.set_position(Vector(4, -4, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture3)
        cubeWall.set_position(Vector(6, -4, 0))
        self.solids.append(cubeWall)
