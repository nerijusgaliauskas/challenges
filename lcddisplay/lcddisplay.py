#110104

def scale(h, num):
    output = num
    while h > 1:
        output_tmp = []
        for i in output:
            trail = []
            part1 = i[:len(i) - 2]
            part2 = i[len(i) - 2:]
            if '-' in i:
                trail = [part1 + '-  ']
            elif '|' in i:
                if '|' in part2:
                    trail = [part1 + ' | ', part1 + ' | ']
                else:
                    trail = [part1 + '   ', part1 + '   ']
            else:
                trail = [part1 + '   ']
            output_tmp += trail
        output = output_tmp
        h -= 1
    return output

def zero(h):
    output = [
        ' -  ',
        '| | ',
        '    ',
        '| | ',
        ' -  ',
    ]
    return scale(h, output)

def one(h):
    output = [
        '  ',
        '| ',
        '  ',
        '| ',
        '  ',
    ]
    return scale(h, output)

def two(h):
    output = [
        ' -  ',
        '  | ',
        ' -  ',
        '|   ',
        ' -  ',
    ]
    return scale(h, output)

def three(h):
    output = [
        '-  ',
        ' | ',
        '-  ',
        ' | ',
        '-  ',
    ]
    return scale(h, output)

def four(h):
    output = [
        '    ',
        '| | ',
        ' -  ',
        '  | ',
        ' -  ',
    ]
    return scale(h, output)

def five(h):
    output = [
        ' -  ',
        '|   ',
        ' -  ',
        '  | ',
        ' -  ',
    ]
    return scale(h, output)

def six(h):
    output = [
        ' -  ',
        '|   ',
        ' -  ',
        '| | ',
        ' -  ',
    ]
    return scale(h, output)

def seven(h):
    output = [
        '-  ',
        ' | ',
        '   ',
        ' | ',
        '   ',
    ]
    return scale(h, output)

def eight(h):
    output = [
        ' -  ',
        '| | ',
        ' -  ',
        '| | ',
        ' -  ',
    ]
    return scale(h, output)

def nine(h):
    output = [
        ' -  ',
        '| | ',
        ' -  ',
        '  | ',
        ' -  ',
    ]
    return scale(h, output)


def num_to_str(h, num):
    output = []
    for i in list(num):
        if i == '0':
            output.append(zero(h))
        elif i == '1':
            output.append(one(h))
        elif i == '2':
            output.append(two(h))
        elif i == '3':
            output.append(three(h))
        elif i == '4':
            output.append(four(h))
        elif i == '5':
            output.append(five(h))
        elif i == '6':
            output.append(six(h))
        elif i == '7':
            output.append(seven(h))
        elif i == '8':
            output.append(eight(h))
        elif i == '9':
            output.append(nine(h))
    return output

data_in = []
with open('input.txt', 'r') as f:
    for line in f:
        content = line.split()
        if len(content) == 2:
            h = int(content[0])
            if 0 < h and h < 11:
                num = int(content[1])
                if -1 < num and num < 100000000:
                    data_in.append(num_to_str(h, str(num)))

data_out = ''
for i in range(len(data_in)):
    num = data_in[i]
    for j in range(len(num[0])):
        for k in range(len(num)):
            data_out += num[k][j]
        data_out += '\n'
    data_out += '\n'

with open('output.txt', 'w') as f:
    f.write(data_out.strip('\n'))
