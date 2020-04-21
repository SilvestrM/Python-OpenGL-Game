from game_objects.Cube import Cube
from game_objects.Panel import Panel
from game_objects.Skybox import Skybox
from levels.Level import Level
from model.Vector import Vector
from utils.Utils import load_texture


class Initial(Level):
    def __init__(self):
        texture2 = load_texture('stoneWall2.jpg')
        texture1 = load_texture('dirt1.jpg')
        texture3 = load_texture('woodenWall4.jpg')
        texture_hedge = load_texture('stoneWall4.jpg')
        texture_ceil = 'darkstone1.jpg'
        self.ambience = 'desertambientl.wav'

        self.skybox = Skybox("skybox1.png")

        self.solids = []

        max = 20
        for i in range(-max, max, 2):
            for j in range(-max, max, 2):
                panel1 = Panel([1.0, 0.5, 0], texture1)
                panel1.set_position(Vector(i, j, 0))
                self.solids.append(panel1)

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
        wall1 = Panel([1.0, 0.5, 0], texture3)
        wall1.set_position(Vector(0, 4, 0), 90, Vector(0, 1, 0))
        self.solids.append(wall1)

        # Maze
        cubeWall = Cube([0, 1.0, 0], texture3)
        cubeWall.set_position(Vector(6, 8, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture3)
        cubeWall.set_position(Vector(4, 8, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture3)
        cubeWall.set_position(Vector(6, 10, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture3)
        cubeWall.set_position(Vector(4, 10, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture3)
        cubeWall.set_position(Vector(-2, 10, 0))
        self.solids.append(cubeWall)
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
        cubeWall.set_position(Vector(-6, 4, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-12, 4, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-12, 6, 0))
        self.solids.append(cubeWall)

        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-6, 6, 0))
        self.solids.append(cubeWall)

        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-6, 8, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-6, 10, 0))
        self.solids.append(cubeWall)

        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-6, 13, 0), scale=Vector(2,1,2))
        self.solids.append(cubeWall)

        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-8, 14, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-10, 14, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-14, 14, 0))
        self.solids.append(cubeWall)

        cubeWall = Cube([0, 1.0, 0], texture_hedge)
        cubeWall.set_position(Vector(-16, 12, 0))
        self.solids.append(cubeWall)

        for i in range(0,20,2):
            cubeWall = Cube([0, 1.0, 0], texture_hedge)
            cubeWall.set_position(Vector(-18, 12 - i, 0))
            self.solids.append(cubeWall)

        cubeWall = Cube([0, 1.0, 0], texture_hedge)
        cubeWall.set_position(Vector(-16, 2, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture_hedge)
        cubeWall.set_position(Vector(-16, 0, 0))
        self.solids.append(cubeWall)

        cubeWall = Cube([0, 1.0, 0], texture_hedge)
        cubeWall.set_position(Vector(-14, -4, 0))
        self.solids.append(cubeWall)

        cubeWall = Cube([0, 1.0, 0], texture_hedge)
        cubeWall.set_position(Vector(-16, -4.5, 0), scale=Vector(1,0.5,1))
        self.solids.append(cubeWall)


        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-14, 12, 0))
        self.solids.append(cubeWall)

        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-14, 10, 0))
        self.solids.append(cubeWall)

        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-12, 10, 0))
        self.solids.append(cubeWall)

        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-10, 10, 0))
        self.solids.append(cubeWall)

        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-10, 4, 0), scale=Vector(1.5,0.5,1))
        self.solids.append(cubeWall)

        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-9, 6, 0), scale=Vector(0.5, 1.5, 1))
        self.solids.append(cubeWall)

        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-14, 6, 0))
        self.solids.append(cubeWall)

        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-4, 10, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-4, 14, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture3)
        cubeWall.set_position(Vector(-2, 14, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture3)
        cubeWall.set_position(Vector(0, 14, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture3)
        cubeWall.set_position(Vector(2, 14, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture3)
        cubeWall.set_position(Vector(4, 14, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture3)
        cubeWall.set_position(Vector(4, 12, 0))
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
        cubeWall.set_position(Vector(-12, -6, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-12, -10, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-12, -12, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-10, -12, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-8, -12, 0))
        self.solids.append(cubeWall)


        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-8, -4, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-8, -6, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-8, -8, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-6, -8, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-4, -8, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-2, -8, 0))
        self.solids.append(cubeWall)

        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-2, -2, 0))
        self.solids.append(cubeWall)

        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(0, -2, 0))
        self.solids.append(cubeWall)

        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-6, 0, 0))
        self.solids.append(cubeWall)

        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-8, 0, 0))
        self.solids.append(cubeWall)

        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(-2, -6, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture3)
        cubeWall.set_position(Vector(-4, -4, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture3)
        cubeWall.set_position(Vector(-2, -4, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(0, -4, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(2, -4, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(4, -4, 0))
        self.solids.append(cubeWall)
        cubeWall = Cube([0, 1.0, 0], texture2)
        cubeWall.set_position(Vector(6, -4, 0))
        self.solids.append(cubeWall)



        cubeWall = Cube([0, 1.0, 0], texture3)
        cubeWall.set_position(Vector(0, 8, 0), scale=Vector(2, 2, 2))
        self.solids.append(cubeWall)
