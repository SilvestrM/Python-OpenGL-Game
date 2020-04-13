import pyglet


class Axes:
    vertices = ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1))
    edges = ((0, 1), (0, 2), (0, 3))
    colors = \
        ((1, 0, 0),  # x
         (0, 1, 0),  # y
         (0, 0, 1))  # z