import collections

grid = []


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


with open('input') as ifile:
    for line in ifile:
        x = 0
        y = 0
        d = 0
        path = collections.OrderedDict()
        for p in line.split(','):
            direction = p[0]
            amount = int(p[1:])

            while amount > 0:
                if direction is 'U':
                    y -= 1
                elif direction is 'D':
                    y += 1
                elif direction is 'L':
                    x -= 1
                elif direction is 'R':
                    x += 1

                d += 1
                if path.get((x, y)) is None:
                    path[(x, y)] = d
                amount -= 1
        grid.append(path)

print(min([dist((0, 0), i) for i in grid[0] if i in grid[1]]))
print(min([(grid[0][i] + grid[1][i]) for i in grid[0] if i in grid[1]]))
