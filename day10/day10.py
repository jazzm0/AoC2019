from sympy import Point, Line

asteroids = set()
X = 0
Y = 0


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def remove(v, vector, a):
    target = add(v, vector)
    while 0 <= target[0] <= X and 0 <= target[1] <= Y:
        if target in a:
            a.remove(target)
        target = add(target, vector)
    return a


def visible(point, a):
    a.remove(point)
    b = a.copy()
    for t in b:
        a = remove(t, (t[0] - point[0], t[1] - point[1]), a)
    return len(a)


with open('basic') as ifile:
    y = 0
    for line in ifile:
        for x in range(len(line[:-1])):
            X = x
            if line[x] == '#':
                asteroids.add(Point(x, y))
        Y = y
        y += 1


for p in asteroids:
    v = visible(p, asteroids.copy())
    print(p, v)
    if v > maxCount:
        maxCount = v
        maxCoord = p

print(maxCoord, maxCount)
