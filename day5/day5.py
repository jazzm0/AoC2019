position_mode = '0'
immediate_mode = '1'

program_input = 5


def add(program, arg_values, ip, ip_increment):
    program[arg_values[2]] = program[arg_values[0]] + program[arg_values[1]]
    ip += ip_increment
    return ip


def mul(program, arg_values, ip, ip_increment):
    program[arg_values[2]] = program[arg_values[0]] * program[arg_values[1]]
    ip += ip_increment
    return ip


def push(program, arg_values, ip, ip_increment):
    program[arg_values[0]] = program_input
    ip += ip_increment
    return ip


def pop(program, arg_values, ip, ip_increment):
    print(program[arg_values[0]])
    ip += ip_increment
    return ip


def jnz(program, arg_values, ip, ip_increment):
    if program[arg_values[0]] != 0:
        ip = program[arg_values[1]]
    else:
        ip += ip_increment
    return ip


def jz(program, arg_values, ip, ip_increment):
    if program[arg_values[0]] == 0:
        ip = program[arg_values[1]]
    else:
        ip += ip_increment
    return ip


def lt(program, arg_values, ip, ip_increment):
    if program[arg_values[0]] < program[arg_values[1]]:
        program[arg_values[2]] = 1
    else:
        program[arg_values[2]] = 0
    ip += ip_increment
    return ip


def eq(program, arg_values, ip, ip_increment):
    if program[arg_values[0]] == program[arg_values[1]]:
        program[arg_values[2]] = 1
    else:
        program[arg_values[2]] = 0
    ip += ip_increment
    return ip


oc = {1: (add, 4),
      2: (mul, 4),
      3: (push, 2),
      4: (pop, 2),
      5: (jnz, 3),
      6: (jz, 3),
      7: (lt, 4),
      8: (eq, 4)}


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


def process(program):
    ip = 0
    arg_values = [0, 0, 0]
    while True:
        instruction = convert(program[ip])

        op_code = int(instruction[-2:])

        if op_code == 99:
            break

        for i in range(len(arg_values)):
            index = ip + i + 1
            if instruction[i] == position_mode:
                arg_values[i] = program[index]
            elif instruction[i] == immediate_mode:
                arg_values[i] = index
            else:
                print('mode error')

        ip = oc[op_code][0](program, arg_values, ip, oc[op_code][1])


with open('input') as ifile:
    for line in ifile:
        program = [int(x) for x in line.split(',')]
        process(program)
