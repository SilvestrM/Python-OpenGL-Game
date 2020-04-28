import math

import pyglet

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
        self.render_distance = 100

        self.prev = ''
        self.fog_density = 0.05
        self.fog_mode = 0

        self.solids = level.solids
        self.skybox = level.skybox

        # Ambience track

        self.ambience_player = pyglet.media.Player()
        self.ambience_player.queue(pyglet.media.StaticSource(pyglet.media.load('../resources/SFX/' + level.ambience)))
        self.ambience_player.volume = 0.5
        self.ambience_player.loop = True
        self.ambience_player.play()

        self.size = size

        self.player = Player(1, Vector(4, 0, 0), 0, 0, 1)

        self.axes = Axes()

    def toggle_fog_mode(self):
        if self.fog_mode == 0:
            self.fog_mode = 1
        else:
            self.fog_mode = 0

    def update(self, dt, moved):
        if self.fog_mode != 0:
            self.fog_density = 0.25
        else:
            self.fog_density = 0.05

        self.player.update(dt)

        # Collisions logic

        collided_objects = []
        padding = self.player.padding

        if moved:
            for solid in self.solids:
                if isinstance(solid, Cube):
                    center_dist = math.sqrt(
                        math.pow(
                            self.player.position.x - solid.position.x, 2) + math.pow(
                            self.player.position.y - solid.position.y, 2) + math.pow(
                            self.player.position.z - solid.position.z, 2))
                    max_size = max(solid.sizes)

                    if center_dist > max_size + 2:
                        continue
                    collides = Utils.collides_point(self.player.position, solid.bounding_box, padding)
                    if collides:
                        print("tru")
                        collided_objects.append(solid)

        if len(collided_objects) > 0:
            collided_objects.sort(key=lambda x: x.center_dist, reverse=True)
            print("solid - center", collided_objects)
            # self.prev = ''

            # for collided_object in collided_objects:
            #     center_dist = self.camera.position.add(Vector(padding, padding, padding)).sub(
            #         collided_object.position)
            position = self.player.position.normalise()

            for collided_object in collided_objects:
                print(collided_object.center_dist)

                # center_dist = collided_object.center_dist
                # for corner in collided_object.bounding_box.corners:
                #     if player.position < corner

                # if collided_object.bounding_box.min.x < self.player.position.x + padding < collided_object.bounding_box.max_x: and

                # for face in collided_object.bounding_box.faces:
                #     for corner in face:
                #         for i in range(3):
                #             if not corner[i]:
                #                 continue
                #             overlap = (position[i] - norm_position[i]) * corner[i]
                #             print(overlap)
                #             if overlap < padding:
                #                 continue
                #             position[i] -= (overlap - padding) * corner[i]
                #             break
                # self.player.position = Vector(position[0], position[1], position[2])
                box = collided_object.bounding_box

                diff = self.player.position.sub(position)
                print("no", box.max_x)
                print("no", position.x)

                print("diff", diff.x - padding)
                print("diff", diff.y - padding)

                print("prev", self.prev)
                # bottom
                if box.min_x < position.x < box.max_x and box.min_y < position.y < box.max_y and position.z == box.min_z:
                    self.player.position.z = box.min_z - padding
                    self.prev = "min_z"
                    continue
                # top
                if box.min_x < position.x < box.max_x and box.min_y < position.y < box.max_y and position.z == box.max_z:
                    self.player.position.z = box.max_z + padding
                    self.prev = "max_z"
                    continue
                if position.x == box.min_x and box.min_y < position.y < box.max_y and box.min_z < position.z < box.max_z:
                    self.player.position.x = box.min_x - padding
                    self.prev = "min_x"
                    continue
                if position.x == box.max_x and box.min_y < position.y < box.max_y and box.min_z < position.z < box.max_z:
                    self.player.position.x = box.max_x + padding
                    self.prev = "max_x"
                    continue
                if box.min_x < position.x < box.max_x and position.y == box.min_y and box.min_z < position.z < box.max_z:
                    self.player.position.y = box.min_y - padding
                    self.prev = "min_y"
                    continue
                if box.min_x < position.x < box.max_x and position.y == box.max_y and box.min_z < position.z < box.max_z:
                    self.player.position.y = box.max_y + padding
                    self.prev = "max_y"
                    continue

                print("sec")
                # edges
                # if box.min_x <= position.x <= box.max_x and box.min_y <= position.y <= box.max_y and position.z == box.min_z:
                #     self.player.position.z = box.min_z - padding
                #     continue
                # if box.min_x <= position.x <= box.max_x and box.min_y <= position.y <= box.max_y and position.z == box.max_z:
                #     self.player.position.z = box.max_z + padding
                #     continue
                # if position.x == box.min_x and position.y == box.min_y and box.min_z < position.z < box.max_z:
                #     if self.prev == "min_x":
                #         self.player.position.x = box.min_x - (padding + dt)
                #         self.prev = "min_x"
                #     elif self.prev == "min_y":
                #         self.player.position.y = box.min_y - (padding + dt)
                #         self.prev = "min_y"
                #     else:
                #         self.player.position.x = box.min_x - padding
                #         self.player.position.y = box.min_y - padding
                #     print("one")
                #     continue
                # elif position.x == box.max_x and position.y == box.max_y and box.min_z < position.z < box.max_z:
                #     if self.prev == "max_x":
                #         self.player.position.x = box.max_x + (padding + dt)
                #         self.prev = "max_x"
                #     elif self.prev == "max_y":
                #         self.player.position.y = box.max_y + (padding + dt)
                #         self.prev = "max_y"
                #     else:
                #         self.player.position.x = box.max_x + padding
                #         self.player.position.y = box.max_y + padding
                #     print("one")
                #     continue
                # elif position.x == box.max_x and position.y == box.min_y and box.min_z < position.z < box.max_z:
                #     if self.prev == "max_x":
                #         self.player.position.x = box.max_x + (padding + dt)
                #         self.prev = "max_x"
                #     elif self.prev == "min_y":
                #         self.player.position.y = box.min_y - (padding + dt)
                #         self.prev = "min_y"
                #     else:
                #         self.player.position.x = box.max_x + padding
                #         self.player.position.y = box.min_y - padding
                #     print("one")
                #     continue
                # elif position.x == box.min_x and position.y == box.max_y and box.min_z < position.z < box.max_z:
                #     if self.prev == "min_x":
                #         self.player.position.x = box.min_x - (padding + dt)
                #         self.prev = "min_x"
                #     elif self.prev == "max_y":
                #         self.player.position.y = box.max_y + (padding + dt)
                #         self.prev = "max_y"
                #     else:
                #         self.player.position.x = box.min_x - padding
                #         self.player.position.y = box.max_y + padding
                #     print("one")
                #     continue
                #
                # elif position.x == box.min_x and position.z == box.max_z and box.min_y < position.y < box.max_y:
                #     if self.prev == "min_x":
                #         self.player.position.x = box.min_x - (padding + dt)
                #         self.prev = "min_x"
                #     elif self.prev == "max_z":
                #         self.player.position.z = box.max_z + (padding + dt)
                #         self.prev = "max_z"
                #     else:
                #         self.player.position.x = box.min_x - padding
                #         self.player.position.z = box.max_z + padding
                #     print("one")
                #     continue

                center_dist = self.player.position.add(Vector(padding, padding, padding)).sub(collided_object.position)

                dist_min_x = math.fabs(self.player.position.x + padding - box.min_x)
                dist_max_x = math.fabs(self.player.position.x + padding - box.max_x)
                dist_min_y = math.fabs(self.player.position.y + padding - box.min_y)
                dist_max_y = math.fabs(self.player.position.y + padding - box.max_y)
                dist_min_z = math.fabs(self.player.position.z + padding - box.min_z)
                dist_max_z = math.fabs(self.player.position.z + padding - box.max_z)

                distances = [dist_min_x - math.fabs(center_dist.x), dist_max_x - math.fabs(center_dist.x),
                             dist_min_y - math.fabs(center_dist.y), dist_max_y - math.fabs(center_dist.y),
                             dist_min_z - math.fabs(center_dist.z), dist_max_z - math.fabs(center_dist.z)]

                print("nX", dist_min_x, "- adjusted ", distances[0])
                print("xX", dist_max_x, "- adjusted ", distances[1])
                print("nY", dist_min_y, "- adjusted ", distances[2])
                print("xY", dist_max_y, "- adjusted ", distances[3])
                print("nZ", dist_min_z, "- adjusted ", distances[4])
                print("xZ", dist_max_z, "- adjusted ", distances[5])
                print("center", center_dist.to_string())

                minimum = min(range(len(distances)), key=distances.__getitem__)

                print("min", minimum)
                # if din

                # min x
                # if minimum == 0:
                #     if distances[0] == distances[2] and not distances[0] == distances[3]:
                #         self.player.position.y = collided_object.min_y - (padding + dt)
                #         self.player.position.x = collided_object.min_x - (padding + dt)
                #     elif distances[0] == distances[3] and not distances[0] == distances[2]:
                #         self.player.position.x = collided_object.min_x - (padding + dt)
                #         self.player.position.y = collided_object.max_y + (padding + dt)
                #     else:
                #         self.player.position.x = collided_object.min_x - padding
                # # max x
                # if minimum == 1:
                #     if distances[1] == distances[2] and not distances[1] == distances[3]:
                #         self.player.position.y = collided_object.min_y - (padding + dt)
                #         self.player.position.x = collided_object.max_x + (padding + dt)
                #     elif distances[1] == distances[3] and not distances[1] == distances[2]:
                #         self.player.position.y = collided_object.max_y + (padding + dt)
                #         self.player.position.x = collided_object.max_x + (padding + dt)
                #     else:
                #         self.player.position.x = collided_object.max_x + padding
                #
                # # min y
                # if minimum == 2:
                #     if distances[0] == distances[2] and not distances[1] == distances[2]:
                #         self.player.position.x = collided_object.min_x - (padding + dt)
                #         self.player.position.y = collided_object.min_y - (padding + dt)
                #     elif distances[1] == distances[2] and not distances[0] == distances[2]:
                #         self.player.position.x = collided_object.max_x + (padding + dt)
                #         self.player.position.y = collided_object.min_y - (padding + dt)
                #     else:
                #         self.player.position.y = collided_object.min_y - padding
                #
                # # max y
                # if minimum == 3:
                #     if distances[0] == distances[3] and not distances[1] == distances[3]:
                #         self.player.position.y = collided_object.max_y + (padding + dt)
                #         self.player.position.x = collided_object.min_x - (padding + dt)
                #     elif distances[1] == distances[3] and not distances[0] == distances[3]:
                #         self.player.position.y = collided_object.max_y + (padding + dt)
                #         self.player.position.x = collided_object.max_x + (padding + dt)
                #     else:
                #         self.player.position.y = collided_object.max_y + padding

                # works best

                if minimum == 0:
                    self.player.position.x = box.min_x - padding
                # max x
                if minimum == 1:
                    self.player.position.x = box.max_x + padding
                # min y
                if minimum == 2:
                    self.player.position.y = box.min_y - padding
                # max y
                if minimum == 3:
                    self.player.position.y = box.max_y + padding
                if minimum == 4:
                    self.player.position.z = box.min_z - padding
                if minimum == 5:
                    self.player.position.z = box.max_z + padding

        if self.player.position.z < 0:
            self.player.position.z = 0
