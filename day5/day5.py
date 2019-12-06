from operator import add, mul

position_mode = '0'
immediate_mode = '1'

program_input = 5


def convert(instruction):
    instruction = str(instruction)
    r = []
    for i in range(len(instruction)):
        r.append(instruction[i])
    while len(r) < 5:
        r.insert(0, '0')
    tmp = r[0]
    r[0] = r[2]
    r[2] = tmp
    return str(''.join(r))


def push():
    return program_input


def pop(value):
    print(value)


def jnz(cond, value):
    if cond != 0:
        return value


def jz(cond, value):
    if cond == 0:
        return value


def lt(a, b, pos):
    if a < b:
        program[pos] = 1
    else:
        program[pos] = 0


def eq(a, b, pos):
    if a == b:
        program[pos] = 1
    else:
        program[pos] = 0


def halt():
    exit()


oc = {1: (add, 2, True), 2: (mul, 2, True), 3: (push, 0, True), 4: (pop, 1, False), 5: (jnz, 2, True),
      6: (jz, 2, True), 7: (lt, 3, False), 8: (eq, 3, False), 99: (halt, 0, False)}

ip_modifiers = {5, 6}


def process():
    ip = 0
    while True:
        instruction = convert(program[ip])
        op_code = int(instruction[-2:])
        op = oc[op_code][0]

        if op_code == 99:
            op()

        arg_values = []
        args = oc[op_code][1]
        for i in range(args):
            ip += 1
            index = program[ip]
            if instruction[i] == position_mode:
                value = program[index]
            elif instruction[i] == immediate_mode:
                value = index
            else:
                print('error')

            arg_values.append(value)

        ip += 1
        if oc[op_code][2]:
            ret_value = op(*arg_values)
            if op_code in ip_modifiers:
                if ret_value is not None:
                    ip = ret_value
            else:
                program[program[ip]] = ret_value
                ip += 1
        else:
            op(*arg_values)


with open('input') as ifile:
    for line in ifile:
        program = [int(x) for x in line.split(',')]
        process()
