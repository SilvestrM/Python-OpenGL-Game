import math

from display.Player import Player
from game_objects.Axes import Axes
from game_objects.Cube import Cube
from game_objects.Panel import Panel
from levels.Level import Level
from model.Vector import Vector
from utils import Utils


class Scene:
    solids = []

    def __init__(self, size: tuple, level: Level):
        self.angle = 0
        self.camera_speed = 3
        self.FPS = 1000 / 60
        self.cam_x = 0
        self.cam_y = 0

        self.solids = level.solids

        self.size = size
        texture1 = 'brokenBricks.jpg'
        texture2 = 'dirt1.jpg'
        texture3 = 'woodenWall1.jpg'

        # self.camera = Camera(Vector(25, 0.0, 0.0), 90, -20, 1)
        self.player = Player(0.5, Vector(4, 0, 0), 0, 0, 1)

        # gluPerspective(90, (self.win_size[0] / self.win_size[1]), 0.1, 50.0)

        self.axes = Axes()

    def update(self, dt, moved):
        # if self.camera.position.z > 0 and not self.camera.is_jumping:
        #     self.camera.position.z -= dt * self.camera.mass
        # elif self.camera.position.z < 0.5 and not self.camera.is_jumping:
        #     self.camera.position.z += dt * self.camera_speed
        self.player.update(dt)

        collides = False
        direction = ""
        collided_objects = []
        padding = self.player.padding

        if moved:
            for solid in self.solids:
                if isinstance(solid, Cube):
                    collides = Utils.insersects_point(self.player.position, solid, padding)
                    if collides:
                        solid.center_dist = math.sqrt(
                            math.pow(
                                self.player.position.x - solid.position.x, 2) + math.pow(
                                self.player.position.y - solid.position.y, 2) + math.pow(
                                self.player.position.z - solid.position.z, 2))
                        collided_objects.append(solid)
                        print("solid- senter", solid.center_dist)
                        break

        if len(collided_objects) > 0:
            collided_objects.sort(key=lambda x: x.center_dist, reverse=True)

            # for collided_object in collided_objects:
            #     center_dist = self.camera.position.add(Vector(padding, padding, padding)).sub(
            #         collided_object.position)
            for collided_object in collided_objects:
                print(collided_object.center_dist)
                center_dist = self.player.position.add(Vector(padding, padding, padding)).sub(collided_object.position)
                # center_dist = collided_object.center_dist

                dist_min_x = math.fabs(self.player.position.x + padding - collided_object.min_x)
                dist_max_x = math.fabs(self.player.position.x + padding - collided_object.max_x)
                dist_min_y = math.fabs(self.player.position.y + padding - collided_object.min_y)
                dist_max_y = math.fabs(self.player.position.y + padding - collided_object.max_y)
                dist_min_z = math.fabs(self.player.position.z - collided_object.min_z)
                dist_max_z = math.fabs(self.player.position.z - collided_object.max_z)

                distances = [dist_min_x - math.fabs(center_dist.x), dist_max_x - math.fabs(center_dist.x),
                             dist_min_y - math.fabs(center_dist.y), dist_max_y - math.fabs(center_dist.y),
                             dist_min_z - math.fabs(center_dist.z), dist_max_z - math.fabs(center_dist.z)]

                print("nX", dist_min_x, "-", distances[0])
                print("xX", dist_max_x, "-", distances[1])
                print("nY", dist_min_y, "-", distances[2])
                print("xY", dist_max_y, "-", distances[3])
                print("nZ", dist_min_z, "-", distances[4])
                print("xZ", dist_max_z, "-", distances[5])
                print("center", center_dist.to_string())

                minimum = min(range(len(distances)), key=distances.__getitem__)

                print("min", minimum)
                # if din

                # min x
                if minimum == 0:
                    if distances[0] == distances[2] and not distances[0] == distances[3]:
                        self.player.position.y = collided_object.min_y - padding
                        self.player.position.x = collided_object.min_x - padding
                    elif distances[0] == distances[3] and not distances[0] == distances[2]:
                        self.player.position.x = collided_object.min_x - padding
                        self.player.position.y = collided_object.max_y + padding
                    else:
                        self.player.position.x = collided_object.min_x - padding
                # max x
                if minimum == 1:
                    if distances[1] == distances[2] and not distances[1] == distances[3]:
                        self.player.position.y = collided_object.min_y - padding
                        self.player.position.x = collided_object.max_x + padding
                    elif distances[1] == distances[3] and not distances[1] == distances[2]:
                        self.player.position.y = collided_object.max_y + padding
                        self.player.position.x = collided_object.max_x + padding
                    else:
                        self.player.position.x = collided_object.max_x + padding

                # min y
                if minimum == 2:
                    if distances[0] == distances[2] and not distances[1] == distances[2]:
                        self.player.position.x = collided_object.min_x - padding
                        self.player.position.y = collided_object.min_y - padding
                    elif distances[1] == distances[2] and not distances[0] == distances[2]:
                        self.player.position.x = collided_object.max_x + padding
                        self.player.position.y = collided_object.min_y - padding
                    else:
                        self.player.position.y = collided_object.min_y - padding

                # max y
                if minimum == 3:
                    if distances[0] == distances[3] and not distances[1] == distances[3]:
                        self.player.position.y = collided_object.max_y + padding
                        self.player.position.x = collided_object.min_x - padding
                    elif distances[1] == distances[3] and not distances[0] == distances[3]:
                        self.player.position.y = collided_object.max_y + padding
                        self.player.position.x = collided_object.max_x + padding
                    else:
                        self.player.position.y = collided_object.max_y + padding
                if minimum == 4:
                    self.player.position.z = collided_object.min_z - padding
                if minimum == 5:
                    self.player.position.z = collided_object.max_z + padding

        if self.player.position.z < 0:
            self.player.position.z = 0

