import collections

grid = []


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def steps(start, end, p):
    s = 0
    for k in p.keys():
        s += dist(start, k)
        start = k
        if k == end:
            return s


with open('input') as ifile:
    for line in ifile:
        x = 0
        y = 0
        path = collections.OrderedDict()
        for p in line.split(','):
            direction = p[0]
            amount = int(p[1:])

            while amount > 0:
                if direction is 'U':
                    y -= 1
                if direction is 'D':
                    y += 1
                if direction is 'L':
                    x -= 1
                if direction is 'R':
                    x += 1

                path[(x, y)] = (x, y)
                amount -= 1
        grid.append(path)

min_dist = 100000000
min_steps = 100000000
origo = (0, 0)

for i in grid[0]:
    if i in grid[1]:
        min_dist = min(min_dist, dist(origo, i))
        min_steps = min(min_steps, steps(origo, i, grid[0]) + steps(origo, i, grid[1]))

print(min_dist)
print(min_steps)
