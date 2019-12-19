from sympy import Point
import numpy as np

asteroids = set()
X = 0
Y = 0


def normalize(vector):
    return Point(np.sign(vector[0]), np.sign(vector[1]))


def count(center, neighbour, points, checked):
    normalized = set()
    for point in points:
        if point not in checked and Point.is_collinear(center, neighbour, point):
            checked.add(point)
            normalized.add(normalize(Point(center[0] - point[0], center[1] - point[1])))
    return len(normalized)


def collect(point, a):
    a.remove(point)
    checked = set()
    visible = 0
    for i in a:
        visible += count(point, i, a, checked)
    return visible


with open('d ') as ifile:
    y = 0
    for line in ifile:
        for x in range(len(line[:-1])):
            X = x
            if line[x] == '#':
                asteroids.add(Point(x, y))
        Y = y
        y += 1

maxCount = 0

for p in asteroids:
    v = collect(p, asteroids.copy())
    print(p, v)
    if v > maxCount:
        maxCount = v
        maxCoord = p
print('\n\n\n\n')
print(maxCoord, maxCount)
