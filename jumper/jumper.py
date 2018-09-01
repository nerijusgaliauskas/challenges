#110201

import sys

N_MIN = 0
N_MAX = 3000

def read_data(input):
    output = []
    with open(input, 'r') as file:
        for line in file:
            content = line.split()
            content_len = len(content)
            if content_len > 0:
                n = int(content[0])
                if N_MIN < n and n < N_MAX:
                    if n == content_len:
                        output.append([int(content[i]) for i in range(1, n)])
                    else:
                        raise Exception('invalid length of sequence '
                            '(entered: {}; expected: {})'
                            .format(content_len, n))
                else:
                    raise Exception('invalid length of sequence '
                        '(entered: {}; expected: between {} and {})'
                        .format(n, N_MIN + 1, N_MAX - 1))
    return output

def process_data(data):
    output = ''
    for i in data:
        modules = []
        for j in range(len(i) - 1):
            modules.append(abs(i[j] - i[j + 1]))
        if sorted(modules) == list(range(1, len(i))):
            output += 'Jolly\n'
        else:
            output += 'Not jolly\n'
    return output

def write_data(data, output):
    with open(output, 'w') as file:
        file.write(data.strip())

try:
    data_in = read_data('input.txt')
    data_out = process_data(data_in)
    write_data(data_out, 'output.txt')
except Exception as e:
    print('Error: {}'.format(e))
    sys.exit()
