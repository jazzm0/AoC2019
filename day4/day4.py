f = 172930
t = 683082
count_one = 0
count_two = 0


def check(n):
    c = str(n)
    b = {}
    one, two = 0, 0
    for i in range(len(c) - 1):
        if c[i] == c[i + 1]:
            b[c[i]] = b.get(c[i], 1) + 1
        if c[i] > c[i + 1]:
            return one, two

    if any(j == 2 for j in b.values()):
        one = 1

    if len(b) > 0:
        two = 1
    return one, two


for a in range(f, t):
    o, t = check(a)
    count_one += o
    count_two += t
print(count_one)
print(count_two)
