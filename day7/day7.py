from itertools import permutations

position_mode = '0'
immediate_mode = '1'


class Machine:
    def __init__(self, program, phase):
        self.program = program.copy()
        self.program_input = [phase]
        self.ip = 0
        self.program_output = 0

    def add(self, arg_values, ip_increment):
        self.program[arg_values[2]] = self.program[arg_values[0]] + self.program[arg_values[1]]
        self.ip += ip_increment

    def mul(self, arg_values, ip_increment):
        self.program[arg_values[2]] = self.program[arg_values[0]] * self.program[arg_values[1]]
        self.ip += ip_increment

    def push(self, arg_values, ip_increment):
        self.program[arg_values[0]] = self.program_input.pop(0)
        self.ip += ip_increment

    def pop(self, arg_values, ip_increment):
        self.program_output = self.program[arg_values[0]]
        # print(program_output)
        self.ip += ip_increment

    def jnz(self, arg_values, ip_increment):
        if self.program[arg_values[0]] != 0:
            self.ip = self.program[arg_values[1]]
        else:
            self.ip += ip_increment

    def jz(self, arg_values, ip_increment):
        if self.program[arg_values[0]] == 0:
            self.ip = self.program[arg_values[1]]
        else:
            self.ip += ip_increment

    def lt(self, arg_values, ip_increment):
        if self.program[arg_values[0]] < self.program[arg_values[1]]:
            self.program[arg_values[2]] = 1
        else:
            self.program[arg_values[2]] = 0
        self.ip += ip_increment

    def eq(self, arg_values, ip_increment):
        if self.program[arg_values[0]] == self.program[arg_values[1]]:
            self.program[arg_values[2]] = 1
        else:
            self.program[arg_values[2]] = 0
        self.ip += ip_increment

    oc = {1: (add, 4),
          2: (mul, 4),
          3: (push, 2),
          4: (pop, 2),
          5: (jnz, 3),
          6: (jz, 3),
          7: (lt, 4),
          8: (eq, 4)}

    @staticmethod
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

    def process(self, inp):
        self.program_input.append(inp)
        while True:
            instruction = self.convert(program[self.ip])

            op_code = int(instruction[-2:])

            if op_code == 99:
                break

            arg_values = []
            for i in range(3):
                index = self.ip + i + 1
                if instruction[i] == position_mode:
                    if index < len(self.program):
                        arg_values.append(self.program[index])
                elif instruction[i] == immediate_mode:
                    arg_values.append(index)
                else:
                    print('mode error')

            self.oc[op_code][0](self, arg_values, self.oc[op_code][1])
            if op_code == 4:
                return self.program_output


with open('input') as ifile:
    for line in ifile:
        program = [int(x) for x in line.split(',')]

outputs = []
for settings in permutations(range(5)):
    program_output = 0
    for i in settings:
        m = Machine(program, i)
        program_output = m.process(program_output)
        outputs.append(program_output)

print(max(outputs))

outputs = []
programs = []
for i in permutations(range(5, 10)):
    machines = [Machine(program, phase) for phase in i]

    output = 0
    while True:
        for machine in machines:
            output = machine.process(output)

        if output:
            outputs.append(output)
        else:
            break

print(max(outputs))
