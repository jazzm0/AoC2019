add = 1
mul = 2
halt = 99


def convert(s):
    return [int(i) for i in s.split(',')]


def calc(op, a, b, s):
    if op == add:
        return a + b
    if op == mul:
        return a * b


with open('input') as ifile:
    for line in ifile:
        line = convert(line)
        line[1] = 12
        line[2] = 2
        index = 0
        while index < len(line):
            operation = line[index]
            if operation == halt:
                print(line[0])
                exit()
            operand_a = line[line[index + 1]]
            operand_b = line[line[index + 2]]
            line[line[index + 3]] = calc(operation, operand_a, operand_b, line)
            index += 4
