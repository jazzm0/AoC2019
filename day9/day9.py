position_mode = 0
immediate_mode = 1
relative_mode = 2


class Machine:
    def __init__(self, program):
        self.program = program.copy()
        self.program_input = []
        self.ip = 0
        self.program_output = 0
        self.relative_base = 0

    def address(self, a):
        if a[0] == position_mode:
            return a[1]
        elif a[0] == relative_mode:
            return a[1] + self.relative_base
        else:
            print('error')

    def value(self, a):
        if a[0] == position_mode:
            return self.program[a[1]]
        elif a[0] == immediate_mode:
            return a[1]
        elif a[0] == relative_mode:
            return self.program[a[1] + self.relative_base]
        else:
            print('error')

    def add(self, arg_values, ip_increment):
        self.program[self.address(arg_values[2])] = self.value(arg_values[0]) + self.value(arg_values[1])
        self.ip += ip_increment

    def mul(self, arg_values, ip_increment):
        self.program[self.address(arg_values[2])] = self.value(arg_values[0]) * self.value(arg_values[1])
        self.ip += ip_increment

    def push(self, arg_values, ip_increment):
        self.program[self.address(arg_values[0])] = self.program_input.pop(0)
        self.ip += ip_increment

    def pop(self, arg_values, ip_increment):
        self.program_output = self.value(arg_values[0])
        print(self.program_output)
        self.ip += ip_increment

    def jnz(self, arg_values, ip_increment):
        if self.value(arg_values[0]) != 0:
            self.ip = self.value(arg_values[1])
        else:
            self.ip += ip_increment

    def jz(self, arg_values, ip_increment):
        if self.value(arg_values[0]) == 0:
            self.ip = self.value(arg_values[1])
        else:
            self.ip += ip_increment

    def lt(self, arg_values, ip_increment):
        if self.value(arg_values[0]) < self.value(arg_values[1]):
            self.program[self.address(arg_values[2])] = 1
        else:
            self.program[self.address(arg_values[2])] = 0
        self.ip += ip_increment

    def eq(self, arg_values, ip_increment):
        if self.value(arg_values[0]) == self.value(arg_values[1]):
            self.program[self.address(arg_values[2])] = 1
        else:
            self.program[self.address(arg_values[2])] = 0
        self.ip += ip_increment

    def off(self, arg_values, ip_increment):
        self.relative_base += self.value(arg_values[0])
        self.ip += ip_increment

    oc = {1: (add, 4),
          2: (mul, 4),
          3: (push, 2),
          4: (pop, 2),
          5: (jnz, 3),
          6: (jz, 3),
          7: (lt, 4),
          8: (eq, 4),
          9: (off, 2)}

    @staticmethod
    def convert(instruction):
        return instruction % 100, [(instruction % 1000) // 100, (instruction % 10000) // 1000, instruction // 10000]

    def add_input(self, inp):
        self.program_input.append(inp)

    def process(self):
        while True:
            op_code, modes = self.convert(self.program[self.ip])

            if op_code == 99:
                break

            arg_values = []
            for i in range(len(modes)):
                index = self.ip + i + 1
                arg_values.append((modes[i], self.program[index]))

            self.oc[op_code][0](self, arg_values, self.oc[op_code][1])


with open('input') as ifile:
    for line in ifile:
        program = [int(x) for x in line.split(',')]

for i in range(1000):
    program.append(0)

m = Machine(program)
m.add_input(2)
m.process()
