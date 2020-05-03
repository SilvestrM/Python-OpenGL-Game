import math

import pyglet

from display.Player import Player
from game_objects.Axes import Axes
from game_objects.Skybox import Skybox
from levels.Level import Level
from model.Vector import Vector
from utils import Utils


class Scene:
    _solids: list = []

    @property
    def collided_number(self) -> int:
        return self._collided_number

    @property
    def fog_mode(self) -> int:
        return self._fog_mode

    @property
    def fog_density(self) -> float:
        return self._fog_density

    @property
    def gravity(self) -> bool:
        return self._gravity

    @property
    def solids(self) -> list:
        return self._solids

    @property
    def skybox(self) -> Skybox:
        return self._skybox

    @property
    def size(self) -> tuple or list:
        return self._size

    @size.setter
    def size(self, size: tuple or list):
        self._size = size

    @property
    def render_distance(self) -> float:
        return self._render_distance

    def __init__(self, size: tuple, level: Level):

        self._collided_number = None
        self._render_distance = 100

        self._prev_collision = ''
        self._fog_density = 0.05
        self._fog_mode = 1

        self._solids = level.solids
        self._skybox = level.skybox
        self.flavor_color = level.flavor_color

        self._gravity = True

        # Ambience track

        self._ambience_player = pyglet.media.Player()
        self._ambience_player.queue(pyglet.media.StaticSource(pyglet.resource.media(level.ambience)))
        self._ambience_player.volume = 0.5
        self._ambience_player.loop = True
        self._ambience_player.play()

        self._size = size

        self.player = Player(1, Vector(4, 0, 1), 60, 0, 1)
        self._ground_zero = self.player.height / 2
        self.axes = Axes()

    def toggle_fog_mode(self):
        if self.fog_mode == 0:
            self._fog_mode = 1
        else:
            self._fog_mode = 0

    def toggle_gravity(self):
        self._gravity = not self._gravity

    def update(self, dt, moved):
        if self.fog_mode != 0:
            self._fog_density = 0.25
        else:
            self._fog_density = 0.05

        self.player.update_pos(dt)
        if self.gravity:
            self.player.update_physics(dt, self._ground_zero)

        # Collisions logic

        collided_objects = []

        for solid in self._solids:
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
                    # print("tru")
                    collided_objects.append(solid)

        self._collided_number = len(collided_objects)
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

                # print("nX", dist_min_x, "- adjusted ", distances[0])
                # print("xX", dist_max_x, "- adjusted ", distances[1])
                # print("nY", dist_min_y, "- adjusted ", distances[2])
                # print("xY", dist_max_y, "- adjusted ", distances[3])
                # print("nZ", dist_min_z, "- adjusted ", distances[4])
                # print("xZ", dist_max_z, "- adjusted ", distances[5])
                # print("center", center_dist.to_string())

                minimum = min(range(len(distances)), key=distances.__getitem__)

                # print("min", minimum)

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
        if self.player.position.z < self._ground_zero:
            self.player.position.z = self._ground_zero
        self.player.update(dt)
