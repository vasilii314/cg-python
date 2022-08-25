import math

import numpy as np


class Matrix(object):

    @classmethod
    def make_identity(cls):
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ]).astype(float)

    @classmethod
    def make_translation(cls, x, y, z):
        return np.array([
            [1, 0, 0, x],
            [0, 1, 0, y],
            [0, 0, 1, z],
            [0, 0, 0, 1],
        ]).astype(float)

    @classmethod
    def make_rotation_x(cls, angle):
        c = math.cos(angle)
        s = math.sin(angle)
        return np.array([
            [1, 0, 0, 0],
            [0, c, -s, 0],
            [0, s, c, 0],
            [0, 0, 0, 1]
        ]).astype(float)

    @classmethod
    def make_rotation_y(cls, angle):
        c = math.cos(angle)
        s = math.sin(angle)
        return np.array([
            [c, 0, s, 0],
            [0, 1, 0, 0],
            [-s, 0, c, 0],
            [0, 0, 0, 1]
        ]).astype(float)

    @classmethod
    def make_rotation_z(cls, angle):
        c = math.cos(angle)
        s = math.sin(angle)
        return np.array([
            [c, -s, 0, 0],
            [s, c, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]).astype(float)

    @classmethod
    def make_scale(cls, s):
        return np.array([
            [s, 0, 0, 0],
            [0, s, 0, 0],
            [0, 0, s, 0],
            [0, 0, 0, 1],
        ]).astype(float)

    @classmethod
    def make_perspective(cls, angle_of_view=60, aspect_ratio=1, near=0.1, far=1000):
        a = angle_of_view * math.pi / 180.0
        d = 1.0 / math.tan(a / 2)
        r = aspect_ratio
        b = (far + near) / (near - far)
        c = 2 * far * near / (near - far)
        return np.array([
            [d / r, 0, 0, 0],
            [0, d, 0, 0],
            [0, 0, b, c],
            [0, 0, -1, 0],
        ]).astype(float)
