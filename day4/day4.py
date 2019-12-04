f = 172930
t = 683082

count_one = 0
count_two = 0


def part_one(n):
    contains = False
    c = str(n)
    for i in range(len(c) - 1):
        if not contains and c[i] == c[i + 1]:
            contains = True
        if c[i] > c[i + 1]:
            return False
    return contains


def part_two(n):
    c = str(n)
    b = {}
    for i in range(len(c) - 1):
        if c[i] == c[i + 1]:
            b[c[i]] = b.get(c[i], 1) + 1

    for j in b.values():
        if j == 2:
            return True
    return False


for a in range(f, t):
    if part_one(a):
        count_one += 1
        if part_two(a):
            count_two += 1

print(count_one)
print(count_two)
