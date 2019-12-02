add = 1
mul = 2
halt = 99


def calc(op, a, b):
    if op == add:
        return a + b
    if op == mul:
        return a * b


def process(noun, verb, program):
    program[1] = noun
    program[2] = verb
    index = 0
    while index + 3 < len(program):
        operation = program[index]
        if operation == halt:
            if program[0] == 19690720:
                print(100 * noun + verb)
                exit()
            return program[0]
        program[program[index + 3]] = calc(operation, program[program[index + 1]], program[program[index + 2]])
        index += 4


with open('input') as ifile:
    for line in ifile:
        line = [int(i) for i in line.split(',')]
        # part 1
        print(process(12, 2, line.copy()))
        # part 2
        for i in range(1, 100):
            for j in range(1, 100):
                process(i, j, line.copy())
