from numpy.linalg import norm
from sympy import Point
import numpy as np
import math

asteroids = set()


def normalize(vector):
    return Point(np.sign(vector[0]), np.sign(vector[1]))


def distance(a, b, c):
    return a


def distance(a, b):
    return math.sqrt(((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2))


def count(center, neighbour, points, checked):
    normalized = set()
    for point in points:
        if point not in checked and Point.is_collinear(center, neighbour, point):
            checked.add(point)
            normalized.add(normalize(Point(center[0] - point[0], center[1] - point[1])))
    return len(normalized)


def shoot(center, target, points):
    actual_target = None
    actual_target_distance = 100
    ct = distance(center, target)
    for point in points:
        if Point.is_collinear(center, target, point) and distance(target, point) <= ct:
            actual_distance = distance(center, point)
            if actual_distance < actual_target_distance:
                actual_target_distance = actual_distance
                actual_target = point
    # TODO calculate next target
    next_target_distance = 100
    next_target = None
    for point in points:
        possible_next_distance = distance(center, actual_target, point)
        if possible_next_distance < next_target_distance:
            next_target_distance = possible_next_distance
            next_target = point
    return actual_target, next_target


def collect(point, a):
    a.remove(point)
    checked = set()
    visible = 0
    for i in a:
        visible += count(point, i, a, checked)
    return visible


with open('input') as ifile:
    y = 0
    for line in ifile:
        for x in range(len(line[:-1])):
            X = x
            if line[x] == '#':
                asteroids.add(Point(x, y))
        Y = y
        y += 1

maxCount = 0

# for p in asteroids:
#     v = collect(p, asteroids.copy())
#     # print(p, v)
#     if v > maxCount:
#         maxCount = v
#         maxCoord = p
# print('\n\n\n\n')
# print(maxCoord, maxCount)

# Point2D(22, 28) 326
center = Point(22, 28)
target = Point(22, 0)
# asteroids.remove(center)
# shots = []
# for p in asteroids.copy():
#     shot, next_target = shoot(center, target, asteroids)
#     shots.append(shot)
#     asteroids.remove(shot)
#     if len(shots) == 200:
#         break
#     target = next_target

p1 = np.array([0, 0])
p2 = np.array([10, 10])
p3 = np.array([1, 1])
d = np.cross(p2 - p1, p3 - p1) / norm(p2 - p1)
