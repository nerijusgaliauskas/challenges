#110105

import sys
import os

INPUT = 'input.txt'
OUTPUT = 'output.txt'

if os.path.exists(OUTPUT):
    os.remove(OUTPUT)

try:
    with open(INPUT, 'r') as f:
        image = []
        m = 0
        n = 0
        for line_cont in f:
            if len(line_cont) > 0:
                command = line_cont[0]
                params = line_cont[1:].split()

                if command == 'I':
                    if len(params) > 1:
                        m = int(params[0])
                        n = int(params[1])
                        if (0 < m < 251 and 0 < n < 251):
                            image = [['O' for i in range(m)] for j in range(n)]
                    else:
                        raise Exception('the command "{}" has {} parameter(s)'
                                        .format(command, 2))
                elif command == 'C':
                    image = [['O' for i in range(m)] for j in range(n)]

                elif command == 'L':
                    if len(params) > 2:
                        x = int(params[0]) - 1
                        y = int(params[1]) - 1
                        color = params[2]
                        image[y][x] = color
                    else:
                        raise Exception('the command "{}" has {} parameter(s)'
                                        .format(command, 3))

                elif command == 'V':
                    if len(params) > 3:
                        x = int(params[0]) - 1
                        y1 = int(params[1]) - 1
                        y2 = int(params[2]) - 1
                        color = params[3]
                        for i in range(y1, y2 + 1):
                            image[i][x] = color
                    else:
                        raise Exception('the command "{}" has {} parameter(s)'
                                        .format(command, 4))

                elif command == 'H':
                    if len(params) > 3:
                        x1 = int(params[0]) - 1
                        x2 = int(params[1]) - 1
                        y = int(params[2]) - 1
                        color = params[3]
                        for i in range(x1, x2 + 1):
                            image[y][i] = color
                    else:
                        raise Exception('the command "{}" has {} parameter(s)'
                                        .format(command, 4))

                elif command == 'K':
                    if len(params) > 4:
                        x1 = int(params[0]) - 1
                        y1 = int(params[1]) - 1
                        x2 = int(params[2]) - 1
                        y2 = int(params[3]) - 1
                        color = params[4]
                        for i in range(y1, y2 + 1):
                            for j in range(x1, x2 + 1):
                                image[i][j] = color
                    else:
                        raise Exception('the command "{}" has {} parameter(s)'
                                        .format(command, 5))

                elif command == 'F':
                    if len(params) > 2:
                        x = int(params[0]) - 1
                        y = int(params[1]) - 1
                        color = params[2]
                        color_old = image[y][x]
                        if color != color_old:
                            region = [(x, y)]
                            while len(region) > 0:
                                xy = region.pop()
                                x = xy[0]
                                y = xy[1]
                                image[y][x] = color
                                for i in [-1, 1]:
                                    if -1 < x + i and x + i < m:
                                        if image[y][x + i] == color_old:
                                            region.append((x + i, y))
                                for j in [-1, 1]:
                                    if -1 < y + j and y + j < n:
                                        if image[y + j][x] == color_old:
                                            region.append((x, y + j))
                    else:
                        raise Exception('the command "{}" has {} parameter(s)'
                                        .format(command, 3))

                elif command == 'S':
                    if len(params) > 0:
                        name = params[0]
                        data_out = '{}\n'.format(name)
                        for i in range(n):
                            for j in range(m):
                                data_out += '{}'.format(image[i][j])
                            data_out += '\n'
                        with open(OUTPUT, 'a') as f:
                            f.write(data_out)
                    else:
                        raise Exception('the command "{}" has {} parameter(s)'
                                        .format(command, 1))

                elif command == 'X':
                    sys.exit()

except Exception as e:
    print(e)
