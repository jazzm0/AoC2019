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
    p = e.get(node, set())
    p.add(node)
    e[node] = p
    if g.get(node) is None:
        return
    for i in g[node]:
        q = e.get(i, set())
        for k in p:
            q.add(k)
        e[i] = q
        d[i] = lev + 1
        travel(i, lev + 1)


travel('COM', 0)

print(sum(d.values()))
path_a = e['SAN']
path_b = e['YOU']

path_a.remove('COM')
path_a.remove('SAN')
path_b.remove('COM')
path_b.remove('YOU')
print(len(path_a.difference(path_b)) + len(path_b.difference(path_a)))
