s = 0


def calc_fuel(a):
    if a <= 0:
        return 0
    f = max((int(a) // 3) - 2, 0)
    return f + calc_fuel(f)


with open('input') as ifile:
    for line in ifile:
        s += calc_fuel(int(line))

print(s)
