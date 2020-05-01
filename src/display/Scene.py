import math

import pyglet

from display.Player import Player
from game_objects.Axes import Axes
from game_objects.Cube import Cube
from game_objects.Panel import Panel
from levels.Level import Level
from model.Collidable import Collidable
from model.Solid import Solid
from model.Vector import Vector
from utils import Utils


class Scene:
    solids = []

    def __init__(self, size: tuple, level: Level):

        self.collided_number = None
        self.render_distance = 100



        self.prev_collision = ''
        self.fog_density = 0.05
        self.fog_mode = 0

        self.solids = level.solids
        self.skybox = level.skybox

        # Ambience track

        self.ambience_player = pyglet.media.Player()
        self.ambience_player.queue(pyglet.media.StaticSource(pyglet.resource.media(level.ambience)))
        self.ambience_player.volume = 0.5
        self.ambience_player.loop = True
        self.ambience_player.play()

        self.size = size

        self.player = Player(1, Vector(4, 0, 0), 0, 0, 1)
        self.ground_zero = self.player.height / 2
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

        self.player.update_pos(dt)
        self.player.update_physics(dt, self.ground_zero)
        # Collisions logic

        collided_objects = []

        for solid in self.solids:
            if hasattr(solid, 'bounding_box'):
                center_dist = math.sqrt(
                    math.pow(
                        self.player.position.x - solid.position.x, 2) + math.pow(
                        self.player.position.y - solid.position.y, 2) + math.pow(
                        self.player.position.z - solid.position.z, 2))
                max_size = max(solid.sizes)

                # To check just solids that are close
                if center_dist > max_size + 2:
                    continue

                collides = Utils.collides_box(self.player.bounding_box, solid.bounding_box)
                # collides = Utils.collides_point(self.player.position, solid.bounding_box, padding)

                if collides:
                    print("tru")
                    collided_objects.append(solid)

        self.collided_number = len(collided_objects)
        if len(collided_objects) > 0:
            # collided_objects.sort(key=lambda x: x.center_dist, reverse=True)

            position = self.player.position.normalise()

            for collided_object in collided_objects:

                box = collided_object.bounding_box
                player = self.player.bounding_box

                # Collision at corners
                center_dist = self.player.position.sub(collided_object.position)

                dist_min_x = math.fabs(player.max_x - box.min_x)
                dist_max_x = math.fabs(player.min_x - box.max_x)
                dist_min_y = math.fabs(player.max_y - box.min_y)
                dist_max_y = math.fabs(player.min_y - box.max_y)
                dist_min_z = math.fabs(player.max_z - box.min_z)
                dist_max_z = math.fabs(player.min_z - box.max_z)

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

                # works best
                # mai x
                if minimum == 0:
                    self.player.position.x = box.min_x - player.size_x
                # max x
                if minimum == 1:
                    self.player.position.x = box.max_x + player.size_x
                # min y
                if minimum == 2:
                    self.player.position.y = box.min_y - player.size_y
                # max y
                if minimum == 3:
                    self.player.position.y = box.max_y + player.size_y
                # min z
                if minimum == 4:
                    self.player.position.z = box.min_z - player.size_z
                # max z
                if minimum == 5:
                    self.player.position.z = box.max_z + player.size_z

        # Ground

        if self.player.position.z < self.ground_zero:
            self.player.position.z = self.ground_zero
        self.player.update(dt)
