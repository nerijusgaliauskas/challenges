#110106

# Credits to Andrey Yemelyanov
import os

INPUT = 'input.txt'
OUTPUT = 'output.txt'

if os.path.exists(OUTPUT):
    os.remove(OUTPUT)

case = -1
data_in = []
with open(INPUT, 'r') as file:
    for line in file:
        line_content = line.split()
        if len(line_content) > 0:
            if case > -1:
                data_in[case].append(int(line_content[0]))
        else:
            case += 1
            data_in.append([])

for list in data_in:
    ram = [0 for i in range(1000)]
    register = [0 for i in range(10)]

    for j in range(len(list)):
        if j < len(ram):
            ram[j] = list[j]

    instruction_counter = 0
    location = 0
    next = True

    while location < len(ram) and next:
        instruction = ram[location]
        instruction_counter += 1
        location += 1

        id = instruction // 100
        param1 = (instruction % 100) // 10
        param2 = (instruction % 100) % 10

        if id == 0:
            if register[param2] != 0:
                location = register[param1]
        elif id == 1:
            if param1 == 0 and param2 == 0:
                with open(OUTPUT, 'a') as file:
                    file.write('{}\n\n'.format(instruction_counter))
                next = False
        elif id == 2:
            register[param1] = param2
        elif id == 3:
            register[param1] = (register[param1] + param2) % 1000
        elif id == 4:
            register[param1] = (register[param1] * param2) % 1000
        elif id == 5:
            register[param1] = register[param2]
        elif id == 6:
            register[param1] = (register[param1] + register[param2]) % 1000
        elif id == 7:
            register[param1] = (register[param1] * register[param2]) % 1000
        elif id == 8:
            register[param1] = ram[register[param2]]
        elif id == 9:
            ram[register[param2]] = register[param1]
