from operator import add, mul

position_mode = '0'
immediate_mode = '1'

program_input = 1


def convert(instruction):
    instruction = str(instruction)
    r = []
    for i in range(len(instruction)):
        r.append(instruction[i])
    while len(r) < 5:
        r.insert(0, '0')
    return str(''.join(r))


def push():
    return program_input


def pop(value):
    print(value)


def halt():
    exit()


oc = {1: (add, 2, True), 2: (mul, 2, True), 3: (push, 0, True), 4: (pop, 1, False), 99: (halt, 0, False)}


def process():
    ip = 0
    while ip < len(program) - 1:
        instruction = convert(program[ip])
        op_code = int(instruction[-2:])
        op = oc[op_code][0]
        arg_values = []
        args = oc[op_code][1]
        for i in range(args):
            ip += 1
            index = program[ip]
            if instruction[2 - i] == position_mode:
                value = program[index]
            elif instruction[2 - i] == immediate_mode:
                value = index
            else:
                print('error')

            arg_values.append(value)

        ip += 1
        if oc[op_code][2]:
            program[program[ip]] = op(*arg_values)
            ip += 1
        else:
            op(*arg_values)


with open('input') as ifile:
    for line in ifile:
        program = [int(x) for x in line.split(',')]
        process()
