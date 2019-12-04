# 172930-683082

count = 0


def contains_two(a):
    c = str(a)
    for i in range(len(c) - 1):
        if c[i] == c[i + 1]:
            return True


for a in range(172930, 683082):
    if contains_two(a):
        print(a)
        count += 1

print(count)
