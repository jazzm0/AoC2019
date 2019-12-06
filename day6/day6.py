g = {}
d = {}
e = {}
with open('input') as ifile:
    for line in ifile:
        p = line[:-1].split(')')
        key = p[0]
        children = g.get(key, set())
        children.add(p[1])
        g[key] = children

d['COM'] = 0
keys = ['COM']
level = 1


def travel(node, lev):
    if g.get(node) is None:
        return
    for i in g[node]:
        d[i] = lev + 1
        travel(i, lev + 1)


travel('COM', 0)

print(sum(d.values()))
