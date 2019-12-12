asteroids = set()

maxX = 0
maxY = 0
points_checked = set()


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def remove(v, vector, a):
    target = add(v, vector)
    while 0 <= target[0] <= maxX and 0 <= target[1] <= maxY:
        if target in a:
            a.remove(target)
        target = add(target, vector)
    return a


def visible(point, a):
    for dist in range(max(maxX, maxY)):
        for x_temp in range(point[0] - dist, point[0] + dist):
            for y_temp in range(point[1] - dist, point[1] + dist):
                v = (x_temp, y_temp)
                if v not in points_checked:
                    points_checked.add(v)
                    if v in a and v != point:
                        a = remove(v, (v[0] - point[0], v[1] - point[1]), a)
    return len(a)


with open('input') as ifile:
    y = 0
    for line in ifile:
        for x in range(len(line[:-1])):
            maxX = max(x, maxX)
            maxY = max(y, maxY)
            if line[x] == '#':
                asteroids.add((x, y))
        y += 1

maxCount = 0
maxCoord = ()

for p in asteroids:
    v = visible(p, asteroids.copy())
    if v > maxCount:
        maxCount = v
        maxCoord = p

print(maxCoord, maxCount)
