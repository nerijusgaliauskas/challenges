#110101

import sys

def cycle_length(n):
    cl = 1
    while n > 1:
        cl += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    return cl

def max_cycle_length(m, n):
    max_cl = 1
    for i in range(m, n + 1):
        cl = cycle_length(i)
        if max_cl < cl:
            max_cl = cl
    return max_cl

def read_data(name):
    data = []
    f = open(name, 'r')
    for i in f:
        data.append([int(j) for j in i.split()])
    f.close()
    return data

def write_data(data, name):
    f = open(name, 'w')
    f.write(data)
    f.close()

data_r = read_data('input.txt')
data_w = ''
for i in data_r:
    data_w += '{} {} {}\n'.format(i[0], i[1], max_cycle_length(i[0], i[1]))
write_data(data_w, 'output.txt')
